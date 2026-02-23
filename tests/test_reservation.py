"""Unit tests for the Reservation class."""

import unittest
import os
import src.customer
import src.hotel
import src.reservation
from src.customer import Customer
from src.hotel import Hotel
from src.reservation import Reservation

TEST_CUST_FILE = "test_res_customers.json"
TEST_HOTEL_FILE = "test_res_hotels.json"
TEST_RES_FILE = "test_res_reservations.json"


class TestReservation(unittest.TestCase):
    """Test cases for Reservation operations."""

    def setUp(self):
        """Set up test file paths and clean environment."""
        src.customer.FILE_PATH = TEST_CUST_FILE
        src.hotel.FILE_PATH = TEST_HOTEL_FILE
        src.reservation.FILE_PATH = TEST_RES_FILE
        for file_path in [TEST_CUST_FILE, TEST_HOTEL_FILE, TEST_RES_FILE]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def tearDown(self):
        """Remove test files after execution."""
        for file_path in [TEST_CUST_FILE, TEST_HOTEL_FILE, TEST_RES_FILE]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_create_reservation(self):
        """Test creating a valid reservation."""
        Customer.create_customer("C1", "John", "john@mail.com")
        Hotel.create_hotel("H1", "Hotel A", "City", 5)

        result = Reservation.create_reservation("R1", "C1", "H1")
        self.assertTrue(result)

        # Duplicate reservation
        result2 = Reservation.create_reservation("R1", "C1", "H1")
        self.assertFalse(result2)

    def test_create_reservation_invalid_entities(self):
        """Test reservation with invalid customer or hotel."""
        Customer.create_customer("C1", "John", "john@mail.com")
        Hotel.create_hotel("H1", "Hotel A", "City", 5)

        # Invalid customer
        self.assertFalse(Reservation.create_reservation("R2", "C99", "H1"))
        # Invalid hotel
        self.assertFalse(Reservation.create_reservation("R3", "C1", "H99"))

    def test_cancel_reservation(self):
        """Test canceling an existing reservation."""
        Customer.create_customer("C1", "John", "john@mail.com")
        Hotel.create_hotel("H1", "Hotel A", "City", 5)
        Reservation.create_reservation("R1", "C1", "H1")

        self.assertTrue(Reservation.cancel_reservation("R1"))
        self.assertFalse(Reservation.cancel_reservation("R99"))

    def test_invalid_json(self):
        """Test handling of invalid JSON file in reservations."""
        with open(TEST_RES_FILE, "w", encoding="utf-8") as file:
            file.write("INVALID JSON")
        data = Reservation._load_data()  # pylint: disable=protected-access
        self.assertEqual(data, {})
