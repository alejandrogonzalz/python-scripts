# pylint: disable=invalid-name
"""
Programa para contar la frecuencia de palabras en un archivo de texto.
Cumple con PEP-8 y manejo de errores para datos inválidos.
"""

import sys
import time


def count_word_frequencies(word_list):
    """Cuenta la frecuencia de cada palabra en la lista."""
    frequencies = {}
    for word in word_list:
        clean_word = word.strip('.,!?;:"()').lower()
        if clean_word:
            if clean_word in frequencies:
                frequencies[clean_word] += 1
            else:
                frequencies[clean_word] = 1
    return frequencies


def read_words_from_file(filename):
    """Lee el archivo y maneja errores de datos o lectura."""
    all_words = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # Separar por espacios
                words = line.split()
                all_words.extend(words)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return None
    except (UnicodeDecodeError, IOError) as error:
        print(f"Error al procesar el archivo: {error}")
        return None
    return all_words


def main():
    """Función principal."""
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    words = read_words_from_file(sys.argv[1])
    if words is None:
        return

    word_map = count_word_frequencies(words)
    sorted_words = sorted(word_map.items(), key=lambda x: x[1], reverse=True)
    elapsed_time = time.time() - start_time

    # Formateo de salida
    output = [f"{'WORD':<20} {'FREQUENCY':<10}", "-" * 31]
    for word, freq in sorted_words:
        output.append(f"{word:<20} {freq:<10}")

    output.append("-" * 31)
    output.append(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")

    final_results = "\n".join(output)
    print(final_results)

    with open("WordCountResults.txt", "w", encoding="utf-8") as f_out:
        f_out.write(final_results)


if __name__ == "__main__":
    main()
