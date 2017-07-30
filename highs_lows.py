import csv

# 从文件中获取最高气温
filename = 'figure/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)
    print(header_now)

    highs = []
    for row in reader:
        highs.append(int(row[1]))
    print(highs)

for index, column_header in enumerate(header_now):
    print(index, column_header)


