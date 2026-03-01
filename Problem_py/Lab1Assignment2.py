# Construct a program to store the following details of a Vendor of a Shop. 
# a) Name of vendor 
# b) Year of association 
# c) Contact number 
# d) eMail ID 
# Read the details of monthly purchases from Vendor and generate a Annual Purchase/Billing report. 
name=input("enter name:")
year=int(input("enter year of association:"))
contactNo=int(input("enter contact no."))
email=input("enter mail")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

monthly_purchases = {} 
total = 0

for month in months:
     amount = float(input(f"Enter purchase amount for {month}: "))
     monthly_purchases[month] = amount 
     total += amount

print("\nAnnual Bill")
print("Vendor Name :", name)
print("Year of Association:", year)
print("Contact Number :", contactNo) 
print("Email ID :", email)

print("Annual Purchase:", total)

