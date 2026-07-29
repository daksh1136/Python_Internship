class bank_acount():
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def diposted(self,amount):
        self.balance+=amount
    def ingo(self):
        return f" {self.holder},{self.balance}"

s1=bank_acount("daksj",50000)

# print(holder)
s1.diposted(50000)
print(s1.ingo())
    





