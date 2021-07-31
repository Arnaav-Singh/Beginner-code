# Python Program to Calculate Total Marks Percentage and Grade of a Student

print("Enter the marks of five subjects::")

subject_1 = float (input ("Enter the marks of English: "))
subject_2 = float (input ("Enter the marks of Hindi:  "))
subject_3 = float (input ("Enter the marks of Math:  "))
subject_4 = float (input ("Enter the marks of SST:    "))
subject_5 = float (input ("Enter the marks of Science:  "))

# calculate the Total  and Percentage
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total / 500.0) * 100

if  percentage >= 90:
    Division = 'First'
elif percentage >= 80 and percentage < 90:
    Division = 'Second'
elif percentage >= 70 and percentage< 80:
    Division = 'Third'
elif percentage>= 60 and percentage < 70:
    Division = 'Fourth'
else:
    Division = 'Fifth'
# produce the final output
print ("The Total marks is:   ", total,)
print ("The Percentage is:    ", percentage, "%")
print ("The Division is:         ",Division )