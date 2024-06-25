import pandas as pd

def readfromcsv():
    df = pd.read_csv("testing.csv")
    return df

def showall():
    df = readfromcsv()
    print(df["rollno"])
    plot(df["rollno"])
    return True

def plot(y):
    import matplotlib.pyplot as plt

 
    plt.plot(y)
    plt.show()

while True:
    print("0 - Exit, 1 - Search")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        details = showall()
        print(details)
   
