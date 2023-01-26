import unittest
from unittest.mock import Mock
from models.address import Address
from repositories.address import AddressRepository
from models.customer import Customer
from repositories.customer import CustomerRepository
from models.account import Account
from repositories.account import AccountRepository
from services.accountService import AccountService


class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.address = Address(id=1, address="111 Doe Avenue",
                               city="Docker", state="CA", zip_code="12345")
        self.customer = Customer(id=1, first_name="John",
                                 last_name="Doe", address=self.address, email_address="test@cg.com")
        self.account = Account(id=1, account_number="12345",
                               customer=self.customer, current_balance=50.00)
        self.address_repository = Mock()
        self.customer_repository = Mock()
        self.account_repository = Mock()
        self.account_service = AccountService(self.account_repository, self.customer_repository, self.address_repository)

    def test_open_account(self):
        self.address_repository.insert = Mock(return_value=self.address)
        self.customer_repository.insert = Mock(return_value=self.customer)
        self.account_repository.insert = Mock(return_value=self.account)
        new_account = self.account_service.open_account(self.account)
        self.assertEqual(new_account, self.account)

if __name__ == "__main__":
    unittest.main()