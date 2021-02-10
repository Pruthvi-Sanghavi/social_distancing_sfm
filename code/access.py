# importing csv module
import csv
import math
import matplotlib.pyplot as plt
import numpy as np


# csv file name
filename = "data/flowrate=400_min/50peds.att.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)


attributes = []
# Convert list rows elements to integers
for i in range(len(rows)):
    # print(i)
    rows_int = list(map(float, rows[i]))
    attributes.append(rows_int)
    # difference = math.sqrt((rows_int[i][4] - rows_int[i+1][4])**2 + (rows_int[i][5] - rows_int[i+1][5])**2)
    # print(rows_int[1])
# print(attributes[1])
distlist1 = []
for k in range(len(rows)):
    for l in range(len(rows)):
        diffx1 = attributes[l][1] - attributes[k][1]
        diffy1 = attributes[l][2] - attributes[k][2]
        distance_1 = math.sqrt(diffx1**2 + diffy1**2)
        distlist1.append(distance_1)

print(distlist1)
matrix = np.array_split(distlist1, 51)
matrix = np.reshape(distlist1,(50,50))
np.savetxt("data/flowrate=400_min/matrix_50peds.txt", matrix, delimiter="|")
