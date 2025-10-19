class PaymentProcessorBadApproach:
    def process_payment(self, payment_type, amount):
        if payment_type == "card":
            print(f"Processing card payment of {amount}")
        elif payment_type == "cash":
            print(f"Processing cash payment of {amount}")
        else:
            raise ValueError("Invalid payment type")


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class CashPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing cash payment of {amount}")

class PayoneerPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Payoneer payment of {amount}")

card_payment = CreditCardPayment()
cash_payment = CashPayment()


def process_payment(payment_processor : PaymentProcessor, amount):
    payment_processor.process_payment(amount)

process_payment(card_payment, 100)
process_payment(cash_payment, 200)
process_payment(PayoneerPayment(), 300)