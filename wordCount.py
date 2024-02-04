import sys
import time

def main():
    """
    Main function to count words and print results.
    """
    # Requirement 1: Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    # Requirement 3: Handle invalid data
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            words_count = {}
            total_words = 0

            for line in file:
                words = line.strip().split()
                total_words += len(words)

                for word in words:
                    # Convert to lowercase for case-insensitive counting
                    word_lower = word.lower()
                    words_count[word_lower] = words_count.get(word_lower, 0) + 1

    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    start_time = time.time()

    # Requirement 2: Print results on screen and write to file
    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write("Word\t\tFrequency\n")
        print("Word\t\tFrequency")
        print("------------------------")

        # Sort words alphabetically in descending order
        sorted_words_count = sorted(words_count.items(), key=lambda x: x[0], reverse=False)

        for word, count in sorted_words_count:
            # Align columns using formatting
            result_file.write(f"{word.ljust(20)}{str(count).rjust(10)}\n")
            print(f"{word.ljust(20)}{str(count).rjust(10)}")

        # Requirement 7: Include time elapsed in results
        result_file.write(f"\nTotal Words: {total_words}\n")
        end_time = time.time()
        elapsed_time = end_time - start_time
        result_file.write(f"Time Elapsed: {elapsed_time} seconds\n")
        print("\nTotal Words:", total_words)
        print("Time Elapsed:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
