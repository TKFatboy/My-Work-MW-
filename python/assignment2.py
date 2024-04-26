class BankAccount:
    def __init__(self, account_number, balance=0.0, name="", account_type="Savings"):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute
        self.__name = name  # private attribute
        self.__account_type = account_type  # private attribute

    def deposit(self, amount):
        if self.__validate_amount(amount):
            self.__balance += amount
            print(f"ฝากเงินจำนวน {amount} บาท")
        else:
            print("จำนวนเงินที่ต้องการฝากไม่ถูกต้อง")

    def withdraw(self, amount):
        if self.__validate_amount(amount) and self.__balance >= amount:
            self.__balance -= amount
            print(f"ถอนเงินจำนวน {amount} บาท")
        else:
            print("เงินไม่เพียงพอหรือจำนวนเงินที่ต้องการถอนไม่ถูกต้อง")

    def transfer(self, recipient_account, amount):
        if self.__validate_amount(amount) and self.__balance >= amount:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            print(f"โอนเงินจำนวน {amount} บาท สู่หมายเลขบัญชี {recipient_account.get_account_number()}")
        else:
            print("เงินไม่เพียงพอหรือจำนวนเงินที่ต้องการโอนไม่ถูกต้อง")

    def check(self):
        return self.__account_type

    def calculate_rate(self):
        if self.__account_type == "Savings":
            return 0.03  
        elif self.__account_type == "Checking":
            return 0.01  
        else:
            return 0.0  

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __validate_amount(self, amount):
        return amount > 0


# Example usage
account1 = BankAccount(373260, 1000.0, "TK", "Savings")
account2 = BankAccount(212544, 500.0, "ZT", "Checking")

print("ยอดเงินในบัญชีของบัญชีที่ 1", account1.get_balance(),"บาท")
print("อัตราดอกเบี้ยของบัญชีที่ 1", account1.calculate_rate(),"บาท")
print("ยอดเงินในบัญชีของบัญชีที่ 2", account2.get_balance(),"บาท")
print("อัตราดอกเบี้ยของบัญชีที่ 2", account2.calculate_rate(),"บาท")

account1.deposit(500.0)
account2.withdraw(200.0)

print("ยอดเงินในบัญชีของบัญชีที่ 1", account1.get_balance(),"บาท")
print("ยอดเงินในบัญชีของบัญชีที่ 2", account2.get_balance(),"บาท")

account1.transfer(account2,300.0)

print("ยอดเงินในบัญชีของบัญชีที่ 1", account1.get_balance(),"บาท")
print("ยอดเงินในบัญชีของบัญชีที่ 2", account2.get_balance(),"บาท")
