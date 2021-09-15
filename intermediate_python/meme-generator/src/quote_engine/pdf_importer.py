"""PDFIngestor"""

from pathlib import Path
from typing import List, Optional
import os
import subprocess
from .ingestor_interface import IngestorInterface
from .text_importer import TextIngestor
from .quote import QuoteModel


class PDFIngestor(IngestorInterface):
    """Converts a pdf to a text file and then uses the TextIngestor to
    read the text file and return quotes.
    """
    _pdf_to_text_exe = Path("C:/tools/pdftotext.exe")
    allowed_extensions = ['pdf']

    def __init__(self, pdf_to_text_exe: Optional[Path] = None):
        if pdf_to_text_exe is not None:
            self._pdf_to_text_exe = pdf_to_text_exe

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses a PDF."""

        if not cls.can_ingest(path):
            raise Exception('This file is not a .pdf')

        text_file = 'pdf_to_text.txt'
        try:
            with open('pdf_to_text.txt', 'w', encoding='utf-8'):
                pass
            cmd = f"{cls._pdf_to_text_exe} -layout -nopgbrk {path} {text_file}"
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
            quotes = TextIngestor.parse(text_file)
            os.remove(text_file)
            return quotes
        except Exception as e:
            raise Exception(f"Something went wrong while parsing {path}, exception was {str(e)}")
