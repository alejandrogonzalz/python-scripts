"""
Programa para calcular estadísticas descriptivas desde un archivo.
Cumple con PEP-8 y manejo de errores para datos inválidos.
"""

import sys
import time


def calculate_statistics(numbers):
    """Calcula media, mediana, moda, varianza y desviación estándar."""
    count = len(numbers)
    if count == 0:
        return None

    # Ordenar lista para mediana y moda (algoritmo básico)
    sorted_nums = sorted(numbers)

    # Media
    mean = sum(sorted_nums) / count

    # Mediana
    if count % 2 == 0:
        median = (sorted_nums[count // 2 - 1] + sorted_nums[count // 2]) / 2
    else:
        median = sorted_nums[count // 2]

    # Moda
    frequency = {}
    for num in sorted_nums:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]
    mode = modes[0] if len(modes) == 1 else modes

    # Varianza
    variance = sum((x - mean) ** 2 for x in sorted_nums) / count

    # Desviación Estándar
    std_dev = variance ** 0.5

    return {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Std Dev": std_dev
    }


def main():
    """Función principal para ejecución desde línea de comandos."""
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Uso: python compute_statistics.py fileWithData.txt")
        return

    filename = sys.argv[1]
    numbers = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Error: Dato inválido encontrado y omitido: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return

    results = calculate_statistics(numbers)
    elapsed_time = time.time() - start_time

    if results:
        output = (
            f"--- Estadísticas ---\n"
            f"Media: {results['Mean']}\n"
            f"Mediana: {results['Median']}\n"
            f"Moda: {results['Mode']}\n"
            f"Varianza: {results['Variance']}\n"
            f"Desviación Estándar: {results['Std Dev']}\n"
            f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
        )
        print(output)

        with open("StatisticsResults.txt", "w", encoding='utf-8') as f_out:
            f_out.write(output)


if __name__ == "__main__":
    main()
