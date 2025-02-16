ch = input("Enter any character or number:")
if ch >= "a" and ch <= "z":
    print(ch, "is a lowercase alphabet")
elif ch >= "A" and ch <= "Z":
    print(ch, "is a uppercase alphabet")
elif ch >= "0" and ch <= "9":
    print(ch, "is a digit")
else:
    print(ch, "is not an alphabet nor an digit")
