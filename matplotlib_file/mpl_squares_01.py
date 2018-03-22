import matplotlib.pyplot as plt

squares = [1,4,6,7,9]
plt.plot(squares,linewidth = 5)

plt.title("square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

plt.tick_params(axis='both',labelsize = 14)

plt.show()