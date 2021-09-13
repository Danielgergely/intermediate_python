from typing import List
import docx
from ingestorInterface import IngestorInterface
from quote import QuoteModel


class DOCXImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('This file is not a .docx')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split(' - ')
                quote = QuoteModel(author, body)
                quotes.append(quote)

        return quotes


if __name__ == "__main__":
    quotes = DOCXImporter.parse('DogQuotesDOCX.docx')
    a = 10
