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
```

## Logs de main.py
```
uv run python main.py
--- INICIANDO SISTEMA DE RESERVAS ---

1. Creando un hotel nuevo...
Error: Hotel H100 already exists.
Hotel: Grand Hotel Tec, Location: Monterrey

2. Creando un cliente nuevo...
Error: Customer C100 already exists.
Customer: Alex (alex@estudiante.tec.mx)

3. Creando una reserva...
Customer: Alex (alex@estudiante.tec.mx)
Hotel: Grand Hotel Tec, Location: Monterrey
¡Reserva R100 creada con éxito!

Estado del hotel después de la reserva:
Hotel: Grand Hotel Tec, Location: Monterrey

4. Cancelando la reserva...
¡Reserva R100 cancelada!

Estado del hotel después de la cancelación:
Hotel: Grand Hotel Tec, Location: Monterrey

--- FIN DE LA EJECUCIÓN ---
``` 