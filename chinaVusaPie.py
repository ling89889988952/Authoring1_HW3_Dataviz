import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
usa = []
china = []

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

total = len(china) + len(usa)
china_percentage = int(len(china) / total * 100)
usa_percentage = int(len(usa) / total * 100)


labels = "Usa", "China"
sizes = [usa_percentage, china_percentage]
colors = ['lightblue', 'pink']
explode = (0.1, 0.1)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal won by usa and china(Pie)")
plt.xlabel("")
plt.show()