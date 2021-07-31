#Inputing Age
age = int(input("Enter Age : "))

# condition to check if the person is an adult or a teenager or a kid  
if age>=18:
        status="Not a teenager. You are an adult"
elif age>=13:
         status="Teenager"
elif age<=12:
         status="You are a kid"
print("You are ",status,)# Printing the result after inputing the age of the kid