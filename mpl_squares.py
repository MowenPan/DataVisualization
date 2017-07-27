import matplotlib.pyplot as plt

squares = [i**2 for i in range(1, 6)]
plt.plot(squares, linewidth=5)

plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
