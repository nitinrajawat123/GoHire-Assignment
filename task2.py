def filter_even_numbers(numbers):
    # Use a list comprehension to filter even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def get_user_input():
    try:
        # Prompt the user to enter a list of numbers
        input_string = input("Enter a list of numbers separated by spaces: ")
        
        # Convert the input string into a list of integers
        input_numbers = [int(num) for num in input_string.split()]

        return input_numbers
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")
        return []

def main():
    # Get the user's input list
    input_numbers = get_user_input()

    # Call the function to filter even numbers
    even_numbers = filter_even_numbers(input_numbers)

    # Print the original list and the list containing only even numbers
    print("Original List:", input_numbers)
    print("Even Numbers:", even_numbers)

if __name__ == "__main__":
    main()
