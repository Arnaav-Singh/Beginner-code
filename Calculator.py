  
def add(a,b):
    result=a+b
    print(result)
def sub(a,b):
    result=a-b
    print(result)
def multiplication(a,b):
    result=a*b
    print(result)
def divide(a,b):
    result=a/b
    print(result)

a=int(input("Enter the first number : "))
b=int(input("Enter the second number: "))
operator=input("Enter the operator:   ")

if operator=="+":
    add(a,b)
elif operator=="-":
    sub(a,b)
elif operator=="*":
    multiplication(a,b)
elif operator=="/":
    divide(a,b) 
else:
    print("Invalid Input")