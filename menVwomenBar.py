import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
men = []
women = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        else:
            if row[5] == "Men":
                men.append(row[5])
            elif row[5] == "Women":
                women.append(row[5])

print('total medals for men:', len(men))
print('total medals for women:', len(women))

print('processed', line_count, 'row of data')

name_list = ['men', 'women']
num_list = [len(men),len(women)]
plt.bar(range(len(num_list)), num_list, tick_label = name_list, color='rgb')
plt.title("total medals won by men and women")
plt.show()
