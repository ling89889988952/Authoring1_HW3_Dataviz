import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
china = []
usa = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        else:
            if row[4] == "CHN":
                china.append(row[4])
            elif row[4] == "USA":
                usa.append(row[4])

print('total medals for china:', len(china))
print('total medals for usa:', len(usa))

print('processed', line_count, 'row of data')

name_list = ['china', 'usa']
num_list = [len(china),len(usa)]
plt.bar(range(len(num_list)), num_list, tick_label = name_list, color='rgb')
plt.title("total medals won by china and usa")
plt.show()