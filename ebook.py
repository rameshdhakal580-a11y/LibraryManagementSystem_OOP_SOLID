from book import Book

class EBook(Book):
    def calculate_late_fee(self, days):
        # Example: $0.50 per day
        return 0.5 * days
