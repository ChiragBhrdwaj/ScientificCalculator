import math

def basic_operations():
    print("\nBasic Operations Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    choice = int(input("Enter your choice (1-5): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 / num2
    elif choice == 5:
        result = num1 % num2
    else:
        print("Invalid choice")
        return

    print("Result:", result)

def trigonometric_functions():
    print("\nTrigonometric Functions Menu:")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")

    choice = int(input("Enter your choice (1-3): "))
    angle = float(input("Enter the angle in degrees: "))

    if choice == 1:
        result = math.sin(math.radians(angle))
    elif choice == 2:
        result = math.cos(math.radians(angle))
    elif choice == 3:
        result = math.tan(math.radians(angle))
    else:
        print("Invalid choice")
        return

    print("Result:", result)

def logarithmic_functions():
    print("\nLogarithmic Functions Menu:")
    print("1. Logarithm base 2 (log2)")
    print("2. Logarithm base 10 (log10)")

    choice = int(input("Enter your choice (1-2): "))
    num = float(input("Enter the number: "))

    if choice == 1:
        result = math.log2(num)
    elif choice == 2:
        result = math.log10(num)
    else:
        print("Invalid choice")
        return

    print("Result:", result)

while True:
    print("\nMain Menu:")
    print("1. Basic Operations")
    print("2. Trigonometric Functions")
    print("3. Logarithmic Functions")
    print("4. Exit")

    option = int(input("Enter your choice (1-4): "))

    if option == 1:
        basic_operations()
    elif option == 2:
        trigonometric_functions()
    elif option == 3:
        logarithmic_functions()
    elif option == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
