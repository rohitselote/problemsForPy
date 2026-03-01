# Construct a program to store the information of an employee such as name, employee ID, department and generate 
# the salary as per the following conditions: 
# (i) DA is 92% of Basic Salary 
# (ii) HRA is 58% of Basic Salary 
# (iii) TA is 30% of Basic Salary 
# (iv) LIC is deducted: Rs. 500 every month. 

name=input("Enter employeee name:")
empid=(input("Enter employeee Department:"))
basicSalary=float(input("Enter Basic salary:"))
DA=float((92/100)*basicSalary)
HRA=float((58/100)*basicSalary)
TA=float((30/100)*basicSalary)
Salary=float(basicSalary+DA+HRA+TA-500)
print(f"Salary is {Salary:.2f}")
