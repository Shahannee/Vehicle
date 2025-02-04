from abc import abstractmethod
from enum import Enum

class PaymentType(Enum):
    CREDIT_CARD = "Credit Card"
    PAYPAL = "PayPal"
    CRYPTO = "Cryptocurrency"

class PaymentMethod:

    def __init__(self, payment_amount : int, discount_percentage: int, payment_type : PaymentType):
        self.__payment_amount = payment_amount
        self.__discount_percentage = discount_percentage
        self.payment_type = payment_type

    @property
    def get_payment_amount(self):
        return self.__payment_amount

    @property
    def get_discount_percentage(self):
        return self.__discount_percentage

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def discount(self):
        pass


class CreditCardPayment(PaymentMethod):

    def __init__(self, payment_amount, discount_percentage, payment_type):
        super().__init__(payment_amount, discount_percentage, payment_type)

    def discount(self):
        return f"When paying with Credit card you get {self.get_discount_percentage} % discount."

    def pay(self):
        payment_amount =self.get_payment_amount - (self.get_payment_amount * self.get_discount_percentage / 100)
        return f"Paid {payment_amount} $ using Credit Card."


class PayPalPayment(PaymentMethod):

    def __init__(self, payment_amount, discount_percentage, payment_type):
        super().__init__(payment_amount, discount_percentage, payment_type)

    def pay(self):
        payment_amount = self.get_payment_amount - (self.get_payment_amount * self.get_discount_percentage / 100)
        return f"Paid {payment_amount} $ using PayPal."

    def discount(self):
        return f"When paying with PayPal you get {self.get_discount_percentage} % discount."


class CryptoPayment(PaymentMethod):

    def __init__(self, payment_amount, discount_percentage, payment_type):
        super().__init__(payment_amount, discount_percentage, payment_type)

    def pay(self):
        payment_amount = self.get_payment_amount - (self.get_payment_amount * self.get_discount_percentage / 100)
        return f"Paid {payment_amount} $ using Cryptocurrency."

    def discount(self):
        return f"When paying with Crypto you get {self.get_discount_percentage} % discount."



creditcard = CreditCardPayment(200, 7, PaymentType.CREDIT_CARD)
paypal = PayPalPayment(300, 10, PaymentType.PAYPAL)
crypto = CryptoPayment(150, 5, PaymentType.CRYPTO)
print(creditcard.pay())
print(creditcard.discount())
print(paypal.pay())
print(paypal.discount())
print(crypto.pay())
print(crypto.discount())
