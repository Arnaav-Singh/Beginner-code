#Inputing Age
age = int(input("Enter Age : "))

# condition to check voting eligibility
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"
#Printing age
print("You are ",status," for Vote.")
