# importing csv module 
import csv
import math
import matplotlib.pyplot as plt
import numpy as np


# csv file name 
filename = "pedestrian/pedestrian1.csv"

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

        # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows 
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row 
    for col in row:
        print("%10s" % col),
    print('\n')
attributes = []
# Convert list rows elements to integers
for i in range(len(rows)):
    # print(i)
    rows_int = list(map(float, rows[i]))
    attributes.append(rows_int)
    # difference = math.sqrt((rows_int[i][4] - rows_int[i+1][4])**2 + (rows_int[i][5] - rows_int[i+1][5])**2)
    # print(rows_int[1])
# print(attributes[1][5])
points = []
# distlist1 = []
for j in range(len(rows)):
    # print(attributes[j-1][5], attributes[j][5])
    points.append((attributes[j][5],attributes[j][6]))
# print(points)
for k in range(1, 26):
    plt.plot([points[k - 1][0], points[k][0]], [points[k - 1][1], points[k][1]], 'b-')
for p in range(27,51):
    plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# print(points)
# plt.plot([points[0][0],points[1][0]],[points[0][1], points[1][1]])
# plt.plot([points[1][0], points[2][0]], [points[1][1],points[2][1]])

plt.grid()
plt.show()
    # print(points[0])
#     plt.plot([points[j][0][0],points[j][0]],[points[0][1],points[1][1]])
    # diffx = attributes[j - 1][4] - attributes[j][4]
    # diffy = attributes[j - 1][5] - attributes[j][5]
    # distance = math.sqrt(diffx**2 + diffy**2)
    # distlist.append(distance)
# plt.show()
#
# for k in range(len(rows)):
#     for l in range(len(rows)):
#         diffx1 = attributes[l][4] - attributes[k][4]
#         diffy1 = attributes[l][5] - attributes[k][5]
#         distance_1 = math.sqrt(diffx1**2 + diffy1**2)
#         distlist1.append(distance_1)

# print(distlist1)
# matrix = np.array_split(distlist1, 27)
# matrix = np.reshape(distlist1,(26,26))
# np.savetxt("matrix.csv", matrix, delimiter=";")


