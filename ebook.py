from book import Book

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def calculate_late_fee(self, days_late):
        return days_late * 0.5
