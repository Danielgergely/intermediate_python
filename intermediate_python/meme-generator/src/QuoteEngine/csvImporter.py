from typing import List
import pandas as pd
from .ingestorInterface import IngestorInterface
from .quote import QuoteModel


class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('This file is not a .csv')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['author'], row['body'])
            quotes.append(new_quote)

        return quotes
