# In a steel plant, the quality of steel is graded according to the following conditions: 
# (i) Hardness must be greater than 50 
# (ii) Carbon content must be less than 0.7 
# (iii) Tensile strength must be greater than 5600 
# The grades are as follows: 
# Grade is 10 if all three conditions are met 
# Grade is 9 if conditions (i) and (ii) are met 
# Grade is 8 if conditions (ii) and (iii) are met 
# Grade is 7 if conditions (i) and (iii) are met 
# Grade is 6 if only one condition is met 
# Grade is 5 if none of the conditions are met 
# Construct a program, which will require the user to give values of hardness, carbon content and tensile strength of 
# the steel under consideration and output the grade of the steel.

h=float(input("Enter Hardness"))
c=float(input("Enter Carbon content"))
t=float(input("Enter Tensile strength"))
if h>50 and c<0.7 and t>5600:
    print("Grade 10")
elif h>50 and c<0.7:
    print("Grade 9")
elif c<0.7 and t>5600:
    print("Grade 8")
elif h>50  and t>5600:
    print("Grade 7")
elif h>50 or c<0.7 or t>5600:
    print("Grade 6")
else:
    print("Grade 5")
