#This is a bank acoung programm
class BankAccount(object):
  balance=0
  
  def __init__(self, name):
    self.name=name
    
  def __repr__(self):
    return 'This Bank Account belongs to %s.\nCurrent balance is: $%.2f' %(self.name, self.balance)
  
  def show_balance(self):
    return 'Current balance is $%.2f' %(self.balance)
  
  def deposit(self, amount):
    if amount<=0:
      print 'Error, invalid amount'
      return
    else:
      self.balance+=amount
      print 'You chose to deposit %.2f dollars.' %(amount)
      self.show_balance()
      
  def withdraw(self, amount):
    if amount<=0:
      print 'Error, invalid amount'
      return
    elif amount>self.balance:
      print 'Error, insufficient funds.'
      return
    else:
      print'You chose to withdraw %.2f dollars' %(amount)
      self.balance-=amount
      self.show_balance()
        
my_account=BankAccount('David')   
print my_account
print my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account