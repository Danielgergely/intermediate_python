"""Web-browser implementation of the meme generator app"""

import random
import os
import requests
from flask import Flask, render_template, request
import io
from quote_engine import Ingestor
from meme_engine import MemeEngine
from pathlib import Path

# static_dir = str(Path.cwd().joinpath("src").joinpath("static"))
#
app = Flask(__name__)

meme = MemeEngine(output_dir="./static",
                  font=Path.cwd().joinpath("fonts").joinpath("LilitaOne-Regular.ttf"))


def setup():
    """ Load all resources """
    cwd = Path.cwd()
    data_path = cwd.joinpath("_data")
    dog_quotes = data_path.joinpath("DogQuotes")
    quote_files = [dog_quotes.joinpath("DogQuotesTXT.txt"),
                   dog_quotes.joinpath("DogQuotesDOCX.docx"),
                   dog_quotes.joinpath("DogQuotesPDF.pdf"),
                   dog_quotes.joinpath("DogQuotesCSV.csv")]

    _quotes = []
    for file in quote_files:
        _quotes.extend(Ingestor.parse(str(file)))

    images_path = data_path.joinpath("photos").joinpath("dog")

    images = []
    for file in os.listdir(images_path):
        images.append(os.path.join(images_path, file))

    return _quotes, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    random_image = random.randint(0, (len(imgs) - 1))
    random_quote = random.randint(0, (len(quotes) - 1))

    img = imgs[random_image]
    quote = quotes[random_quote]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form['image_url']
    img_data = requests.get(img_url).content
    body = request.form['body']
    author = request.form['author']

    image_file = io.BytesIO(img_data)

    path = meme.make_meme(source_img=image_file,
                          text=body,
                          author=author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
