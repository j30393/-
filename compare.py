# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import csv 
# chinese output handling 
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

lst_x = []
lst_y = []
# x co-ordinates
with open('data_handle_after.csv','r',encoding= "utf-8") as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        lst_x.append(int(row[1]))
        lst_y.append(float(row[8]))

x = np.array(lst_x)
y = np.array(lst_y)
k = np.vstack((x,y))
r = np.corrcoef(k)
print(r)
A = np.array([x, np.ones(len(lst_x))])


# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y, rcond=None)[0]
print(w)

line = w[0]*x + w[1]  # regression line
plt.xlabel('GDP')
plt.ylabel('國泰房產')
plt.title('GDP 對上國泰房產(扣除 2007~2010 . 2019 ) ')
plt.legend()
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.savefig('GDP_國泰房產_2007_2010_except.png', bbox_inches='tight')