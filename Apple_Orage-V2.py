# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def getApple():
    _Apple = int(input("How many apples do you want to buy? : "))
    return _Apple

def getOrange():
    _Orange = int(input("How many oranges do you want to buy? : "))
    return _Orange

def display():
    PriceApple = 20
    PriceOrange = 25
    TotalApple = PriceApple*NumApple
    TotalOrange = PriceOrange*NumOrange
    Totalamount_ = TotalApple + TotalOrange
    print(f"The total amount is {Totalamount_}.")



NumApple = getApple()
NumOrange = getOrange()
display()