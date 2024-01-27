import datetime

def main():
    # Accept user's name as input
    user_name = input("Enter your name: ")

    # Greet the user with a personalized welcome message
    print(f"Hello, {user_name}! Welcome to the age calculator.")

    # Ask the user to input their age
    try:
        user_age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")
        return

    # Calculate the year when the user will turn 100 years old
    current_year = datetime.datetime.now().year
    year_turn_100 = current_year + (100 - user_age)

    # Print the calculated year
    print(f"{user_name}, you will turn 100 years old in the year {year_turn_100}.")

if __name__ == "__main__":
    main()
