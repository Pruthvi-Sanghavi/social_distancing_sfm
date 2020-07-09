import numpy as np
import xlrd
import matplotlib.pyplot as plt

""" Path of each data file """
path1 = "data/flowrate=50_min/matrix_50peds.xlsx"
path2 = "data/flowrate=100_min/matrix_50peds.xlsx"
path3 = "data/flowrate=200_min/matrix_50peds.xlsx"
# path4 = "data/flowrate=75_min/matrix_50peds.xlsx"
# path5 = "data/flowrate=80_min/matrix_50peds.xlsx"
# path6 = "data/flowrate=125_min/matrix_50peds.xlsx"
path7 = "data/flowrate=150_min/matrix_50peds.xlsx"
path8 = "data/flowrate=250_min/matrix_50peds.xlsx"
path9 = "data/flowrate=300_min/matrix_50peds.xlsx"
path10 = "data/flowrate=350_min/matrix_50peds.xlsx"
path11 = "data/flowrate=400_min/matrix_50peds.xlsx"



""" Opening the data files """
wb1 = xlrd.open_workbook(path1)
wb2 = xlrd.open_workbook(path2)
wb3 = xlrd.open_workbook(path3)
# wb4 = xlrd.open_workbook(path4)
# wb5 = xlrd.open_workbook(path5)
# wb6 = xlrd.open_workbook(path6)
wb7 = xlrd.open_workbook(path7)
wb8 = xlrd.open_workbook(path8)
wb9 = xlrd.open_workbook(path9)
wb10 = xlrd.open_workbook(path10)
wb11 = xlrd.open_workbook(path11)


""" reading the entries in data files"""
sheet1 = wb1.sheet_by_index(0)
sheet2 = wb2.sheet_by_index(0)
sheet3 = wb3.sheet_by_index(0)
# sheet4 = wb4.sheet_by_index(0)
# sheet5 = wb5.sheet_by_index(0)
# sheet6 = wb5.sheet_by_index(0)
sheet7 = wb7.sheet_by_index(0)
sheet8 = wb8.sheet_by_index(0)
sheet9 = wb9.sheet_by_index(0)
sheet10 = wb10.sheet_by_index(0)
sheet11 = wb11.sheet_by_index(0)

""" Calculating the number of pedestrian at different seperations"""
hRisk1  = []
inRisk1 = []
lRisk1 = []

hRisk2  = []
inRisk2 = []
lRisk2 = []

hRisk3  = []
inRisk3 = []
lRisk3 = []

# hRisk4  = []
# inRisk4 = []
# lRisk4 = []
#
# hRisk5  = []
# inRisk5 = []
# lRisk5 = []
#
# hRisk6  = []
# inRisk6 = []
# lRisk6 = []

hRisk7  = []
inRisk7 = []
lRisk7 = []

hRisk8  = []
inRisk8 = []
lRisk8 = []

hRisk9  = []
inRisk9 = []
lRisk9 = []

hRisk10  = []
inRisk10 = []
lRisk10 = []

hRisk11  = []
inRisk11 = []
lRisk11 = []


for i in range(0, 49):
    for j in range(i,49):
    # print(sheet.cell_value(0, i))
        if 0.0 < sheet1.cell_value(j,i) < 2.0:
            hRisk1.append(sheet1.cell_value(j,i))
            # print(i, j, sheet1.cell_value(j,i))
        if 2.0 < sheet1.cell_value(j,i) < 4.0:
            inRisk1.append(sheet1.cell_value(j,i))
        if 4.0 < sheet1.cell_value(j,i) < 6.0:
            lRisk1.append(sheet1.cell_value(j,i))

for p in range(0, 49):
    for q in range(p,49):
    # print(sheet.cell_value(0, i))
        if 0.0 < sheet2.cell_value(q,p) < 2.0:
            hRisk2.append(sheet2.cell_value(q,p))
            # print(i, j, sheet.cell_value(j,i))
        if 2.0 < sheet2.cell_value(q,p) < 4.0:
            inRisk2.append(sheet2.cell_value(q,p))
        if 4.0 < sheet2.cell_value(q,p) < 6.0:
            lRisk2.append(sheet2.cell_value(q,p))

for x in range(0, 49):
    for y in range(x,49):
    # print(sheet.cell_value(0, i))
        if 0.0 < sheet3.cell_value(y,x) < 2.0:
            hRisk3.append(sheet3.cell_value(y,x))
            # print(i, j, sheet.cell_value(j,i))
        if 2.0 < sheet3.cell_value(y,x) < 4.0:
            inRisk3.append(sheet3.cell_value(y,x))
        if 4.0 < sheet3.cell_value(y,x) < 6.0:
            lRisk3.append(sheet3.cell_value(y,x))

