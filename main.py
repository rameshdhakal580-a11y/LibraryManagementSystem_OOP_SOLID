# 1. Import your classes
from ebook import EBook
from printed_book import PrintedBook
from payment import PaymentProcessor, PayPalPayment, CreditCardPayment

# 2. Main function
def main():
    # Create book objects
    ebook = EBook("Python 101", "John Doe", 15.0)
    printed_book = PrintedBook("Clean Code", "Robert Martin", 25.0)

    # Show book info
    print(f"Title: {ebook.title}, Author: {ebook.author}, Price: ${ebook.price}")
    print(f"EBook Late Fee (3 days): ${ebook.calculate_late_fee(3)}")

    print(f"Title: {printed_book.title}, Author: {printed_book.author}, Price: ${printed_book.price}")
    print(f"Printed Late Fee (3 days): ${printed_book.calculate_late_fee(3)}")

    # Payment processing
    processor = PaymentProcessor()
    print(processor.process_payment(PayPalPayment(), 20))
    print(processor.process_payment(CreditCardPayment(), 30))

# 3. Run main function
if __name__ == "__main__":
    main()
