num = int(input("Enter a number"))
denom = int(input("Enter another number"))
while denom > 0:
    temp = num % denom
    num = denom
    denom = temp
print(num)
