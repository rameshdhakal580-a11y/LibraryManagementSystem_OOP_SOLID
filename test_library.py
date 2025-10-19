import unittest
from ebook import EBook
from printed_book import PrintedBook
from payment import PaymentProcessor, PayPalPayment, CreditCardPayment

# Test Book subclasses
class TestBooks(unittest.TestCase):
    def setUp(self):
        self.ebook = EBook("Python 101", "John Doe", 15.0)
        self.printed_book = PrintedBook("Clean Code", "Robert Martin", 25.0)

    def test_ebook_late_fee(self):
        self.assertEqual(self.ebook.calculate_late_fee(3), 1.5)

    def test_printed_late_fee(self):
        self.assertEqual(self.printed_book.calculate_late_fee(3), 3.0)

# Test Payment methods
class TestPayments(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()

    def test_paypal_payment(self):
        self.assertEqual(self.processor.process_payment(PayPalPayment(), 20), "Paid $20 using PayPal.")

    def test_credit_card_payment(self):
        self.assertEqual(self.processor.process_payment(CreditCardPayment(), 30), "Paid $30 using Credit Card.")

# Run tests
if __name__ == "__main__":
    unittest.main()
