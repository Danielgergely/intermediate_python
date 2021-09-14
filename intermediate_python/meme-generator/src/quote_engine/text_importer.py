"""TextIngestor"""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote import QuoteModel


class TextIngestor(IngestorInterface):
    """Reads a text file and returns quotes."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses a text file."""

        if not cls.can_ingest(path):
            raise Exception('This file is not a .txt')

        quotes = []
        try:
            with open(path, encoding='utf-8') as file:
                lines = file.readlines()

                for line in lines:
                    body, author = line.split(' - ')
                    quote = QuoteModel(author, body)
                    quotes.append(quote)

            return quotes
        except Exception:
            raise Exception(f"Something went wrong while parsing {path}") from None
