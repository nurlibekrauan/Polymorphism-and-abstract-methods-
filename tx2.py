from abc import ABC, abstractmethod


class PaymentError(Exception):
    """Класс для ошибок, связанных с платежами"""

    def __init__(self, message):
        super().__init__(message)


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        """Обработка платежа"""
        pass

    @abstractmethod
    def refund(self):
        """Возврат средств"""
        pass

    @abstractmethod
    def log_transaction(self, message):
        """Логирование успешной транзакции"""
        pass

    @abstractmethod
    def log_error(self, error):
        """Логирование ошибки"""
        pass
print('sdf')

class CreditCardPayment(Payment):
    def __init__(self, card_number, amount):
        super().__init__(amount)
        self.card_number = card_number
        self.fee_percent = 0.02  # Комиссия 2%

    def process_payment(self):
        fee = self.amount * self.fee_percent
        total = self.amount + fee

        # Имитация ошибки
        if len(self.card_number) != 16:
            error = f"Неверный номер карты: {self.card_number}"
            self.log_error(error)
            raise PaymentError(error)
        if self.amount <= 0:
            error = f"Недостаточно средств для транзакции: {self.amount}"
            self.log_error(error)
            raise PaymentError(error)

        # Успешная транзакция
        self.log_transaction(
            f"Платеж {total} с карты {self.card_number} выполнен успешно."
        )

    def refund(self):
        self.log_transaction(
            f"Возврат {self.amount} на карту {self.card_number} выполнен."
        )

    def log_transaction(self, message):
        print(f"[CreditCard] {message}")

    def log_error(self, error):
        print(f"[CreditCard ERROR] {error}")


class PayPalPayment(Payment):
    def __init__(self, email, amount):
        super().__init__(amount)
        self.email = email
        self.fee_percent = 0.03  # Комиссия 3%

    def process_payment(self):
        fee = self.amount * self.fee_percent
        total = self.amount + fee

        if "@" not in self.email:
            error = f"Неверный email: {self.email}"
            self.log_error(error)
            raise PaymentError(error)
        if self.amount <= 0:
            error = f"Недостаточно средств для транзакции: {self.amount}"
            self.log_error(error)
            raise PaymentError(error)

        self.log_transaction(
            f"Платеж {total} через PayPal {self.email} выполнен успешно."
        )

    def refund(self):
        self.log_transaction(f"Возврат {self.amount} на PayPal {self.email} выполнен.")

    def log_transaction(self, message):
        print(f"[PayPal] {message}")

    def log_error(self, error):
        print(f"[PayPal ERROR] {error}")


class BankTransferPayment(Payment):
    def __init__(self, account_number, amount):
        super().__init__(amount)
        self.account_number = account_number
        self.fee_percent = 0.01  # Комиссия 1%

    def process_payment(self):
        fee = self.amount * self.fee_percent
        total = self.amount + fee

        if len(self.account_number) != 9:
            error = f"Неверный номер счета: {self.account_number}"
            self.log_error(error)
            raise PaymentError(error)
        if self.amount <= 0:
            error = f"Недостаточно средств для транзакции"
            self.log_error(error)
            raise PaymentError(error)
        self.log_transaction(self.amount)

    def log_error(self, error):
        print(f"[BankTransfer ERROR] {error}")

    def log_transaction(self, amount):
        print(
            f"[BankTransfer] Платеж {amount} на счет {self.account_number} выполнен успешно."
        )

    def refund(self, amount):
        print(f"Возврат комиссии: {amount * self.fee_percent:.2f}")


payments = [
    CreditCardPayment(card_number="1234567898765432", amount=100.0),
    PayPalPayment(email="user@example.com", amount=150.0),
    BankTransferPayment(account_number="123456789", amount=200.0),
]

for payment in payments:
    try:
        payment.process_payment()
    except PaymentError as e:
        payment.log_error(e)
