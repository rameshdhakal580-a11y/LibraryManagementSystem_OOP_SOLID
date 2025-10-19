from ebook import EBook
from printed_book import PrintedBook
from payment import CreditCardPayment, PayPalPayment, PaymentProcessor

def main():
    ebook = EBook("Python 101", "John Doe", 15, "5MB")
    printed = PrintedBook("Clean Code", "Robert Martin", 25, 350)

    print(ebook.get_details())
    print(f"EBook Late Fee (3 days): ${ebook.calculate_late_fee(3)}")

    print(printed.get_details())
    print(f"Printed Late Fee (3 days): ${printed.calculate_late_fee(3)}")

    payment = PaymentProcessor(PayPalPayment())
    print(payment.process_payment(20))

if __name__ == "__main__":
    main()
