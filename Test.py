import unittest
from AccountManage import PersonalAccount, Amount

class TestPersonalAccount(unittest.TestCase):
    def setUp(self):
        self.acc = PersonalAccount(12345, "Test User")

    def test_initial_balance(self):
        self.assertEqual(self.acc.get_balance(), 0.0)

    def test_deposit(self):
        self.acc.deposit(100.0)
        self.assertEqual(self.acc.get_balance(), 100.0)
        self.assertEqual(len(self.acc.transactions), 1)

    def test_withdraw_success(self):
        self.acc.deposit(100.0)
        self.acc.withdraw(40.0)
        self.assertEqual(self.acc.get_balance(), 60.0)

    def test_insufficient_funds(self):
        self.acc.deposit(50.0)
        self.acc.withdraw(100.0)
        self.assertEqual(self.acc.get_balance(), 50.0)  # Balance should not change

    def test_operator_overloading(self):
        self.acc + 200.0
        self.assertEqual(self.acc.get_balance(), 200.0)
        self.acc - 50.0
        self.assertEqual(self.acc.get_balance(), 150.0)

if __name__ == '__main__':
    unittest.main()