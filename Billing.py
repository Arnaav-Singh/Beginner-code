# To enter bill amount and ask the user the payment mode and give the discount based on payment mode. Also display net payable amount
x = int(input('Amount: '))
print(""" Kindly chose the mode of the payment 
Credit Card 
Debit Card 
Net Banking 
None of The above 
""")
y = str(input("Enter mode of payment:  "))
 

if y == "Credit Card":
     print(x*10/100+x)
elif y == "Debit Card":
    print(x*5/100+x)
elif y == "Net Banking":
    print(x*2/100+x)
elif y == "None of the above":
    print("Please click continue")
else:
    print("Invalid input")

