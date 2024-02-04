import sys
import time

def convert_to_binary(decimal_number):
    """
    Convert a decimal number to binary representation.

    Args:
        decimal_number (int): The decimal number.

    Returns:
        str: Binary representation.
    """
    if decimal_number == 0:
        return "0"

    sign = '-' if decimal_number < 0 else ''
    decimal_number = abs(decimal_number)

    binary_representation = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_representation = str(remainder) + binary_representation
        decimal_number //= 2

    return f"{sign}{binary_representation}" if binary_representation else "0"

def convert_to_hexadecimal(decimal_number):
    """
    Convert a decimal number to hexadecimal representation.

    Args:
        decimal_number (int): The decimal number.

    Returns:
        str: Hexadecimal representation.
    """
    if decimal_number == 0:
        return "0x0"

    sign = '-' if decimal_number < 0 else ''
    decimal_number = abs(decimal_number)

    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_representation = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_representation = hexadecimal_digits[remainder] + hexadecimal_representation
        decimal_number //= 16

    return f"{sign}0x{hexadecimal_representation}" if hexadecimal_representation else "0x0"

def main():
    """
    Main function to convert numbers and print results.
    """
    # Requirement 1: Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers2.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    # Requirement 3: Handle invalid data
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            numbers = []
            for line in file:
                try:
                    value = float(line.strip())
                    numbers.append(int(value))  # Convert to integer
                except ValueError:
                    print(f"Skipping non-numeric value: {line.strip()}")

    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    start_time = time.time()

    binary_results = [convert_to_binary(num) for num in numbers]
    hexadecimal_results = [convert_to_hexadecimal(num) for num in numbers]

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Requirement 2: Print results on screen and write to file
    with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
        for i, num in enumerate(numbers):
            result_file.write(f"Number: {num}, Binary: {binary_results[i]}, Hexadecimal: {hexadecimal_results[i]}\n")
            print(f"Number: {num}, Binary: {binary_results[i]}, Hexadecimal: {hexadecimal_results[i]}")

        # Requirement 7: Include time elapsed in results
        result_file.write(f"\nTime Elapsed: {elapsed_time} seconds\n")
        print(f"\nTime Elapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
