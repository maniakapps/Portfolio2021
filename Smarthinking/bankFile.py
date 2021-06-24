#sys for fetching command-line arguments
#os for linesep
import sys, os

#for retaining ordering
from collections import OrderedDict

#fetch the command-line arguments and store them
F1 = sys.argv[1]
F2 = sys.argv[2]

#empty dictionary for holding balance data read from F1
balance_dict = OrderedDict()

#iterate through each line in F1 and store in the balance_dict with account number as the key
#handle the case in which the file doesn't or the path is wrong
try:
#open F1 for reading
with open(F1, 'r') as balance_file:
for line in balance_file.readlines():
#split the line by "|", and store data, strip any extra white spaces
account_number, pin_code, balance = line.strip().split("|")
#strip white spaces for each variables
account_number = account_number.strip()
pin_code = pin_code.strip()
balance = float(balance.strip())
#store the values into the dictionary
balance_dict[account_number] = { "pin_code" : pin_code, "balance" : balance }

#open F2 for reading
with open(F2, 'r') as transaction_file:
#go through each line of F2
for line in transaction_file.readlines():
#extract data
command, amount, account_number, pin_code = line.strip().split("|")
#strip each variable string of extra white spaces, and convert into proper types as well
command = command.strip()
amount = float(amount.strip())
account_number = account_number.strip()
pin_code = pin_code.strip()

#handle the case in which the key doesn't exist in the dict
try:
#check if the pin_code matches or not
if pin_code == balance_dict[account_number]["pin_code"]:
#check what the command is
if command.lower() == "add":
#add amount to balance
    balance_dict[account_number]["balance"] += amount
elif command.lower() == "sub":
#compute balance
    new_balance = balance_dict[account_number]["balance"] - amount
#check if balance is negative or not
if new_balance >= 0:
#if not, update
    balance_dict[account_number]["balance"] -= amount
except KeyError:
    print("Oops!! Account number doesn't exist in F1")

#open F1 for writing updated balances
with open(F1, 'w') as balance_file:
#go through each item in balance_dict
for key in balance_dict:
#construct the line to write to F1
line = key + "|" + balance_dict[key]["pin_code"] + "|" + str(balance_dict[key]["balance"]) + os.linesep
balance_file.write(line)

except IOError:
print("Either a file doesn't exist or a path is wrong!!")
