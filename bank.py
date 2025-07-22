def deposite(Accounts,amt,ch):
    Accounts[ch]+=amt
    print(f"{amt} successfully deposited")

def withdraw(Accounts,am,ch):
    if Accounts[ch]>=amt:
        Accounts[ch]-=am
        print(f"{am} successfully withdrawn")
    else:
        print("insufficient balance")
def transfer(Accounts,n,x):
    to_acc=int(input("enter4 the acc number to transfer to:"))
    if to_acc not in Accounts:
        print("Target account does not exist")
        return
    if Accounts[from_acc]>=amt:
        Accounts[from_acc]-=amt 
        Accounts[to_acc]+=amt     



def menu(Accounts,ch):
    while(True):
        print("welcome {}".format(ch))
        print("1.check balance")
        print("2.deposite")
        print("2.withdraw")
        print("4.transfer")
        print("5.logout")
        d=int(input("enter ur choice:"))
        if(d==1):
            print("balance is",Accounts[ch])
        elif(d==2):
            amt=int(input("enter the amount to deposite"))
            deposite(Accounts,amt,ch)
        elif(d==3):
            am=int(int("enter amount to withdraw"))
            withdraw(Accounts,am,ch)
        elif(d==4):
            n=int(input("enter the account number:"))
            x=int(input("enter the amount to transfer:"))
            transfer(Accounts,n,x)
        else:
            exit(0)

Accounts={101:1000,102:2000,103:3000}
while True:
    print("-----BANK MANAGEMENT SYSTEM-----")
    ch=int(input("enter account number(0 to exit)"))
    if (ch in Accounts):
        menu(Accounts,ch)
    elif(ch==0):
        print("Exiting the system")
        break
    else:
        print("Invalid account number")