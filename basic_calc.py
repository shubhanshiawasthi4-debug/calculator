
def get_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("Invalid input! Please enter a number.")


# Basic Arithmetic
def calculator():
    print("\n--- BASIC CALCULATOR ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        return

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if choice == "1":
        print("Result:", a + b)

    elif choice == "2":
        print("Result:", a - b)

    elif choice == "3":
        print("Result:", a * b)

    elif choice == "4":
        if b == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", a / b)


# Unit Conversion
def unit_converter():
    print("\n--- UNIT CONVERTER ---")
    print("1. Kilometres to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        km = get_number("Enter distance in kilometres: ")
        miles = km * 0.621371
        print("Distance in miles:", round(miles, 2))

    elif choice == "2":
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", round(fahrenheit, 2))

    else:
        print("Invalid choice!")


# Currency Conversion
def currency_converter():
    print("\n--- CURRENCY CONVERTER ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = input("Enter your choice (1-2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    amount = get_number("Enter amount: ")
    rate = get_number("Enter current exchange rate (INR per USD): ")

    if rate <= 0:
        print("Exchange rate must be greater than zero!")
        return

    if amount < 0:
        print("Amount cannot be negative!")
        return

    if choice == "1":
        result = amount / rate
        print("Amount in USD:", round(result, 2))

    elif choice == "2":
        result = amount * rate
        print("Amount in INR:", round(result, 2))


# Main Menu
while True:
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Basic Calculator")
    print("2. Unit Converter")
    print("3. Currency Converter")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        unit_converter()

    elif choice == "3":
        currency_converter()

    elif choice == "4":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
