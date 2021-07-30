# Python Programarks to Calculate Average and Percentage marksarks
# Taking Input for the total subject marks
Name= input("Enter Age: ")
print("Enter marksarks Obtained in 5 Subjects: ")
marksOne= int(input("Enter Englsih : "))
marksTwo= int(input("Enter Math:  "))
marksThree= int(input("Enter Hindi: " ))
marksFour= int(input("Enter Science: "))
marksFive= int(input("Enter SST: "))
#Processing the values from the user
sumarks = marksOne+marksTwo+marksThree+marksFour+marksFive
percentage = (sumarks/500)*100
#Printing values 
print(end="sum of Marks = ")
print(sumarks)
print(end="Percentage marks = ")
print(percentage)
