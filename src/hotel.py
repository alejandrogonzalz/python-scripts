"""Module for Hotel management."""

import json
import os

FILE_PATH = "data/hotels.json"


class Hotel:
    """Represents a hotel in the reservation system."""

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Converts the hotel object to a dictionary."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms,
        }

    @classmethod
    def _load_data(cls):
        """Loads hotels from the JSON file."""
        if not os.path.exists(FILE_PATH):
            return {}
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Invalid data in hotels file.")
            return {}

    @classmethod
    def _save_data(cls, data):
        """Saves the hotels dictionary to the JSON file."""
        directory = os.path.dirname(FILE_PATH)
        if directory:  # <-- Agregamos esta validación
            os.makedirs(directory, exist_ok=True)
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Creates a new hotel and saves it."""
        hotels = cls._load_data()
        if str(hotel_id) in hotels:
            print(f"Error: Hotel {hotel_id} already exists.")
            return False

        new_hotel = cls(hotel_id, name, location, rooms)
        hotels[str(hotel_id)] = new_hotel.to_dict()
        cls._save_data(hotels)
        return True

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Deletes a hotel by ID."""
        hotels = cls._load_data()
        if str(hotel_id) in hotels:
            del hotels[str(hotel_id)]
            cls._save_data(hotels)
            return True
        print(f"Error: Hotel {hotel_id} not found.")
        return False

    @classmethod
    def display_hotel(cls, hotel_id):
        """Displays hotel information."""
        hotels = cls._load_data()
        hotel = hotels.get(str(hotel_id))
        if hotel:
            print(f"Hotel: {hotel['name']}, Location: {hotel['location']}")
            return hotel
        print(f"Error: Hotel {hotel_id} not found.")
        return None

    @classmethod
    def modify_hotel(cls, hotel_id, name=None, location=None, rooms=None):
        """Modifies existing hotel information."""
        hotels = cls._load_data()
        if str(hotel_id) in hotels:
            if name:
                hotels[str(hotel_id)]["name"] = name
            if location:
                hotels[str(hotel_id)]["location"] = location
            if rooms is not None:
                hotels[str(hotel_id)]["rooms"] = rooms
            cls._save_data(hotels)
            return True
        print(f"Error: Hotel {hotel_id} not found.")
        return False

    @classmethod
    def reserve_room(cls, hotel_id):
        """Decreases the available rooms of a hotel."""
        hotels = cls._load_data()
        if str(hotel_id) in hotels:
            if hotels[str(hotel_id)]["rooms"] > 0:
                hotels[str(hotel_id)]["rooms"] -= 1
                cls._save_data(hotels)
                return True
            print(f"Error: No rooms available in Hotel {hotel_id}.")
            return False
        print(f"Error: Hotel {hotel_id} not found.")
        return False

    @classmethod
    def cancel_reservation(cls, hotel_id):
        """Increases the available rooms of a hotel."""
        hotels = cls._load_data()
        if str(hotel_id) in hotels:
            hotels[str(hotel_id)]["rooms"] += 1
            cls._save_data(hotels)
            return True
        print(f"Error: Hotel {hotel_id} not found.")
        return False
