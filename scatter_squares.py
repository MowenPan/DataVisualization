import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [i**2 for i in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 添加标题和坐标轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.svg', bbox_inches='tight')
plt.show()
