# pylint: disable=invalid-name
"""
Programa para convertir números a binario y hexadecimal.
Implementa algoritmos de conversión manual sin funciones integradas.
"""

import sys
import time


def to_binary(n):
    """Convierte un número entero a binario usando el algoritmo de división."""
    if n == 0:
        return "0"
    is_negative = n < 0
    num = abs(int(n))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return "-" + binary if is_negative else binary


def to_hexadecimal(n):
    """Convierte un número entero a hexadecimal usando el algoritmo de división."""
    if n == 0:
        return "0"
    is_negative = n < 0
    num = abs(int(n))
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        hexadecimal = hex_chars[num % 16] + hexadecimal
        num //= 16
    return "-" + hexadecimal if is_negative else hexadecimal


def process_file(filename):
    """Lee el archivo y retorna una lista de tuplas con los resultados."""
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                raw = line.strip()
                if raw:
                    try:
                        val = int(float(raw))
                        data.append((val, to_binary(val), to_hexadecimal(val)))
                    except ValueError:
                        print(f"Error: Dato inválido '{raw}' omitido.")
    except FileNotFoundError:
        print(f"Error: Archivo '{filename}' no encontrado.")
        return None
    return data


def main():
    """Función principal."""
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        return

    results = process_file(sys.argv[1])
    if results is None:
        return

    elapsed = time.time() - start_time

    # Construcción de la salida para evitar demasiadas variables locales
    header = f"{'ITEM':<5} {'NUMBER':<10} {'BINARY':<20} {'HEX':<10}"
    output = [header, "-" * 50]
    for i, res in enumerate(results, 1):
        output.append(f"{i:<5} {res[0]:<10} {res[1]:<20} {res[2]:<10}")

    output.append("-" * 50)
    output.append(f"Tiempo de ejecución: {elapsed:.4f} segundos")

    final_text = "\n".join(output)
    print(final_text)

    with open("ConvertionResults.txt", "w", encoding='utf-8') as f_out:
        f_out.write(final_text)


if __name__ == "__main__":
    main()
