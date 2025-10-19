from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."

class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."

class PaymentProcessor:
    def __init__(self, payment_method: Payment):
        self.payment_method = payment_method

    def process_payment(self, amount):
        return self.payment_method.pay(amount)
