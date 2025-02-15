sal = float(input("Enter your salary"))

if sal <= 0:
    print("Invalid salary")


hra = 0
ta = 0
tax = 0
totsal = 0


hra = sal * 0.1
ta = sal * 0.05
tax = sal * 0.02

totsal = (sal + hra + ta) - tax

print("The total salary is ", totsal)
