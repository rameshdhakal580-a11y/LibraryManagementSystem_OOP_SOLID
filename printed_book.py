from book import Book

class PrintedBook(Book):
    def __init__(self, title, author, price, pages):
        super().__init__(title, author, price)
        self.pages = pages

    def calculate_late_fee(self, days_late):
        return days_late * 1.0
