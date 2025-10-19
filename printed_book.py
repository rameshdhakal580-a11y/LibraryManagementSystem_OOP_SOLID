from book import Book

class PrintedBook(Book):
    def calculate_late_fee(self, days):
        # Example: $1 per day
        return 1 * days
