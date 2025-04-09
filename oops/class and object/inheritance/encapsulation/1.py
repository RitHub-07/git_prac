# private and protected access modifier 
class Bank_Account: 
# Public
    account_holder_name="ritul"
# Protected
    _account_number="123456"
# Private
    __account_balance =10000000000

    def first_scheme(self):
        print("This Is beneficial Scheme")
    def second_scheme(self):
        print("This Is Worst Scheme")
class pan_detail(Bank_Account):
    pan_no="ABC1234567"
    print("Here is the information regarding PAN details")

obj=pan_detail()
print(obj.account_holder_name)

print(obj._account_number)