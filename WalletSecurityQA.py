import unittest
import threading

from DigitalWallet import DigitalWallet


class WalletSecurityQA(unittest.TestCase):

    # 1. Normal transaction
    def test_normal_transaction(self):

        wallet = DigitalWallet("TestUser", 50000)

        result = wallet.deposit(5000)

        self.assertTrue(result)
        self.assertEqual(wallet.balance, 55000)

    # 2. Insufficient balance
    def test_insufficient_balance(self):

        wallet = DigitalWallet("TestUser", 1000)

        result = wallet.withdraw(5000)

        self.assertFalse(result)
        self.assertEqual(wallet.balance, 1000)

    # 3. Daily limit
    def test_daily_limit(self):

        wallet = DigitalWallet("TestUser", 50000, daily_limit=10000)

        result1 = wallet.deposit(8000)
        result2 = wallet.deposit(5000)

        self.assertTrue(result1)
        self.assertFalse(result2)

        self.assertEqual(wallet.balance, 58000)

    # 4. Multiple failed PINs
    def test_multiple_failed_pins(self):

        wallet = DigitalWallet("TestUser", 50000)

        wallet.failed_pin_attempt()
        wallet.failed_pin_attempt()

        self.assertEqual(wallet.failed_pins, 2)

    # 5. Suspicious transaction
    def test_suspicious_transaction(self):

        wallet = DigitalWallet("TestUser", 100000)

        result = wallet.deposit(60000)

        self.assertTrue(result)
        self.assertTrue(wallet.check_fraud(60000))

    # 6. Duplicate transaction
    def test_duplicate_transaction(self):

        wallet = DigitalWallet("TestUser", 50000)

        wallet.deposit(5000)
        wallet.deposit(5000)

        self.assertEqual(len(wallet.transactions), 2)
        self.assertEqual(wallet.balance, 60000)

    # 7. Negative amount
    def test_negative_amount(self):

        wallet = DigitalWallet("TestUser", 50000)

        result = wallet.deposit(-1000)

        self.assertFalse(result)
        self.assertEqual(wallet.balance, 50000)

    # 8. Concurrent transactions
    def test_concurrent_transactions(self):

        wallet = DigitalWallet("TestUser", 50000)

        def deposit_money():
            wallet.deposit(1000)

        threads = []

        for i in range(5):

            t = threading.Thread(target=deposit_money)

            threads.append(t)

            t.start()

        for t in threads:
            t.join()

        self.assertEqual(wallet.balance, 55000)


if __name__ == "__main__":
    unittest.main()
