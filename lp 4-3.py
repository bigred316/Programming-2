eggs = int(input("how many eggs do you want?"))
dozen = eggs // 12
price = 0
if dozen <= 3:
    price = 0.50
elif dozen in range(4,6):
    price = 0.45
elif dozen in range(6,11):
    price = 0.40
elif dozen >= 11:
    price = 0.35
print("your eggs will cost $",price, " per dozen")
print("your total cost is $", eggs * (price/12))
