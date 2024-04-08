import json

def binary_search(sorted_sequence, target_number):
    """
    Performs binary search on a sorted sequence to find the target number.
    :param sorted_sequence: (list of int), sorted list of numbers
    :param target_number: (int), the number to search for
    :return: index of the target_number in sorted_sequence or None if not found
    """
    left, right = 0, len(sorted_sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_sequence[mid] == target_number:
            return mid
        elif sorted_sequence[mid] < target_number:
            left = mid + 1
        else:
            right = mid - 1
    return None

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
    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    if ordered_numbers is not None:
        print("Ordered Numbers:", ordered_numbers)
        # Define the number to search for, e.g., 42
        target_number = 42
        # Call the binary_search function
        index = binary_search(ordered_numbers, target_number)
        if index is not None:
            print(f"Number {target_number} found at index {index}.")
        else:
            print(f"Number {target_number} not found in the sequence.")
    else:
        print("No data to search.")

if __name__ == '__main__':
    main()
