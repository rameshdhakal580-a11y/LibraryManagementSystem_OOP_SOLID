class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Price: ${self.__price}"

    def calculate_late_fee(self, days_late):
        raise NotImplementedError("Subclass must implement abstract method")
