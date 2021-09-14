"""Web-browser implementation of the meme generator app"""

import random
import os
import requests
from flask import Flask, render_template, request

from quote_engine import Ingestor
from meme_engine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    _quotes = []
    for file in quote_files:
        _quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

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
    tmp = './tmp_img.jpg'
    with open(tmp, 'wb').write(img_data):
        pass

    path = meme.make_meme(tmp, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
