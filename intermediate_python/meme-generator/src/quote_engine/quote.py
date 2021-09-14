"""QuoteModule"""


class QuoteModel:
    """Defines a quote model."""

    def __init__(self, author: str, body: str):
        self.author = author
        self.body = body

    def __str__(self):
        return f'"{self.body}" - {self.author}'
