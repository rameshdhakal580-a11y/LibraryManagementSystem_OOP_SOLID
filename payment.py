from abc import ABC, abstractmethod

# Payment interface
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."


# Payment processor using dependency injection
class PaymentProcessor:
    def process_payment(self, payment_method: Payment, amount):
        return payment_method.pay(amount)
