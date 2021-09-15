"""Main Ingestor"""

from typing import List, Optional
from .ingestor_interface import IngestorInterface
from .pdf_importer import PDFIngestor
from .docx_importer import DocxIngestor
from .text_importer import TextIngestor
from .csv_importer import CSVIngestor
from .quote import QuoteModel


class Ingestor(IngestorInterface):
    """Decides which helper class should be used to read a file."""

    importers = [PDFIngestor, DocxIngestor, TextIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> Optional[List[QuoteModel]]:
        try:
            for importer in cls.importers:
                if importer.can_ingest(path):
                    return importer.parse(path)
            return None
        except Exception as e:
            raise Exception(f"An error occured while processing {path},exception was {str(e)}")
