class Review:
    def __init__(self, description: str, user, product):
        self.description = description
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review for product: {self.product.name}\n{self.description}\nwritten by: {self.user.name}"

