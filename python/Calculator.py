def convert_string_to_int(s):
    if not s.strip():
        raise ValueError("The value must be a valid integer")
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Error: '{s}' cannot be converted into an integer, input numerical values e.g 123")

class Calculation:
    result = 0
    @staticmethod
    def addition(x, y):
        result = x + y
        print(f"{x} + {y} = {result}")
    
    @staticmethod
    def substraction(x, y):
        result = x - y
        print(f"{x} - {y} = {result}")   
        
    @staticmethod
    def division(x, y):
        result = x * y
        print(f"{x} * {y} = {result}")
       
    @staticmethod
    def multiplication(x, y):
        result = x / y
        print(f"{x} / {y} = {result}")
       
first_value = convert_string_to_int(input("Input your first number: "))
second_value = convert_string_to_int(input("Input your second number: "))
operator = input("Input a single operator either (+,_,/,*): ").strip()

match operator:
    case '+':
        Calculation.addition(first_value, second_value)
    case '-':
        Calculation.substraction(first_value, second_value)
    case '*':
        Calculation.multiplication(first_value, second_value)
    case '/':
        Calculation.division(first_value, second_value)
    case _:
        print("Invalid operator! Couldn't complete the calculation")                          
        
        
    
        
