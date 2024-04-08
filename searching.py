import json

def pattern_search(sequence, pattern):
    """
    Searches for all occurrences of a pattern in a given sequence. Automatically
    skips to the next character in the sequence upon the first mismatch.
    :param sequence: (str), the sequence to search in
    :param pattern: (str), the pattern to search for
    :return: set of positions (indexes) where the pattern occurs in the sequence
    """
    positions = set()  # Use a set to store positions to avoid duplicates
    index = 0
    while index <= len(sequence) - len(pattern):
        match_found = True
        for pattern_index in range(len(pattern)):
            if sequence[index + pattern_index] != pattern[pattern_index]:
                match_found = False
                break  # Break out of the inner loop if a mismatch is found
        if match_found:
            positions.add(index)
            index += 1  # Move to the next character after finding a match
        else:
            index += max(1, pattern_index)  # Skip to the next character or beyond based on the mismatch
    return positions

def read_data(file_name, field):
    """
    Reads json file and returns data based on the specified field.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: data from the json file based on field
    """
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
        return data.get(field, None)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None

def main():
    dna_sequence = read_data("sequential.json", "dna_sequence")
    if dna_sequence is not None:
        print("DNA Sequence:", dna_sequence)
        # Define the pattern to search for, e.g., "ATA"
        search_pattern = "ATA"
        # Call the pattern_search function
        pattern_positions = pattern_search(dna_sequence, search_pattern)
        print(f"Positions of pattern '{search_pattern}' in the sequence:", pattern_positions)
    else:
        print("No data to search.")

if __name__ == '__main__':
    main()