# for a in range(0, 49):
#     for b in range(a,49):
#     # print(sheet.cell_value(0, i))
#         if 0.0 < sheet4.cell_value(b,a) < 2.0:
#             hRisk4.append(sheet4.cell_value(b,a))
#             # print(i, j, sheet.cell_value(j,i))
#         if 2.0 < sheet4.cell_value(b,a) < 4.0:
#             inRisk4.append(sheet4.cell_value(b,a))
#         if 4.0 < sheet4.cell_value(b,a) < 6.0:
#             lRisk4.append(sheet4.cell_value(b,a))
#
#
# for c in range(0, 49):
#     for d in range(c,49):
#     # print(sheet.cell_value(0, i))
#         if 0.0 < sheet5.cell_value(d,c) < 2.0:
#             hRisk5.append(sheet5.cell_value(d,c))
#             # print(i, j, sheet.cell_value(j,i))
#         if 2.0 < sheet5.cell_value(d,c) < 4.0:
#             inRisk5.append(sheet5.cell_value(d,c))
#         if 4.0 < sheet5.cell_value(d,c) < 6.0:
#             lRisk5.append(sheet5.cell_value(d,c))
#
# for e in range(0, 49):
#     for f in range(e,49):
#     # print(sheet.cell_value(0, i))
#         if 0.0 < sheet6.cell_value(f,e) < 2.0:
#             hRisk6.append(sheet6.cell_value(f,e))
#             # print(i, j, sheet.cell_value(j,i))
#         if 2.0 < sheet6.cell_value(f,e) < 4.0:
#             inRisk6.append(sheet6.cell_value(f,e))
#         if 4.0 < sheet6.cell_value(f,e) < 6.0:
#             lRisk6.append(sheet6.cell_value(f,e))

for g in range(0, 49):
    for h in range(g,49):
    # print(sheet.cell_value(0, i))
        if 0.0 < sheet7.cell_value(h,g) < 2.0:
            hRisk7.append(sheet7.cell_value(h,g))
            # print(i, j, sheet.cell_value(j,i))
        if 2.0 < sheet7.cell_value(h,g) < 4.0:
            inRisk7.append(sheet7.cell_value(h,g))
        if 4.0 < sheet7.cell_value(h,g) < 6.0:
            lRisk7.append(sheet7.cell_value(h,g))

for k in range(0, 49):
    for l in range(k,49):
    # print(sheet.cell_value(0, k))
        if 0.0 < sheet8.cell_value(l,k) < 2.0:
            hRisk8.append(sheet8.cell_value(l,k))
            # print(k, l, sheet8.cell_value(l,k))
        if 2.0 < sheet8.cell_value(l,k) < 4.0:
            inRisk8.append(sheet8.cell_value(l,k))
        if 4.0 < sheet8.cell_value(l,k) < 6.0:
            lRisk8.append(sheet8.cell_value(l,k))

for m in range(0, 49):
    for n in range(m,49):
    # print(sheet.cell_value(0, m))
        if 0.0 < sheet9.cell_value(n,m) < 2.0:
            hRisk9.append(sheet9.cell_value(n,m))
            # print(m, n, sheet9.cell_value(n,m))
        if 2.0 < sheet9.cell_value(n,m) < 4.0:
            inRisk9.append(sheet9.cell_value(n,m))
        if 4.0 < sheet9.cell_value(n,m) < 6.0:
            lRisk9.append(sheet9.cell_value(n,m))

for r in range(0, 49):
    for s in range(r,49):
    # print(sheet.cell_value(0, r))
        if 0.0 < sheet10.cell_value(s,r) < 2.0:
            hRisk10.append(sheet10.cell_value(s,r))
            # print(r, s, sheet10.cell_value(s,r))
        if 2.0 < sheet10.cell_value(s,r) < 4.0:
            inRisk10.append(sheet10.cell_value(s,r))
        if 4.0 < sheet10.cell_value(s,r) < 6.0:
            lRisk10.append(sheet10.cell_value(s,r))

for t in range(0, 49):
    for u in range(t,49):
    # print(sheet.cell_value(0, t))
        if 0.0 < sheet11.cell_value(u,t) < 2.0:
            hRisk11.append(sheet11.cell_value(u,t))
            # print(t, u, sheet11.cell_value(u,t))
        if 2.0 < sheet11.cell_value(u,t) < 4.0:
            inRisk11.append(sheet11.cell_value(u,t))
        if 4.0 < sheet11.cell_value(u,t) < 6.0:
            lRisk11.append(sheet11.cell_value(u,t))






plt.plot(50, len(hRisk1), 'mx')
plt.plot(100, len(hRisk2), 'mx')
plt.plot(200, len(hRisk3), 'mx')
# plt.plot(75, len(hRisk4), 'mx')
# plt.plot(80, len(hRisk5), 'mx')
# plt.plot(125, len(hRisk6), 'mx')
plt.plot(150, len(hRisk7), 'mx')
plt.plot(250, len(hRisk8), 'mx')
plt.plot(300, len(hRisk9), 'mx')
plt.plot(350, len(hRisk10), 'mx')
plt.plot(400, len(hRisk11), 'mx')


""" Calculates the sum of number of the row in a matrix """
# hRisk = []
# inRisk = []
# lrisk = []
# for i in range(0,49):
#     for j in range(i, 49):
#         # list.append(sheet.cell_value(i,j))
#         if 0 < sheet.cell_value(i,j) < 2.0:
#             print(sheet.cell_value(i,j))
#             hRisk.append(sheet.cell_value(i,j))
#         if 2.0 < sheet.cell_value(i,j) < 4.0:
#             # print(sheet.cell_value(i,j))
#             inRisk.append(sheet.cell_value(i,j))
# print(len(hRisk))
# print(inRisk)
    # sum.append(sheet.cell_value(0,i))
    #     sum += sheet.cell_value(i,j)
        # sum2 += sheet.cell_value(1,i+1)
    # sumlist.append(sum)



"""Plotting the curves"""
plt.ylabel('Number of interactions of pedestrians at less than 2 meters')
plt.xlabel('Pedestrians flow rate per minute')
plt.ylim(0, 600)
plt.xlim(0, 500)
plt.grid('on')
plt.title("Number of interactions vs. flow rate (sim time = 2 minutes)")
plt.show()
