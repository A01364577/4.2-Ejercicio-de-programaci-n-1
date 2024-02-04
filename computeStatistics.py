import sys
import time

def calculate_mean(data):
    """
    Calculate the mean of a given dataset.

    Args:
        data (list): The dataset.

    Returns:
        float: The mean value.
    """
    return sum(data) / len(data)

def calculate_median(data):
    """
    Calculate the median of a given dataset.

    Args:
        data (list): The dataset.

    Returns:
        float: The median value.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        middle1 = sorted_data[n//2 - 1]
        middle2 = sorted_data[n//2]
        return (middle1 + middle2) / 2
    return sorted_data[n//2]

def calculate_mode(data):
    """
    Calculate the mode of a given dataset.

    Args:
        data (list): The dataset.

    Returns:
        list: List of modes.
    """
    frequency_dict = {}
    for num in data:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    max_frequency = max(frequency_dict.values())
    mode_list = [key for key, value in frequency_dict.items() if value == max_frequency]
    return mode_list

def calculate_variance(data, mean):
    """
    Calculate the variance of a given dataset.

    Args:
        data (list): The dataset.
        mean (float): The mean value.

    Returns:
        float: The variance value.
    """
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_standard_deviation(variance):
    """
    Calculate the standard deviation from the variance.

    Args:
        variance (float): The variance value.

    Returns:
        float: The standard deviation value.
    """
    return variance ** 0.5

def main():
    """
    Main function to compute statistics.
    """
    # Requirement 1: Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics2.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    # Requirement 3: Handle invalid data
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file]

    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    start_time = time.time()

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    standard_deviation = calculate_standard_deviation(variance)

    end_time = time.time()
    elapsed_time = end_time - start_time

    with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write(f"Mean: {mean}\n")
        result_file.write(f"Median: {median}\n")
        result_file.write(f"Mode: {mode}\n")
        result_file.write(f"Variance: {variance}\n")
        result_file.write(f"Standard Deviation: {standard_deviation}\n")
        result_file.write(f"Time Elapsed: {elapsed_time} seconds\n")

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {standard_deviation}")
    print(f"Time Elapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
