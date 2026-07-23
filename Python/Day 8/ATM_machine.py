balance=5000
try:
    amount=int(input("enter the amount to witdhwrawl:"))
    if amount> balance:
        print(f" amount is grater than balance")
    else:
        balance-=amount
        print("withdrawl successful")
        print(f" remaining balance :{balance}")
except ValueError:
    print("check you amount first")
finally:
    print("atm closed")