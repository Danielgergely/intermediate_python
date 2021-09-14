"""CSV Ingestor"""

from typing import List
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote import QuoteModel


class CSVIngestor(IngestorInterface):
    """Reads a csv file and returns quotes."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses a .csv file."""

        if not cls.can_ingest(path):
            raise Exception('This file is not a .csv')

        quotes = []
        dataframe = pd.read_csv(path, header=0)

        try:
            for index, row in dataframe.iterrows():
                new_quote = QuoteModel(row['author'], row['body'])
                quotes.append(new_quote)

            return quotes
        except Exception:
            raise Exception(f"Something went wrong while parsing {path}") from None
