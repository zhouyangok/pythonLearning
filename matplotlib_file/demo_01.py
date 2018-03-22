"""
数字的三次方被称为其立方。
请绘制一个图形， 显示前5个整数的立方值，
再绘制一个图形， 显示前5000个整数的立方值。
"""

import matplotlib.pyplot as plt
'''
x_values = [1,3,4,5,6]
y_values = [x**3 for x in x_values]
'''
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=1)

plt.show()