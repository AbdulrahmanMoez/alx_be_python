num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))
opteration = input ("Choose Operator: (+) (*) (-) (/) (%):  ")
try:
    match opteration:
        case "+":
            print("The result is: ", num1 + num2)
        case  "*":
            print("The result is: ",num1 * num2)
        case  "-":
            print("The result is: ",num1 - num2)
        case "/":
            print("The result is: ",num1 / num2)
        case _:
            print("Error: Wrong Operation")
except ZeroDivisionError:
    print("Error: Division by Zero is not allowed")
