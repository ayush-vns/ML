import pandas as pd
def readfromexcel():
    df=pd.read_excel("ABI.xlsx",index_col=0)
    return df
def GetBalance(accno):
    try:
        df=readfromexcel()
        x = df[['balance']]

        return x.loc[accno][0]

    except:
        return None
def ChangeBalance(accno,newbalance):
    try:
        newdata = {'accno': [accno],

               'balance': [newbalance]
               }
        newdata = pd.DataFrame(newdata, index=newdata["accno"])
        print(newdata)
        df=readfromexcel()
        df.update(newdata)

        SaveToExcel(df)
        return True
    except:
        return False    
def CloseAccount(accno):
    try:
        df = readfromexcel()
        df=df.drop(accno)
        print(df)
        SaveToExcel(df)
        return True
    except:
        return False
def NewAccount(accno,name,balance):
    # try:
        newdata = {
                   "accno":accno,
                   'balance': balance,
                   "name": name
                   }
        df = readfromexcel()
        print(newdata)
        df.loc[accno]=newdata
        print('df',df)
        SaveToExcel(df)
        return True
    # except:
    #     return False
def depositbalance(accno,newdeposit):
    currentbalance = GetBalance(accno)
    balance= currentbalance+deposit
    ChangeBalance(accno,balance)

def withdrawalbalance(accno,newdeposit):
    currentbalance = GetBalance(accno)
    balance= currentbalance-withdrawal
    ChangeBalance(accno,balance)


def delete(accno):
    df=readfromexcel()
    df =df.drop(accno)
    print(df)
    SaveToExcel(df)
    return True

def showall(accno):
    df = readfromexcel()
    x=df[['name']]
    hello=x.loc[accno][0]
    balance=GetBalance(accno)
    return accno,hello,balance
    
    

    
    return True

def SaveToExcel(df):
    try:
        df.to_excel("ABI.xlsx")
#NewAccount(4,"Popat",500)
#CloseAccount(4)
#balance=GetBalance(4)
#print(balance)
# ChangeBalance(4,600)

# x=GetBalance(3)
# print(x)
# x=NewAccount(4,"Champak",300)
# print(x)
# print(readfromexcel())
    except:
        return False
while True:
    print("0-Exit,1-add,2-search,3-delete,4-all,5-deposit,6-withdrawal")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        print("new")
        name = input("Enter your name  ")
        accno =int(input(" Enter your account_no "))
        newdeposit = int(input("deposit money "))
        NewAccount(accno,name,newdeposit)
        continue
    if option == 2:
        print("Search")
        accno = int(input("Enter account_no: "))
        details=showall(accno)
        print(details)
        continue
    if option == 5:
        print("deposit")
        accno = int(input("Enter account_no "))
        # if SaveToExcel.get(accno) is None:
        #     print("Invalid Account No")
        #     continue
        deposit = int(input("Enter deposit money "))
        currentbalance = GetBalance(accno)
        newbalance = currentbalance + deposit
        ChangeBalance(accno,newbalance)
        continue
    if option == 6:
        print("withdrawal")
        accno = int(input("Enter account_no "))
        # if SaveToExcel.get(accno) is None:
        #     print("Invalid Account No")
        #     continue
        withdrawal = int(input("Enter withdrawal money "))
        currentbalance = GetBalance(accno)
        newbalance = currentbalance - withdrawal
        ChangeBalance(accno,newbalance)
        continue 
    if option == 3:
        print("delete")
        accno = int(input("Enter account_no "))
        delete(accno)
        continue 
    
    