# Sistema de Reservas - Actividad 6.2

**Autor:** `Alejandro Gonzalez Almazan`
**Matrícula:** `A00517113`

## Descripción del Proyecto

Este repositorio contiene la implementación de un sistema de reservas en Python, correspondiente a la Actividad 6.2, Ejercicio de programación 3. El sistema está diseñado para gestionar tres entidades principales mediante programación orientada a objetos:

1. **Hotel:** Creación, eliminación, consulta y modificación de información.
2. **Customer (Cliente):** Creación, eliminación, consulta y modificación de información.
3. **Reservation (Reserva):** Creación y cancelación de reservas vinculando clientes y hoteles.

El proyecto implementa persistencia de datos utilizando archivos JSON, incluye mecanismos para el manejo de errores ante datos inválidos y está desarrollado bajo un enfoque estricto de calidad de código.

## Estructura del Proyecto

```text
/
├── data/                  # Archivos .json generados para la persistencia de datos
├── src/                   # Código fuente de las clases principales
│   ├── customer.py
│   ├── hotel.py
│   └── reservation.py
├── tests/                 # Casos de prueba unitarios
│   ├── test_customer.py
│   ├── test_hotel.py
│   └── test_reservation.py
└── README.md