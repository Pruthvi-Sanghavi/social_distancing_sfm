# importing csv module 
import csv
import math
import matplotlib.pyplot as plt
import numpy as np


# csv file name 
filename = "matrix.csv"

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
print(attributes[1])

points = []
distances = []
for j in range(len(rows)):
    points.append((attributes[j][1],attributes[j][2]))
    for i in range(len(rows)):
        distance = attributes[j][1]
    # distances.append(())
print(distance)
print(points)
# for k in range(1, 51):
#     line1 = plt.plot([points[k - 1][0], points[k][0]], [points[k - 1][1], points[k][1]], 'b-')
#
# for b in range(52,101):
#     plt.plot([points[b - 1][0], points[b][0]], [points[b - 1][1], points[b][1]], 'r-')
# for c in range(103,128):
#     plt.plot([points[c - 1][0], points[c][0]], [points[c - 1][1], points[c][1]], 'k-')
# for d in range(129,154):
#     plt.plot([points[d - 1][0], points[d][0]], [points[d - 1][1], points[d][1]], 'y-')
# for e in range(155,180):
#     plt.plot([points[e - 1][0], points[e][0]], [points[e - 1][1], points[e][1]], 'm-')
# for f in range(181,206):
#     plt.plot([points[f - 1][0], points[f][0]], [points[f - 1][1], points[f][1]], 'c-')
# for g in range(183,208):
#     plt.plot([points[g - 1][0], points[g][0]], [points[g - 1][1], points[g][1]], 'r-')
# for h in range(209,234):
#     plt.plot([points[h - 1][0], points[h][0]], [points[h - 1][1], points[h][1]], 'r-')
# for l in range(235,260):
#     plt.plot([points[l - 1][0], points[l][0]], [points[l - 1][1], points[l][1]], 'r-')
# for m in range(261,286):
#     plt.plot([points[m - 1][0], points[m][0]], [points[m - 1][1], points[m][1]], 'r-')
# for n in range(287,309):
#     plt.plot([points[n - 1][0], points[n][0]], [points[n - 1][1], points[n][1]], 'r-')
# for p in range(310,326):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for o in range(327,342):
#     plt.plot([points[o - 1][0], points[o][0]], [points[o - 1][1], points[o][1]], 'r-')
# for q in range(343,357):
#     plt.plot([points[q - 1][0], points[q][0]], [points[q - 1][1], points[q][1]], 'r-')
# for r in range(358,372):
#     plt.plot([points[r - 1][0], points[r][0]], [points[r - 1][1], points[r][1]], 'r-')
# for s in range(373,386):
#     plt.plot([points[s - 1][0], points[s][0]], [points[s - 1][1], points[s][1]], 'r-')
# for k in range(387, 400):
#     plt.plot([points[k - 1][0], points[k][0]], [points[k - 1][1], points[k][1]], 'b-')
# for p in range(401,412):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(413,423):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(424,434):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(435,444):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(445,453):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(454,462):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(463,470):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(471,478):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(479,484):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(485,490):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(491,496):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(497,501):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(502,505):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(506,509):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(510,513):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(514,517):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for k in range(518,521):
#     plt.plot([points[k - 1][0], points[k][0]], [points[k - 1][1], points[k][1]], 'b-')
# for p in range(522,524):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(525,527):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(528,531):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(531,534):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(534,536):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(536,538):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(538,540):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(540,542):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(542,544):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(544,546):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(546,548):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(548,550):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(550,552):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(552,554):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(554,555):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(555,556):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(556,557):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(557,558):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# for p in range(558,559):
#     plt.plot([points[p - 1][0], points[p][0]], [points[p - 1][1], points[p][1]], 'r-')
# print(points)
# plt.plot([points[0][0],points[1][0]],[points[0][1], points[1][1]])
# plt.plot([points[1][0], points[2][0]], [points[1][1],points[2][1]])
plt.xlabel('x coordinate of a pedestrian in meters')
plt.ylabel('y coordinate of a pedestrian in meters')
plt.title("Pedestrian coordinates")
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


