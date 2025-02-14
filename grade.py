n1 = float(input("enter the first marks"))
n2 = float(input("enter the second marks"))
n3 = float(input("enter the third marks"))
n4 = float(input("enter the fourth marks"))

total = n1 + n2 + n3 + n4
agg = total / 4

print(" the total is :", total)
print(" the agg is :", agg)

if agg > 75:
    print("you have passed with first class with distinction")
elif agg > 60 and agg <= 75:
    print("you have passed with first class ")
elif agg > 45 and agg <= 60:
    print("you have passed with second class ")
elif agg > 35 and agg <= 45:
    print("you have passed with third class ")
else:
    print("you have failed")
