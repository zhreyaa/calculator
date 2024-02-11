import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_logarithm(x):
    return math.log(x)

def power(x, b):
    return x ** b

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def main():
    while True:
        print("\nScientific Calculator Menu:")
        print("1. Square root function (√x)")
        print("2. Factorial function (x!)")
        print("3. Natural logarithm function (ln(x))")
        print("4. Power function (x^b)")
        print("5. Addition")
        print("6. Subtraction")
        print("7. Multiplication")
        print("8. Division")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            x = float(input("Enter the value of x: "))
            result = square_root(x)
            print("Square root of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '2':
            x = int(input("Enter the value of x: "))
            result = factorial(x)
            print("Factorial of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '3':
            x = float(input("Enter the value of x: "))
            result = natural_logarithm(x)
            print("Natural logarithm of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '4':
            x = float(input("Enter the value of x: "))
            b = float(input("Enter the value of b: "))
            result = power(x, b)
            print(x, "raised to the power of", b, "is:", result)
            print("-----------------------------------------")
        elif choice == '5':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = addition(x, y)
            print("Result of addition:", result)
            print("-----------------------------------------")
        elif choice == '6':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = subtraction(x, y)
            print("Result of subtraction:", result)
            print("-----------------------------------------")
        elif choice == '7':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = multiplication(x, y)
            print("Result of multiplication:", result)
            print("-----------------------------------------")
        elif choice == '8':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number (non-zero): "))
            result = division(x, y)
            print("Result of division:", result)
            print("-----------------------------------------")
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
if choice == '1':
            x = float(input("Enter the value of x: "))
            result = square_root(x)
            print("Square root of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '2':
            x = int(input("Enter the value of x: "))
            result = factorial(x)
            print("Factorial of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '3':
            x = float(input("Enter the value of x: "))
            result = natural_logarithm(x)
            print("Natural logarithm of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '4':
            x = float(input("Enter the value of x: "))
            b = float(input("Enter the value of b: "))
            result = power(x, b)
            print(x, "raised to the power of", b, "is:", result)
            print("-----------------------------------------")
        elif choice == '5':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = addition(x, y)
            print("Result of addition:", result)
            print("-----------------------------------------")
        elif choice == '6':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = subtraction(x, y)
            print("Result of subtraction:", result)
            print("-----------------------------------------")
        elif choice == '7':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = multiplication(x, y)
            print("Result of multiplication:", result)
            print("-----------------------------------------")
        elif choice == '8':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number (non-zero): "))
            result = division(x, y)
            print("Result of division:", result)
            print("-----------------------------------------")
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
if choice == '1':
            x = float(input("Enter the value of x: "))
            result = square_root(x)
            print("Square root of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '2':
            x = int(input("Enter the value of x: "))
            result = factorial(x)
            print("Factorial of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '3':
            x = float(input("Enter the value of x: "))
            result = natural_logarithm(x)
            print("Natural logarithm of", x, "is:", result)
            print("-----------------------------------------")
        elif choice == '4':
            x = float(input("Enter the value of x: "))
            b = float(input("Enter the value of b: "))
            result = power(x, b)
            print(x, "raised to the power of", b, "is:", result)
            print("-----------------------------------------")
        elif choice == '5':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = addition(x, y)
            print("Result of addition:", result)
            print("-----------------------------------------")
        elif choice == '6':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = subtraction(x, y)
            print("Result of subtraction:", result)
            print("-----------------------------------------")
        elif choice == '7':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            result = multiplication(x, y)
            print("Result of multiplication:", result)
            print("-----------------------------------------")
        elif choice == '8':
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number (non-zero): "))
            result = division(x, y)
            print("Result of division:", result)
            print("-----------------------------------------")
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
