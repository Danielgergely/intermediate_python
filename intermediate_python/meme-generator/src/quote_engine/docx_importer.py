"""Docx Ingestor"""

from typing import List
import docx
from .ingestor_interface import IngestorInterface
from .quote import QuoteModel


class DocxIngestor(IngestorInterface):
    """Reads a word file and returns quotes."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses a word document."""

        if not cls.can_ingest(path):
            raise Exception('This file is not a .docx')

        quotes = []
        try:
            doc = docx.Document(path)

            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    body, author = paragraph.text.split(' - ')
                    quote = QuoteModel(author, body)
                    quotes.append(quote)

            return quotes
        except Exception:
            raise Exception(f"Something went wrong while processing {path}") from None
