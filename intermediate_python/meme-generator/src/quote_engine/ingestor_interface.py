"""IngestorInterface"""
from abc import ABC, abstractmethod
from typing import List
from .quote import QuoteModel


class IngestorInterface(ABC):
    """An interface for all ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Checks if file is readable."""

        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses a certain datafile and returns a list of quotes"""
