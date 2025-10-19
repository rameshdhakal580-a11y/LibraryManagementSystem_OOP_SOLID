import unittest
from ebook import EBook
from printed_book import PrintedBook

class TestLibrary(unittest.TestCase):
    def test_late_fee(self):
        ebook = EBook("Book A", "Author A", 10, "3MB")
        printed = PrintedBook("Book B", "Author B", 20, 200)
        self.assertEqual(ebook.calculate_late_fee(2), 1.0)
        self.assertEqual(printed.calculate_late_fee(2), 2.0)

if __name__ == "__main__":
    unittest.main()
