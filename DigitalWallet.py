from datetime import datetime, timedelta
import threading


class DigitalWallet:

    def __init__(self, name, balance=0, daily_limit=100000):
        self.name = name
        self.balance = balance
        self.daily_limit = daily_limit
        self.daily_total = 0
        self.transactions = []
        self.failed_pins = 0
        self.transaction_times = []
        self.lock = threading.Lock()

    # 1. Account creation
    def account_creation(self):
        print("Account created for:", self.name)
        return True

    # Record transaction
    def record_transaction(self, amount, transaction_type):
        now = datetime.now()

        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "time": now
        })

        self.transaction_times.append(now)

        # Keep only transactions from the last 10 minutes
        ten_minutes_ago = now - timedelta(minutes=10)

        self.transaction_times = [
            t for t in self.transaction_times
            if t >= ten_minutes_ago
        ]

    # Fraud detection
    def check_fraud(self, amount):
        suspicious = False

        # More than 5 transactions in 10 minutes
        if len(self.transaction_times) > 5:
            suspicious = True
            print("Suspicious transaction: More than 5 transactions in 10 minutes")

        # Large transaction
        if amount > 50000:
            suspicious = True
            print("Suspicious transaction: Large amount")

        # Multiple failed PIN attempts
        if self.failed_pins >= 2:
            suspicious = True
            print("Suspicious transaction: Multiple failed PIN attempts")

        # Unusual transaction amount
        if amount > self.daily_limit:
            suspicious = True
            print("Suspicious transaction: Unusual transaction amount")

        return suspicious

    # 2. Deposit
    def deposit(self, amount):

        with self.lock:

            if amount <= 0:
                print("Invalid deposit amount")
                return False

            if self.daily_total + amount > self.daily_limit:
                print("Daily transaction limit exceeded")
                return False

            self.balance += amount
            self.daily_total += amount

            self.record_transaction(amount, "Deposit")

            print("Deposit successful:", amount)

            self.check_fraud(amount)

            return True

    # 3. Withdrawal
    def withdraw(self, amount):

        with self.lock:

            if amount <= 0:
                print("Invalid withdrawal amount")
                return False

            if amount > self.balance:
                print("Insufficient balance")
                return False

            if self.daily_total + amount > self.daily_limit:
                print("Daily transaction limit exceeded")
                return False

            self.balance -= amount
            self.daily_total += amount

            self.record_transaction(amount, "Withdrawal")

            print("Withdrawal successful:", amount)

            self.check_fraud(amount)

            return True

    # 4. Money transfer
    def transfer(self, amount, receiver):

        with self.lock:

            if amount <= 0:
                print("Invalid transfer amount")
                return False

            if amount > self.balance:
                print("Insufficient balance")
                return False

            if self.daily_total + amount > self.daily_limit:
                print("Daily transaction limit exceeded")
                return False

            self.balance -= amount
            self.daily_total += amount

            self.record_transaction(amount, "Transfer")

            print("Transfer successful:", amount, "to", receiver)

            self.check_fraud(amount)

            return True

    # 5. Transaction history
    def transaction_history(self):

        for transaction in self.transactions:
            print(transaction)

        return self.transactions

    # 6. Daily transaction limit
    def check_daily_limit(self, amount):

        return self.daily_total + amount <= self.daily_limit

    # 7. Balance verification
    def verify_balance(self):

        print("Current Balance:", self.balance)

        return self.balance

    # Failed PIN attempt
    def failed_pin_attempt(self):

        self.failed_pins += 1

        print("Failed PIN attempt:", self.failed_pins)

        if self.failed_pins >= 2:
            print("Suspicious transaction: Multiple failed PIN attempts")

        return True

    # Reset PIN attempts
    def reset_pin_attempts(self):

        self.failed_pins = 0

        return True


# Demonstration
if __name__ == "__main__":

    wallet = DigitalWallet("Vaishnavi", 50000)

    wallet.account_creation()

    wallet.deposit(10000)

    wallet.withdraw(5000)

    wallet.transfer(20000, "TestUser")

    wallet.failed_pin_attempt()
    wallet.failed_pin_attempt()

    wallet.transaction_history()

    wallet.verify_balance()
