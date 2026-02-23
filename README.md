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

## Pruebas y Calidad de Código

El proyecto fue desarrollado utilizando buenas prácticas de ingeniería de software, cumpliendo con los siguientes criterios:

* **Pruebas Unitarias:** Implementadas con el módulo estándar `unittest`.
* **Cobertura de Código:** Se alcanzó un **97% de cobertura** total (`coverage`), superando el 85% requerido.
* **Estándar PEP-8:** El código fuente pasó las validaciones de análisis estático sin errores ni advertencias utilizando `flake8` y logrando una calificación perfecta en `pylint`.

## Ejecución del Sistema (`main.py`)

A continuación se muestra el registro (log) de ejecución del archivo principal para pruebas manuales, el cual simula el flujo de creación de hoteles, clientes y el procesamiento de una reserva:

```text
$ uv run python main.py
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

## Ejecucion del coverage
```text
$ uv run coverage run -m unittest discover -s tests
Error: Customer C1 already exists.
.Error: Customer C99 not found.
.Customer: John (john@mail.com)
Error: Customer C99 not found.
.Error: Invalid data in customers file.
.Customer: Johnny (john@mail.com)
Error: Customer C99 not found.
.Error: Hotel H1 already exists.
.Error: Hotel H99 not found.
.Hotel: Hotel A, Location: City
Error: Hotel H99 not found.
.Error: Invalid data in hotels file.
.Hotel: Hotel A, Location: City
Error: Hotel H99 not found.
.Error: No rooms available in Hotel H1.
Error: Hotel H99 not found.
Error: Hotel H99 not found.
.Customer: John (john@mail.com)
Hotel: Hotel A, Location: City
Error: Reservation R99 not found.
.Customer: John (john@mail.com)
Hotel: Hotel A, Location: City
Customer: John (john@mail.com)
Hotel: Hotel A, Location: City
Error: Reservation R1 already exists.
.Error: Customer C99 not found.
Error: Cannot create reservation. Invalid Customer.
Customer: John (john@mail.com)
Error: Hotel H99 not found.
Error: Cannot create reservation. Invalid Hotel.
.Error: Invalid data in reservations file.
.
----------------------------------------------------------------------
Ran 15 tests in 0.038s

OK
```

## Ejecucion de los tests
```
$ uv run coverage report -m
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
src\__init__.py                 0      0   100%
src\customer.py                67      2    97%   38, 85
src\hotel.py                   91      3    97%   44, 89, 91
src\reservation.py             58      2    97%   44, 71
tests\test_customer.py         39      1    97%   18
tests\test_hotel.py            46      1    98%   18
tests\test_reservation.py      46      1    98%   27
---------------------------------------------------------
TOTAL                         347     10    97%
```

