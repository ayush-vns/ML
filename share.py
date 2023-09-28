from sklearn import tree
import matplotlib.pyplot as plt


def division (n):
    if n==2:
       return False
    return True

def classifications (n):
    if n< 50:
        return 2
    return 1

def division (n):
    if n<51:
        return 1
    if n>51:
        return 2
    

inputdata=[25,85,96,15,51,50]
inputdata.sort()

data=[[x]for x in inputdata]

result=[2,1,1,2,1,2]

textresult=[division(x) for x in result]

print("result numeric",result)
print("result text",textresult)
print("input data",inputdata)

classifire=tree.DecisionTreeClassifier()
model =classifire.fit(data,result)

plt.plot(data,result,color='red')
plt.scatter(data,result,color='blue',marker='o')
plt.grid(color="green")
plt.xlabel('Marks')
plt.ylabel('division')
plt.title("data-division")
plt.legend(["actual Division","Predicted Division"])
plt.show()