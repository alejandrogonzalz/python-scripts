"""
Programa para calcular el total de ventas basado en un catálogo de precios.
Cumple con los estándares PEP-8 y maneja errores de archivos JSON.
"""

import sys
import json
import time


def load_json_file(file_path):
    """Carga un archivo JSON y maneja errores de lectura."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{file_path}' no tiene un formato válido.")
    return None


def calculate_total_sales(prices, sales):
    """Calcula el costo total cruzando precios y ventas."""
    total_cost = 0.0
    errors = []

    # Crear un diccionario para búsqueda rápida de precios
    price_map = {
        item["title"]: item["price"]
        for item in prices
        if "title" in item and "price" in item
    }

    for record in sales:
        product = record.get("product")
        quantity = record.get("quantity", 0)

        if product in price_map:
            total_cost += price_map[product] * quantity
        else:
            errors.append(f"Producto no encontrado en catálogo: {product}")

    return total_cost, errors


def main():
    """Función principal para la ejecución del programa."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py prices.json sales.json")
        return

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    prices_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if prices_data is None or sales_data is None:
        return

    total, errors = calculate_total_sales(prices_data, sales_data)

    elapsed_time = time.time() - start_time

    # Formatear resultados
    output = (
        f"{'=' * 30}\n"
        f"REPORTE DE VENTAS\n"
        f"{'=' * 30}\n"
        f"Total de ventas: ${total:,.2f}\n"
        f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
        f"{'=' * 30}\n"
    )

    if errors:
        output += "\nErrores detectados:\n" + "\n".join(errors) + "\n"

    # Imprimir en pantalla y guardar en archivo
    print(output)
    with open("SalesResults.txt", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    main()
