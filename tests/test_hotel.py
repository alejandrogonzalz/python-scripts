"""Unit tests for the Hotel class."""

import unittest
import os
import src.hotel
from src.hotel import Hotel

TEST_FILE = "test_hotels.json"


class TestHotel(unittest.TestCase):
    """Test cases for Hotel operations."""

    def setUp(self):
        """Set up test file path and clean environment."""
        src.hotel.FILE_PATH = TEST_FILE
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        """Remove test file after execution."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_create_hotel(self):
        """Test creating a new hotel and duplicates."""
        result = Hotel.create_hotel("H1", "Hotel A", "City", 10)
        self.assertTrue(result)
        result2 = Hotel.create_hotel("H1", "Hotel A", "City", 10)
        self.assertFalse(result2)

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        Hotel.create_hotel("H1", "Hotel A", "City", 10)
        self.assertTrue(Hotel.delete_hotel("H1"))
        self.assertFalse(Hotel.delete_hotel("H99"))

    def test_display_hotel(self):
        """Test displaying hotel info."""
        Hotel.create_hotel("H1", "Hotel A", "City", 10)
        hotel = Hotel.display_hotel("H1")
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel["name"], "Hotel A")
        self.assertIsNone(Hotel.display_hotel("H99"))

    def test_modify_hotel(self):
        """Test modifying hotel data."""
        Hotel.create_hotel("H1", "Hotel A", "City", 10)
        self.assertTrue(Hotel.modify_hotel("H1", rooms=15))
        hotel = Hotel.display_hotel("H1")
        self.assertEqual(hotel["rooms"], 15)
        self.assertFalse(Hotel.modify_hotel("H99", name="Fake"))

    def test_reserve_and_cancel_room(self):
        """Test room reservation and cancellation logic."""
        Hotel.create_hotel("H1", "Hotel A", "City", 1)
        self.assertTrue(Hotel.reserve_room("H1"))
        # No rooms left
        self.assertFalse(Hotel.reserve_room("H1"))
        # Invalid hotel
        self.assertFalse(Hotel.reserve_room("H99"))

        # Cancel reservation restores room
        self.assertTrue(Hotel.cancel_reservation("H1"))
        self.assertFalse(Hotel.cancel_reservation("H99"))

    def test_invalid_json(self):
        """Test handling of invalid JSON file."""
        with open(TEST_FILE, "w", encoding="utf-8") as file:
            file.write("INVALID JSON")
        hotels = Hotel._load_data()  # pylint: disable=protected-access
        self.assertEqual(hotels, {})
