import matplotlib.pyplot as plt

x_value = [i for i in range(1, 5001)]
y_value = [i**3 for i in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Numbers", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 125000000000])

plt.show()
