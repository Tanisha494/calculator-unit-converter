
def get_number(message):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def arithmetic():
    print("\n--- Basic Arithmetic ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose an operation (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Error! Cannot divide by zero.")
            return
        result = num1 / num2

    print("Result:", result)


def unit_conversion():
    print("\n--- Unit Conversion ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose a conversion (1-2): ")

    if choice == "1":
        km = get_number("Enter distance in kilometers: ")
        miles = km * 0.621371
        print("Distance in miles:", round(miles, 2))

    elif choice == "2":
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", round(fahrenheit, 2))

    else:
        print("Invalid conversion choice!")


def main():
    while True:
        print("\n==============================")
        print("   CALCULATOR & UNIT CONVERTER")
        print("==============================")
        print("1. Basic Arithmetic")
        print("2. Unit Conversion")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            arithmetic()
        elif choice == "2":
            unit_conversion()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
