```python
class SBI: 
    accounts = [1111]
    def __init__(self, pin):
        self.__pin = pin
        self.account_no = SBI.generateAccountNo()
        self.amount = 0
        print("🏦 you account has been created ")
        print(" [ account no ] : ", self.account_no)

    def deposit(self, acc_no, pin, amount): 
        isAuth, msg = self.authenticate( acc_no, pin )
        if not isAuth:
            print(msg)
            return
        if self.validateAmount(amount):
            self.amount = self.amount + amount
        else:
            print("⚠️ you have entered invalid amount")
            
    def withdraw(self, acc_no, pin, amount):
        isAuth, msg = self.authenticate( acc_no, pin )
        if not isAuth:
            print(msg)
            return
        if self.validateAmount(amount):
            total = self.amount - amount
            if total < 0:
                print("sufficeint amount is not avaible")
            else:
                self.amount = total
        else:
            print("⚠️ you have entered invalid amount")
            
    def check(self): 
        print(" your balance amount is: ", self.amount)
    
    @staticmethod
    def generateAccountNo():
        latest_acc = SBI.accounts[-1]
        new_acc = latest_acc + 1
        SBI.accounts.append(new_acc)
        return new_acc

    @staticmethod
    def validateAmount(amount):
        if amount <= 0:
            return False
        return True

    def authenticate(self,acc_no, pin):
        if acc_no not in self.accounts:
            return ( False, "account not exists" )
        if self.account_no != acc_no:
            return ( False, "Invalid account no" )
        if pin != self.__pin:
            return ( False, "wrong pin no" )
        return ( True, "success" )

    @classmethod
    def info(cls):
        print(" --- SBI ( state bank of india ) --- ")
    
    @classmethod
    def getTotalAccounts(cls):
        print(" total accounts : ", len(cls.accounts)) 
    
```


```python
arun = SBI(1234)
diya = SBI(3344)
```

    🏦 you account has been created 
     [ account no ] :  1112
    🏦 you account has been created 
     [ account no ] :  1113
    


```python
julie = SBI(1222)
```

    🏦 you account has been created 
     [ account no ] :  1114
    


```python
julie.deposit(1114, 1222, 1000)
```


```python
julie.check()
```

     your balance amount is:  1000
    


```python
julie.deposit(1114, 1222, 500)
```


```python
julie.check()
```

     your balance amount is:  1500
    


```python
julie.withdraw(1114, 1222, 600)

```


```python
julie.check()
```

     your balance amount is:  900
    


```python
SBI.getTotalAccounts()
```

     total accounts :  4
    


```python

```
