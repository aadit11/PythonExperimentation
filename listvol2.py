n = int(input("Enter number of elements"))

print()
list = []

for x in range(0, n):
    z = int(input("Enter the number : "))
    list.append(z)

print("The list is : ", list)

for i in range(0, n):
    
    
    
    if list[i] % 2 == 0:
        print("The even list is ", list[i])

    elif list[i] != 0:
        print("The odd list is : ", list[i])
