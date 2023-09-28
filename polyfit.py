import numpy
from numpy.polynomial import polynomial as poly
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import random
import warnings
warnings.simplefilter('ignore', numpy.polynomial.polyutils.RankWarning)

x = [45, 39, 90, 0, 87]  # Input X
y = [4*x*x - 5*x - 12 for x in x]  # Input Y
# y=[1,0,1,0,1]

'''


130.45,135.00,132.60,131.00,129.60,132.80,129.50,131.40,129.50,132.40


'''
r = 2
model = poly.polyfit(x, y, deg=r)  # Generate the model
plt.scatter(x, y)
# x=list(range(-5,10))
predicty = poly.polyval(x, model)
correlation = round(r2_score(y, predicty), 3)
print("Correlation", correlation * 100, "%")
predictx = list(range(-5, 10))
predicty = poly.polyval(predictx, model)
print("Input ", x, y)
print("Predict ", predictx, predicty)

plt.plot(x, poly.polyval(x, model), "red", label="Degree " + str(r))
plt.legend()
plt.show()
# Get the model output formatted as a equation. Model is an nparray, poly1d requires the array of coefficients in reverse order. Hence th flip.
equation = str(numpy.poly1d(numpy.flip(model)))
print("The equation is Y=\n ", equation)
predictx = 6
predicty = poly.polyval(predictx, model)
print(predictx, predicty)

predictx = -0
predicty = poly.polyval(predictx, model)
print(predictx, predicty)
