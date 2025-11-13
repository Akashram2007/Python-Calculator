def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a/b

def calculator():
    print("\n_____ Python Calculator ____")

    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Enter a valid number!")
            continue

        if choice == 5:
            print("Exiting Calculator...Bye!")
            break

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except:
            print("Invalid number!")
            continue

        if choice == 1:
            print("Result =", add(x, y))
        elif choice == 2:
            print("Result =", sub(x, y))
        elif choice == 3:
            print("Result =", mul(x, y))
        elif choice == 4:
            print("Result =", div(x, y))
        else:
            print("Invalid choice!")
            
calculator()