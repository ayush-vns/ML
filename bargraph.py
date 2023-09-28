import matplotlib.pyplot as plt
import numpy as np 
categories = ['Apples', 'Oranges', 'Bananas', 'Grapes','aman']
v1 = [1, 2, 3,4,5]
v2 = [7, 9, 11,13,15]
# plt.bar(categories, v1,v2)
bar_width = 0.35
# plt.bar(categories, v1, color='orange', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width)
# plt.bar(categories, v2, color='blue', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width)
plt.legend(['Sales 1'])
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Number of Sales')
plt.scatter(v1,v2)
plt.show()