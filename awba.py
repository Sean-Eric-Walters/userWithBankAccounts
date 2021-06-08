class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance < 0:
            print('insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print('Balance:', self.balance)
        return self 

    def yeild_interest(self):
        if self.balance>0:
            self.int_rate = 0.01
            self.balance = self.balance * (1+self.int_rate)
        return self

        
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account_balance.make_deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account_balance.make_withdrawal(amount)
        return self
    
    def dispaly_user_balance(self):
        print(self.name, self.isplay_account_info)

    def tranfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Batou = user('Batou', 'Batou@section9.gov' )
Togusa = user('Togusa', 'Togusa@section9.gov')
Major = user('Major', 'Major@section9.gov')

print('==balance==')

Batou.make_deposit(4999).make_deposit(4999).make_deposit(1698.58).make_withdrawal(2800).dispaly_user_balance()

Togusa.make_deposit(1589.31).make_withdrawal(243.19).make_deposit(1589.31).make_withdrawal(2000).dispaly_user_balance()

Major.make_deposit(9000).make_withdrawal(1100).make_withdrawal(89.13).make_withdrawal(983.21).dispaly_user_balance()

print('==balance==')

Batou.tranfer_money(Major,3000)
Batou.dispaly_user_balance()
Major.dispaly_user_balance()