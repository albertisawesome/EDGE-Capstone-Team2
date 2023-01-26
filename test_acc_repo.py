import unittest
from models.address import Address
from repositories.address import AddressRepository
from models.customer import Customer
from repositories.customer import CustomerRepository
from models.account import Account
from repositories.account import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def create_examples(self):
        self.addressRepository = AddressRepository()
        self.customerRepository = CustomerRepository()
        self.accountRepository = AccountRepository()
        self.inserted_address = self.addressRepository.insert(
            Address(id=0, address="111 Doe Avenue", city="Docker", state="CA", zip_code="12345"))
        self.inserted_customer = self.customerRepository.insert(
            Customer(id=0, first_name="John", last_name="Doe", address=self.inserted_address, email_address="test@cg.com"))
        self.inserted_account = self.accountRepository.insert(
            Account(id=0, account_number="12345", customer=self.inserted_customer, current_balance=50.00))

    def test_get_by_account_number(self):
        self.create_examples()

        get_account = self.accountRepository.get_by_account_number(
            self.inserted_account.account_number)
        self.inserted_account.customer = Customer.construct(
            id=self.inserted_customer.id)
        self.assertEqual(get_account, self.inserted_account)

if __name__ == "__main__":
    unittest.main()