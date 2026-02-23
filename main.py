"""Main script to demonstrate the Reservation System."""

from src.hotel import Hotel
from src.customer import Customer
from src.reservation import Reservation


def main():
    """Executes a sample flow of the reservation system."""
    print("--- INICIANDO SISTEMA DE RESERVAS ---\n")

    # 1. Crear un Hotel
    print("1. Creando un hotel nuevo...")
    Hotel.create_hotel("H100", "Grand Hotel Tec", "Monterrey", 10)
    Hotel.display_hotel("H100")

    # 2. Crear un Cliente
    print("\n2. Creando un cliente nuevo...")
    Customer.create_customer("C100", "Alex", "a00517113@tec.mx")
    Customer.display_customer("C100")

    # 3. Hacer una Reserva
    print("\n3. Creando una reserva...")
    # El cliente C100 reserva en el hotel H100
    if Reservation.create_reservation("R100", "C100", "H100"):
        print("¡Reserva R100 creada con éxito!")

    # Ver cómo bajó el número de habitaciones del hotel
    print("\nEstado del hotel después de la reserva:")
    Hotel.display_hotel("H100")

    # 4. Cancelar la Reserva
    print("\n4. Cancelando la reserva...")
    if Reservation.cancel_reservation("R100"):
        print("¡Reserva R100 cancelada!")

    # Ver cómo se recuperó la habitación del hotel
    print("\nEstado del hotel después de la cancelación:")
    Hotel.display_hotel("H100")

    print("\n--- FIN DE LA EJECUCIÓN ---")


if __name__ == "__main__":
    main()
