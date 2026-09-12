try:
   number = float(input("Enter the number which square you would like to know:"))
   print("Square is:", round(number ** 2, 2))
except ValueError:
    print("Not a valid input, try entering a number")