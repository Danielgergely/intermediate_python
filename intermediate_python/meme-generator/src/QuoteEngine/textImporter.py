from typing import List
from ingestorInterface import IngestorInterface
from quote import QuoteModel


class TextImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('This file is not a .txt')

        quotes = []
        with open(path) as f:
            lines = f.readlines()

            for line in lines:
                body, author = line.split(' - ')
                quote = QuoteModel(author, body)
                quotes.append(quote)

        return quotes
