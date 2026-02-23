"""Unit tests for the Customer class."""

import unittest
import os
import src.customer
from src.customer import Customer

TEST_FILE = "test_customers.json"


class TestCustomer(unittest.TestCase):
    """Test cases for Customer operations."""

    def setUp(self):
        """Set up test file path and clean environment."""
        src.customer.FILE_PATH = TEST_FILE
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        """Remove test file after execution."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_create_customer(self):
        """Test creating a new customer and duplicates."""
        result = Customer.create_customer("C1", "John", "john@mail.com")
        self.assertTrue(result)
        # Attempt to create duplicate
        result2 = Customer.create_customer("C1", "John", "john@mail.com")
        self.assertFalse(result2)

    def test_delete_customer(self):
        """Test deleting an existing and non-existing customer."""
        Customer.create_customer("C1", "John", "john@mail.com")
        self.assertTrue(Customer.delete_customer("C1"))
        self.assertFalse(Customer.delete_customer("C99"))

    def test_display_customer(self):
        """Test displaying customer information."""
        Customer.create_customer("C1", "John", "john@mail.com")
        customer = Customer.display_customer("C1")
        self.assertIsNotNone(customer)
        self.assertEqual(customer["name"], "John")
        self.assertIsNone(Customer.display_customer("C99"))

    def test_modify_customer(self):
        """Test modifying customer data."""
        Customer.create_customer("C1", "John", "john@mail.com")
        self.assertTrue(Customer.modify_customer("C1", name="Johnny"))
        customer = Customer.display_customer("C1")
        self.assertEqual(customer["name"], "Johnny")
        self.assertFalse(Customer.modify_customer("C99", name="No Name"))

    def test_invalid_json(self):
        """Test handling of an invalid JSON file."""
        with open(TEST_FILE, "w", encoding="utf-8") as file:
            file.write("INVALID JSON")
        customers = Customer._load_data()  # pylint: disable=protected-access
        self.assertEqual(customers, {})
