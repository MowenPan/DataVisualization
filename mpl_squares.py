import matplotlib.pyplot as plt

input_values = [i for i in range(1, 6)]
squares = [i**2 for i in range(1, 6)]
plt.plot(input_values, squares, linewidth=5)

# 设置折线图标题,给坐标轴添加标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
