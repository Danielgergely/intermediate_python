"""Command line implementation of the meme generator app"""

import argparse
import os
import random
from quote_engine import Ingestor, QuoteModel
from meme_engine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(author, body)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create memes from quotes and images"
    )
    parser.add_argument('--path',
                        help="The path of the image used for the meme")

    parser.add_argument('--body', help="The quote you want to write on an image")
    parser.add_argument('--author', help='The author of that great quote')

    args = parser.parse_args()
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    print(generate_meme(args.path, args.body, args.author))
