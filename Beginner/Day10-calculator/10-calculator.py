from art import logo

##Calculator operations 
##Add
def add(number1, number2):
    return number1 + number2

##Subtract
def subtract(number1, number2):
    return number1 - number2

##Multiply
def multiply(number1, number2):
    return number1 * number2

##Divide
def divide(number1, number2):
    return number1 / number2

##dictionary in the form of = { '+' : add, ...}
##save literally the function not the string that contains the name of the function  
operations = {
                '+': add, 
                '-': subtract, 
                '*': multiply, 
                '/': divide, 
}

def calculus():
    print(logo)
    first_number = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)

    #flag for the loop
    keep_calculating = True

    while keep_calculating:
        operation_symbol = input("Pick an operation: ").strip()
        second_number = float(input("What's the next number: "))

        operation_choosed = operations[operation_symbol]
        result = operation_choosed(first_number, second_number)

        print(f'{first_number} {operation_symbol} {second_number} = {result}')

        keep = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start again.: ").lower()
        
        #breaking the loop with the flag
        if keep == 'y':
            first_number = result
        else:    
            keep_calculating = False
            #recursion
            calculus()


calculus()





