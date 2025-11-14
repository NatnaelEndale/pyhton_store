
def add(n1, n2):
    """It operates in two numbers which add them to gether"""
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide }

def calculator():
    n1 = float(input("Enter the first number: "))
    result = n1
    is_true = True
    while is_true:
        operation = input("Enter the operation(+, -, *, /): ")
        n2 = float(input("Enter the second number: "))
        if operation in operations:
            calculation_function = operations[operation]
            result = calculation_function(n1, n2)
        else:
            print("You entered wrong command!")
        print(result)
        want_contunue = input("do you want to continue operation (y or n): ").lower()
        if want_contunue == "y":
            n1 = result
        else:
            print(f"The result is: {result}")
            want_again = input("DO you want to perform another calculation(y or n): ").lower()
            if want_again == "y":
                is_true = False
                calculator()
            else:
                print("Thanks for using our calculator!")
                break
calculator()


