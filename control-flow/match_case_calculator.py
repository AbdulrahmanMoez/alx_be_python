num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))
operation = input ("Choose the operation (+, -, *, /): ")

match operation: 
    case "+":
        result = ( num1 + num2)
    case  "*":
        result = (num1 * num2)
    case  "-":
        result = (num1 - num2)
    case "/":
        if num2 != 0:
            result = (num1 / num2)
        else:
            result = "Cannot divide by zero"
    case _:
        print("Invalid operation")

print(f"The result is {result}")
