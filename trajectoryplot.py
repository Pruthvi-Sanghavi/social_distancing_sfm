import csv
import xlrd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# path to the file.
path = "2.xlsx"

# reading the excel data file
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)

# debug
# print(sheet.cell_value(0, 0))
ped1_xcoord = []
ped1_ycoord = []
ped1_time = []

ped2_xcoord = []
ped2_ycoord = []
ped2_time = []

ped3_xcoord = []
ped3_ycoord = []
ped3_time = []

ped4_xcoord = []
ped4_ycoord = []
ped4_time = []

ped5_xcoord = []
ped5_ycoord = []
ped5_time = []

ped6_xcoord = []
ped6_ycoord = []
ped6_time = []

ped7_xcoord = []
ped7_ycoord = []
ped7_time = []

ped8_xcoord = []
ped8_ycoord = []
ped8_time = []

ped9_xcoord = []
ped9_ycoord = []
ped9_time = []

ped10_xcoord = []
ped10_ycoord = []
ped10_time = []

ped11_xcoord = []
ped11_ycoord = []
ped11_time = []

ped12_xcoord = []
ped12_ycoord = []
ped12_time = []

ped13_xcoord = []
ped13_ycoord = []
ped13_time = []

ped14_xcoord = []
ped14_ycoord = []
ped14_time = []

ped15_xcoord = []
ped15_ycoord = []
ped15_time = []

ped16_xcoord = []
ped16_ycoord = []
ped16_time = []

ped17_xcoord = []
ped17_ycoord = []
ped17_time = []

ped18_xcoord = []
ped18_ycoord = []
ped18_time = []

ped19_xcoord = []
ped19_ycoord = []
ped19_time = []

ped20_xcoord = []
ped20_ycoord = []
ped20_time = []



# Getting the waypoints for pedestrian 1
for i in range(1, 126410):
    x = sheet.cell_value(i, 1)
    if x == 1:
        ped1_xcoord.append(sheet.cell_value(i, 4))
        ped1_ycoord.append(sheet.cell_value(i, 5))
        ped1_time.append(sheet.cell_value(i, 0))


    if x == 2:
        ped2_xcoord.append(sheet.cell_value(i, 4))
        ped2_ycoord.append(sheet.cell_value(i, 5))
        ped2_time.append(sheet.cell_value(i, 0))


    if x == 3:
        ped3_xcoord.append(sheet.cell_value(i, 4))
        ped3_ycoord.append(sheet.cell_value(i, 5))
        ped3_time.append(sheet.cell_value(i, 0))

    if x == 4:
        ped4_xcoord.append(sheet.cell_value(i, 4))
        ped4_ycoord.append(sheet.cell_value(i, 5))
        ped4_time.append(sheet.cell_value(i, 0))

    if x == 5:
        ped5_xcoord.append(sheet.cell_value(i, 4))
        ped5_ycoord.append(sheet.cell_value(i, 5))
        ped5_time.append(sheet.cell_value(i, 0))

    if x == 6:
        ped6_xcoord.append(sheet.cell_value(i, 4))
        ped6_ycoord.append(sheet.cell_value(i, 5))
        ped6_time.append(sheet.cell_value(i, 0))

    if x == 7:
        ped7_xcoord.append(sheet.cell_value(i, 4))
        ped7_ycoord.append(sheet.cell_value(i, 5))
        ped7_time.append(sheet.cell_value(i, 0))

    if x == 8:
        ped8_xcoord.append(sheet.cell_value(i, 4))
        ped8_ycoord.append(sheet.cell_value(i, 5))
        ped8_time.append(sheet.cell_value(i, 0))

    if x == 9:
        ped9_xcoord.append(sheet.cell_value(i, 4))
        ped9_ycoord.append(sheet.cell_value(i, 5))
        ped9_time.append(sheet.cell_value(i, 0))

    if x == 10:
        ped10_xcoord.append(sheet.cell_value(i, 4))
        ped10_ycoord.append(sheet.cell_value(i, 5))
        ped10_time.append(sheet.cell_value(i, 0))

    if x == 11:
        ped11_xcoord.append(sheet.cell_value(i, 4))
        ped11_ycoord.append(sheet.cell_value(i, 5))
        ped11_time.append(sheet.cell_value(i, 0))

    if x == 12:
        ped12_xcoord.append(sheet.cell_value(i, 4))
        ped12_ycoord.append(sheet.cell_value(i, 5))
        ped12_time.append(sheet.cell_value(i, 0))

    if x == 13:
        ped13_xcoord.append(sheet.cell_value(i, 4))
        ped13_ycoord.append(sheet.cell_value(i, 5))
        ped13_time.append(sheet.cell_value(i, 0))

    if x == 14:
        ped14_xcoord.append(sheet.cell_value(i, 4))
        ped14_ycoord.append(sheet.cell_value(i, 5))
        ped14_time.append(sheet.cell_value(i, 0))

    if x == 15:
        ped15_xcoord.append(sheet.cell_value(i, 4))
        ped15_ycoord.append(sheet.cell_value(i, 5))
        ped15_time.append(sheet.cell_value(i, 0))

    if x == 16:
        ped16_xcoord.append(sheet.cell_value(i, 4))
        ped16_ycoord.append(sheet.cell_value(i, 5))
        ped16_time.append(sheet.cell_value(i, 0))

    if x == 17:
        ped17_xcoord.append(sheet.cell_value(i, 4))
        ped17_ycoord.append(sheet.cell_value(i, 5))
        ped17_time.append(sheet.cell_value(i, 0))

    if x == 18:
        ped18_xcoord.append(sheet.cell_value(i, 4))
        ped18_ycoord.append(sheet.cell_value(i, 5))
        ped18_time.append(sheet.cell_value(i, 0))

    if x == 19:
        ped19_xcoord.append(sheet.cell_value(i, 4))
        ped19_ycoord.append(sheet.cell_value(i, 5))
        ped19_time.append(sheet.cell_value(i, 0))

    if x == 20:
        ped20_xcoord.append(sheet.cell_value(i, 4))
        ped20_ycoord.append(sheet.cell_value(i, 5))
        ped20_time.append(sheet.cell_value(i, 0))


fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')
# ax.legend()

ax.plot(ped1_xcoord, ped1_ycoord, ped1_time, '-g')
ax.plot(ped2_xcoord, ped2_ycoord, ped2_time, '-g')
ax.plot(ped3_xcoord, ped3_ycoord, ped3_time, '-g')
ax.plot(ped4_xcoord, ped4_ycoord, ped4_time, '-g')
ax.plot(ped5_xcoord, ped5_ycoord, ped5_time, '-g')
ax.plot(ped6_xcoord, ped6_ycoord, ped6_time, '-g')
ax.plot(ped7_xcoord, ped7_ycoord, ped7_time, '-g')
ax.plot(ped8_xcoord, ped8_ycoord, ped8_time, '-g')
ax.plot(ped9_xcoord, ped9_ycoord, ped9_time, '-g')
ax.plot(ped10_xcoord, ped10_ycoord, ped10_time, '-g')
ax.plot(ped11_xcoord, ped11_ycoord, ped11_time, '-g')
ax.plot(ped12_xcoord, ped12_ycoord, ped12_time, '-g')
ax.plot(ped13_xcoord, ped13_ycoord, ped13_time, '-g')
ax.plot(ped14_xcoord, ped14_ycoord, ped14_time, '-g')
ax.plot(ped15_xcoord, ped15_ycoord, ped15_time, '-g')
ax.plot(ped16_xcoord, ped16_ycoord, ped16_time, '-g')
ax.plot(ped17_xcoord, ped17_ycoord, ped17_time, '-g')
ax.plot(ped18_xcoord, ped18_ycoord, ped18_time, '-g')
ax.plot(ped19_xcoord, ped19_ycoord, ped19_time, '-g')
ax.plot(ped20_xcoord, ped20_ycoord, ped20_time, '-g')



ax.set_xlabel("x coordinate in meters(m)")
ax.set_ylabel("y coordinate in meters(m)")
ax.set_zlabel('time in seconds(s)')
plt.show()