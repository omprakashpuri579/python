operator = input("Enter the operator (+ - * /):")
num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    addition = (num1 + num2)
    print(f"The sum is {round(addition, 2)}")

elif operator == "-":
    subtraction = (num1 - num2)
    print(f"The subtraction is {round(subtraction, 2)}")

elif operator == "*":
    if num2 == 0:
        print("the ans is zero")
    else:
        multiplication = (num1 * num2)
        print(f"The multiplication is {round(multiplication, 2)}")

elif operator == "/":
    if num2 == 0:
        print("its invalid input")
    else:
        division = (num1 / num2)
        print(f"The division is {round(division, 2)}")

else:
    print("Invalid operator")