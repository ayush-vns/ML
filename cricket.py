import sys
 
import requests
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


url="https://gist.githubusercontent.com/ayush-vns/8368d8c0af84a22dc81bb6e687766725/raw/065fc64d3f5f8824b131709c9faccadeb7711c34/ml"
response = requests.get(url)
print(response)
result=["win","losse","losse","losse"]
status = [1,0,0,0]
df=pandas.DataFrame({"RESULT":result,"STATUS":status})
resulttonumber = {'losse': 0, 'win': 1}
numbertoresult = {0: 'losse', 1: 'win'}

df['RESULT'] = df['RESULT'].map(resulttonumber)
print(df['RESULT'])

# df["STATUS"] = df["STATUS"].map(numbertoresult)
# print(df["STATUS"])

features = ['Team1', 'Team2']

X =df[features]
y = df['RESULT']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
tree.plot_tree(dtree, feature_names=features)
sys.stdout.flush()  
Team1=[]
Team2=[]
results=[]
marks={"Team1":[44],"Team2":[45],"MATCHS":[41]}
examplemarks=pandas.DataFrame(marks)
print("Marks",examplemarks)
result=dtree.predict(examplemarks)
df=pandas.DataFrame({"RESULT":result})
df['TEXTRESULT'] = df['RESULT'].map(numbertoresult)
print(df['TEXTRESULT'][0])
Team1.append(marks["PHY"][0])
Team2.append(marks["CHEM"][0])
# maths.append(marks["MATHS"][0])
results.append(df["RESULT"][0])