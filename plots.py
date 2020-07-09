import numpy as np
import xlrd
import matplotlib.pyplot as plt
path = "data/flowrate=50_min/matrix_50peds.xlsx"

wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0,1))
# sum1 = 0
# sum2 = 0

""" Calculates the sum of number of the row in a matrix """
# sumlist = []
# for i in range(0,70):
#     sum = 0
#     for j in range(i, 70):
#     # sum.append(sheet.cell_value(0,i))
#         sum += sheet.cell_value(i,j)
#         # sum2 += sheet.cell_value(1,i+1)
#     sumlist.append(sum)
#
# print(sumlist)
###########################################################






#### Plotting #####
# plt.xlabel('distance between the pedestrians')
# plt.ylabel('number of pedestrians')
# plt.title("")
# plt.show()
