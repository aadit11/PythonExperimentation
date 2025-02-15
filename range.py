num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))


sum = 0

while num1 <= num2:
    sum = sum + num1
    num1 = num1 + 1


print("the sum of the numbers for the following range is: ", sum)
