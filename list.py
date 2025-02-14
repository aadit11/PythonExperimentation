n = int(input("Enter number of elements"))

print()
list = []

for x in range(0, n):
    z = int(input("Enter the number : "))
    list.append(z)

print("The list is : ", list)
print("The max number is ", max(list))
print("The min number is ", min(list))
print()

sum = 0
for i in range(0, n):
    sum = sum + list[i]

print("The sum is : ", sum)

avg = sum / n
print("The avg is : ", avg)
