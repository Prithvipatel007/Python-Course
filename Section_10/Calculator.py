from common import logo

def add (n1, n2):
    """
    Addition of two numbers
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Subtract two numbers
    """
    return n1 - n2
    
def multiply(n1, n2):
    """
    Multiply two numbers
    """
    return n1 * n2

def divide(n1, n2):
    """
    Divide two numbers
    """
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's your first number? : "))

    for symbol in operation:
        print(symbol)

    should_continue = True

    while should_continue == True:
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's your second number? : "))

        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()