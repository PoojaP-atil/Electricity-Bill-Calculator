unit = int(input("Enter your units : "))
amt = 0
if unit <= 100:
    amt = unit * 5
    print("Your bill amount is ", amt)

elif unit <= 200:
    amt = (100 * 5) + (unit - 100) * 7
    print("Your bill amount is ", amt)

elif unit <= 300:
    amt = (200 * 7) + (unit - 200) * 9
    print("Your bill amount is ", amt)

elif unit > 300:
    amt = (300 * 9) + (unit - 300) * 10
    print("Your bill amount is ", amt)