"""Module for Reservation management."""

import json
import os
from src.hotel import Hotel
from src.customer import Customer

FILE_PATH = "data/reservations.json"


class Reservation:
    """Represents a reservation in the system."""

    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Converts the reservation object to a dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }

    @classmethod
    def _load_data(cls):
        """Loads reservations from the JSON file."""
        if not os.path.exists(FILE_PATH):
            return {}
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Invalid data in reservations file.")
            return {}

    @classmethod
    def _save_data(cls, data):
        """Saves the reservations dictionary to the JSON file."""
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Creates a reservation linking a customer and a hotel."""
        # Verificar que el cliente y el hotel existan
        if not Customer.display_customer(customer_id):
            print("Error: Cannot create reservation. Invalid Customer.")
            return False

        if not Hotel.display_hotel(hotel_id):
            print("Error: Cannot create reservation. Invalid Hotel.")
            return False

        reservations = cls._load_data()
        if str(reservation_id) in reservations:
            print(f"Error: Reservation {reservation_id} already exists.")
            return False

        # Intentar reservar la habitación en el hotel
        if Hotel.reserve_room(hotel_id):
            new_res = cls(reservation_id, customer_id, hotel_id)
            reservations[str(reservation_id)] = new_res.to_dict()
            cls._save_data(reservations)
            return True
        return False

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancels a reservation and frees up the hotel room."""
        reservations = cls._load_data()
        if str(reservation_id) in reservations:
            hotel_id = reservations[str(reservation_id)]["hotel_id"]
            # Liberar la habitación en el hotel
            Hotel.cancel_reservation(hotel_id)
            # Eliminar la reserva del registro
            del reservations[str(reservation_id)]
            cls._save_data(reservations)
            return True
        print(f"Error: Reservation {reservation_id} not found.")
        return False
