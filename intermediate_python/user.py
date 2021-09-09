from product import Product
from review import Review


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.reviews = []

    def __str__(self):
        return f"The name of this user is: {self.name} with id: #{self.id}"

    def sell_product(self, product_name: str, description: str, price: float):
        product = Product(product_name, description, self, price, availability=True)
        return product

    @staticmethod
    def buy_product(product: Product):
        product.available = product.available - 1

    def write_review(self, description: str, product: Product):
        review = Review(description, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review
