print("Welcome to Chase bank.")
print("Have a nice day!")

# option = ""
# balance = 1000
# def bank(balance, option, deposit_amt):
#     result = balance + deposit_amt
#     if(option == "withdraw"):
#         print("withdraw: ", balance) 
#     elif(option == "deposit"):
#         print("depost: ", result)
# # bank(balance, option="withdraw")
# bank(balance, option="deposit", deposit_amt=2000)

balance = 150000
def bank_balance():
    print(f"Your current balance is {balance}") 
    what_it_do = input("What would you like to do: ")
    if (what_it_do == "deposit"):
        deposit_in = input("How much would you like to deposit: ") 
        return f"Your current balance is: {balance + int(deposit_in)}"
    elif (what_it_do == "withdraw"):
        withdraw_in = input("How much would you like to withdraw: ")
        return f"Your current balance is: {balance - int(withdraw_in)}"
    elif (what_it_do == "check_balance"):
        return f"Your current balance is: {balance}"
print(bank_balance())