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

total = len(can) + len(aut) + len(usa)
can_percentage = int(len(can) / total * 100)
aut_percentage = int(len(aut) / total * 100)
usa_percentage = int(len(usa) / total * 100)


labels = "CAN", "AUT", "USA"
sizes = [can_percentage, aut_percentage, usa_percentage]
colors = ['red', 'blue', 'yellow']
explode = (0.1, 0.1, 0.15)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal won by can and aut and usa(Pie)")
plt.xlabel("")
plt.show()


