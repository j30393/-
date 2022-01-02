# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import csv 
# chinese output handling 

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

lst_x = []
lst_y = []

with open('data_handle_new.csv','r',encoding= "utf-8") as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        lst_x.append(int(row[1]))
        lst_y.append(float(row[4]))

written_data = []
r_data = []

sum = 0
season_1 = []
season_2 = []
season_3 = []
season_4 = []
count = 0
for i in range(len(lst_x)-3):
    x = np.array(lst_x[i:i+3])
    y = np.array(lst_y[i:i+3])
    k = np.vstack((x,y))
    r = np.corrcoef(k)
    sum = sum + 1
    count = count + 1
    if(count % 4 == 1):
        season_1.append(r[0,1])
    elif(count %4 == 2):
        season_2.append(r[0,1])
    elif(count %4 == 3):
        season_3.append(r[0,1])
    elif(count %4 == 0):
        season_4.append(r[0,1])
    
    written_data.append(str(r[0,1]))
    r_data.append(r[0,1]) 

cnt = 0
year = 2002
year_data = []
season_1_data = []
season_2_data = []
season_3_data = []
season_4_data = []

with open ('出口物價.txt','w') as fh:
    for data in written_data:
        cnt = cnt + 1
        if(cnt == 5):
            year = year + 1
            cnt = 1
        fh.write(str(year) + ' season ' +str(cnt) + ' : ')
        year_data.append(year + cnt//10)
        if(cnt == 1):
            season_1_data.append(year)
        if(cnt == 2):
            season_2_data.append(year + 0.25)
        if(cnt == 3):
            season_3_data.append(year + 0.5)
        if(cnt == 4):
            season_4_data.append(year + 0.75)
        fh.write(data)
        fh.write('\n')

x_1_out = np.array(season_1_data)
y_1_out = np.array(season_1)
x_2_out = np.array(season_2_data)
y_2_out = np.array(season_2)
x_3_out = np.array(season_3_data)
y_3_out = np.array(season_3)
x_4_out = np.array(season_4_data)
y_4_out = np.array(season_4)

plt.xlabel('時間')
plt.ylabel('出口物價相關係數 以不同季排序')
plt.title('時間 vs 出口物價相關係數')
plt.plot(x_1_out, y_1_out, '.' , color = 'b')
plt.plot(x_2_out, y_2_out, '.' , color = 'm')
plt.plot(x_3_out, y_3_out, '.' , color = 'g')
plt.plot(x_4_out, y_4_out, '.' , color = 'y')

plt.savefig('出口物價相關係數_以不同季排序.png', bbox_inches='tight')
