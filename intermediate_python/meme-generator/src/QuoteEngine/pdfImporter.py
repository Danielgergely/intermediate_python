from typing import List
import os
import subprocess
from ingestorInterface import IngestorInterface
from textImporter import TextImporter
from quote import QuoteModel


class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('This file is not a .pdf')

        text_file = './pdf_to_text.txt'
        with open('pdf_to_text.txt', 'w') as fp:
            pass
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextImporter.parse(text_file)
        os.remove(text_file)
        return quotes


if __name__ == "__main__":
    quotes = PDFImporter.parse('DogQuotesPDF.pdf')
