
class Product:
    def __init__(self, name: str, description: str, seller, price: float, availability):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = availability

    def __str__(self):
        string = f"Product name: {self.name}\nDescription: {self.description}\nThe seller is: {self.seller.name}\n"
        if self.reviews:
            string = string + "These are all the reviews of this product: \n"
            for index, review in enumerate(self.reviews):
                string = string + f"    #{index +1}: {review.description}\n"
        string = string + f"The price is: {self.price}\n"
        if self.available:
            string = string + "This product is available\n"
        else:
            string = string + "Sorry, at the moment this product is not available"
        return string

