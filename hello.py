"""create a basic calculator"""
def add(num1 , num2):
    """Add two number"""
    return num1 + num2

def subtract(num1, num2):
    """Subtract two number"""
    return num1 - num2

def multiply(num1, num2):
    """Multiply two number"""
    return num1 * num2

def divide(num1, num2):
    """Divide two number"""
    return num1 / num2


print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:

    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        try:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num_1, "+", num_2, "=", add(num_1, num_2))

        elif choice == '2':
            print(num_1, "-", num_2, "=", subtract(num_1, num_2))

        elif choice == '3':
            print(num_1, "*", num_2, "=", multiply(num_1, num_2))

        elif choice == '4':
            print(num_1, "/", num_2, "=", divide(num_1, num_2))

        else:
            print("Invalid Input")
