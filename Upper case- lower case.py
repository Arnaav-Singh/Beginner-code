# To enter any character and print it's upper case and lower case
x = input("Enter the symbol to be checked: ")
if x >= 'A' and x <= 'Z':
    print(x ," is an Uppercase character")
elif x >= 'a' and x <= 'z':
    print(x ,  "is an lower case character")
else:
    ("Invalid Input")

