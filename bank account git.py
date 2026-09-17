class account:
    def __init__(self,bal, acc):
        self.bal=bal
        self.acc=acc

    def debit(self,amount):
        self.bal-=amount
        print("this",amount,"is debited")
    def credit(self,amount):
        self.bal+=amount
        print("this",amount,"is added")

    def balance(self):
        return self.bal    

acc1=  account(12000,7000)
acc1.debit(1000)
acc1.credit(500)

print("total balance is :",acc1.balance())
 
  
# 
# 





