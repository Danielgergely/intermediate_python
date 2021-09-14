"""The Quote Engine handles the reading of different
type of files and returns a quote ('some text' - author)
"""

from .csv_importer import CSVIngestor
from .ingestor_interface import IngestorInterface
from .docx_importer import DocxIngestor
from .pdf_importer import PDFIngestor
from .ingestor import Ingestor
from .quote import QuoteModel
