import matplotlib.pyplot as plt


x_values = [1,2,3,4,5,6,7,8,9,12]
y_values = [1,4,1,3,5,6,7,8,9,12]
#plt.scatter(2,4,s=200)
plt.scatter(x_values,y_values,s=100)
plt.title("squares numbers",fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()