import matplotlib.pyplot as plt
import json
import requests
import numpy as np

url=("https://gist.githubusercontent.com/ayush-vns/8368d8c0af84a22dc81bb6e687766725/raw/6ca6bcc2bfaa75d925fc21afeb9196a0db99d509/ml")
response=requests.get(url)
data=response.text
data=json.loads(data)
x=data["x"]
y=data["y"]
plt.plot(x,y)
plt.grid(True)
plt.scatter(x,y)
plt.show()

