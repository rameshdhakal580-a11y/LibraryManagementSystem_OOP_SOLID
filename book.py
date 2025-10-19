class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    # Getters for encapsulation
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    def calculate_late_fee(self, days):
        raise NotImplementedError("Subclasses must implement calculate_late_fee")


