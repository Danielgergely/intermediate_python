from user import User

if __name__ == "__main__":
    brianna = User(1, 'Brianna')
    mary = User(2, 'Mary')

    keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.available)  # => True
    mary.buy_product(keyboard)
    print(keyboard.available)  # => False
    review = mary.write_review('This is the worst keyboard ever!', keyboard)
    review = mary.write_review('This is the best keyboard ever!', keyboard)
    review in mary.reviews  # => True
    review in keyboard.reviews  # => True
    # print(mary)
    print(keyboard)
    # print(review)