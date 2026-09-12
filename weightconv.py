weight = float(input("Enter your weight :"))
unit = input("Enter in kilograms or pounds(k or l): ")
if unit == "k":
    weight = weight * 2.205
elif unit == "l":
    weight = weight / 2.205
print(f"The weight is {round(weight,2)}")