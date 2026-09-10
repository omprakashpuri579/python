#typecasting its the process where a variable is converting from one data type to another 
#       str(), int(), float(), bool()

name = ""
age = 17
gpa = 3.07
is_student = True

gpa = int(gpa)   # example gpa ma float ko sato int so gpa 3.07 ko place ma 3 aayo
print(gpa)

age = str(age)   # age ma float use garda 17.0 and str use garda 17 same as int but str ma add garda number jodinxa
age += "1"

print(age)

name = bool(name)    #name blank then i will say false
print(name)
