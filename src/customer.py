"""Module for Customer management."""

import json
import os

FILE_PATH = "data/customers.json"


class Customer:
    """Represents a customer in the reservation system."""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Converts the customer object to a dictionary."""
        return {"customer_id": self.customer_id, "name": self.name, "email": self.email}

    @classmethod
    def _load_data(cls):
        """Loads customers from the JSON file."""
        if not os.path.exists(FILE_PATH):
            return {}
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Invalid data in customers file.")
            return {}

    @classmethod
    def _save_data(cls, data):
        """Saves the customers dictionary to the JSON file."""
        directory = os.path.dirname(FILE_PATH)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Creates a new customer and saves it to the file."""
        customers = cls._load_data()
        if str(customer_id) in customers:
            print(f"Error: Customer {customer_id} already exists.")
            return False

        new_customer = cls(customer_id, name, email)
        customers[str(customer_id)] = new_customer.to_dict()
        cls._save_data(customers)
        return True

    @classmethod
    def delete_customer(cls, customer_id):
        """Deletes a customer by ID."""
        customers = cls._load_data()
        if str(customer_id) in customers:
            del customers[str(customer_id)]
            cls._save_data(customers)
            return True
        print(f"Error: Customer {customer_id} not found.")
        return False

    @classmethod
    def display_customer(cls, customer_id):
        """Displays customer information."""
        customers = cls._load_data()
        customer = customers.get(str(customer_id))
        if customer:
            print(f"Customer: {customer['name']} ({customer['email']})")
            return customer
        print(f"Error: Customer {customer_id} not found.")
        return None

    @classmethod
    def modify_customer(cls, customer_id, name=None, email=None):
        """Modifies existing customer information."""
        customers = cls._load_data()
        if str(customer_id) in customers:
            if name:
                customers[str(customer_id)]["name"] = name
            if email:
                customers[str(customer_id)]["email"] = email
            cls._save_data(customers)
            return True
        print(f"Error: Customer {customer_id} not found.")
        return False
