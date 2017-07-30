import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温和日期
filename = 'figure/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)
    print(header_now)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
    print(highs)

for index, column_header in enumerate(header_now):
    print(index, column_header)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
# 设置图形格式
plt.title("Daily high Temperature,July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


