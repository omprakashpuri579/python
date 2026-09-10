from unittest import result
num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

operator = input("Enter the operator (+ - * /):")
def show(result):
    if result == int(result):
        print(int(result))
    else:
        print(result)

if operator == "+":
    addition = num1 + num2
    print(f"The sum is {pow(addition, 2)}")

elif operator == "-":
    subtraction = num1 - num2
    print(f"The subtraction is {pow(subtraction, 2)}")


elif operator == "*":
    multiplication = num1 * num2
    print(f"The multiplication is {pow(multiplication, 2)}")

elif operator == "/":
    division = num1 / num2
    print(f"The division is {pow(division, 2)}")



