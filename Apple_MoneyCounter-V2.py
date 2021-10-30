# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def getMoney():
    Money = int(input("Enter the amount of money you have: "))
    return Money 

def getApplePrice():
    PriceApple = float(input("Enter how much is the cost of an apple: "))
    return PriceApple

def Display():
    NumberApple = AmountMoney // PriceApple
    Change = AmountMoney - (NumberApple*PriceApple)
    print(f"You can buy {NumberApple} apples and your change is {Change} pesos.")

AmountMoney = getMoney()
PriceApple = getApplePrice()
Display()