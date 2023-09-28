from sklearn import tree
import matplotlib.pyplot as plt


def divisions(n):
    if n == 2:
        return "fail"
    return "pass"


def classifications(n):
    if n < 40:
        return 2
    return 1


def divisions(n):
    # Convert numeric division code to text
    if n == 4:
        return "fail"
    if n == 3:
        return "3rd"
    if n == 2:
        return "2nd"
    return "1st"


def classifications(n):
    # Less than 40 is fail and the numeric code is 4.
    # >=40 and less than 50 = 3rd division
    # >=50 and less than 60 = 2nd division
    # >=60 1st division
    if n < 40:
        return 4
    if n < 50:
        return 3
    if n < 60:
        return 2
    return 1


inputmarks = [50, 45, 66, 7, 89, 21, 39, 40, 89]
inputmarks.sort()
   # Classification needs input as a 2d array
# Use one of the following three
# results=[classifications(x) for x in inputmarks]#Calculated
results = [4, 4, 4, 3, 3, 2, 1, 1, 1]  # Input Results
# results= [4, 4, 1, 3, 3, 2, 1, 1,1]# Input Results with error
# results= [4, 4, 1, 1, 1, 1, 1, 1,4]# Input Results with fail pass error
# results= [4, 4, 4, 3, 3, 2, 1, 1,4]# Input Results with labeling error. 89 = both1 and 4
textresults = [divisions(x) for x in results]  # Print results in words
print("Results numeric",results)
print("Results text",textresults)
print("Input marks ",inputmarks)
classifier = tree.DecisionTreeClassifier()
model = classifier.fit(marks, results)
fullmarksrange=[x for x in range(101)]
fullresultrange=[model.predict([[x]])[0] for x in fullmarksrange]
print(fullresultrange)


# plt.plot(marks, results, color='red')
# plt.scatter(marks, results, color='blue', marker='o')
# plt.grid()
# plt.xlabel('Marks')
# plt.ylabel('Division')
# plt.title("Marks - Division")
# plt.legend(["Actual Division", "Actual Division"])
# plt.show()
plt.plot(fullmarksrange,fullresultrange,color='green')
plt.scatter(marks,results,color='brown',marker='o')
plt.grid()
plt.xlabel('Marks')
plt.ylabel('Division')
plt.title("Predicted Marks - Division")
plt.legend(["Predicted Division","Predicted Division"])
plt.show()
for i in range(101):
  value=[[i]]
  result=model.predict(value)
  probability=model.predict_proba(value)
  print("[Marks ",value[0][0], " result is ",divisions(result) , " prob is ", probability[0],"]",end=",")
  if i % 10==0 and i>0:
    print()
