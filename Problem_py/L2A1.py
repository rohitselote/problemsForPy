# a) Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the 
# current (I) using Ohm’s Law. 
# b) Modify the above program to display the nature of current: 
# If current < 0.5 A, print “Low current” 
# If 0.5 A ≤ current ≤ 2 A, print “Normal current” 
# If current > 2 A, print “High current 
v=float(input("Enter voltage"))
r=float(input("Enter resistance"))
i=float(v/r)
print(i)
if i<0.5:
    print("low current")
elif 0.5<=i<=2 :
    print("Normal current")
else:
    print("high currrent")
