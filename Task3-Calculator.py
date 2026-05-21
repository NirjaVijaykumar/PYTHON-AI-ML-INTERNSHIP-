def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def main():
    print("\nSimple Calculator")
    print("="*30)

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            a, b = get_numbers()
            result = add(a, b)
            print(f"\nResult: {a} + {b} = {result}\n")

        elif choice == "2":
            a, b = get_numbers()
            result = subtract(a, b)
            print(f"\nResult: {a} - {b} = {result}\n")

        elif choice == "3":
            a, b = get_numbers()
            result = multiply(a, b)
            print(f"\nResult: {a} x {b} = {result}\n")

        elif choice == "4":
            a, b = get_numbers()
            result = divide(a, b)
            if result is None:
                print("\nError: Division by zero is not allowed.\n")
            else:
                print(f"\nResult: {a} / {b} = {result}\n")

        elif choice == "5":
            print("\nExiting Calculator. Goodbye!\n")
            break

        else:
            print("\nInvalid choice. Please enter 1-5.\n")

main()
