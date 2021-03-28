class User:
    def __init__(self, username, account_balance):           # now our method has 2 parameters!
        self.username = username			                 # and we use the values passed in to set the name attribute                
        self.account_balance = 0		                     # the account balance is set to $0, so no need for a third parameter

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self.account_balance


    def make_withdrawal(self, amount):
        self.account_balance -=amount
        return self.account_balance

    def display_user_balance(self):
        print("user name: ",self.username,', user balance :' ,self.account_balance)


# Create 3 instances of the User class
x=User('mike jordan',0)
y=User('rafae nadal ',0)
z=User('ronaldo nazario',0)


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
x.make_deposit(200)
x.make_deposit(200)
x.make_deposit(200)
# print the balence before withdrawalis 
x.display_user_balance()
#print the balence after withdrawalis 
x.make_withdrawal(100)
x.display_user_balance()


# Have the second user make 2 deposits and 2 withdrawals and then display their balance
y.make_deposit(500)
y.make_deposit(1000)
#print the balence before withdrawalis 
y.display_user_balance()
#print the balence after withdrawalis 
y.make_withdrawal(140)
y.make_withdrawal(700)
y.display_user_balance()


#Have the third user make 1 deposits and 3 withdrawals and then display their balance
z.make_deposit(1000)
#print the balence before withdrawalis 
z.display_user_balance()
#print the balence after withdrawalis 
z.make_withdrawal(40)
z.make_withdrawal(65)
z.make_withdrawal(80)
z.display_user_balance()




