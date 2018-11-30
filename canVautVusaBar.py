import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
can = []
aut = []
usa = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        else:
            if row[4] == "CAN":
                can.append(row[4])
            elif row[4] == "AUT":
                aut.append(row[4])
            elif row[4] == "USA":
                usa.append(row[4])

print('total medals for can:', len(can))
print('total medals for aut:', len(aut))
print('total medals for usa:', len(usa))

print('processed', line_count, 'row of data')

name_list = ['can', 'aut', 'usa']
num_list = [len(can),len(aut),len(usa)]
plt.bar(range(len(num_list)), num_list, tick_label = name_list, color='rgb')
plt.title("Medal won by can and aut and usa")
plt.show()