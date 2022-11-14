# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:04:11 2022

@author: 20215
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('serie_7.csv') # <=====
df1 = data1.dropna()

time1 = df1['Tiempo (s)'].tolist()
position1 = df1['Posición (m)'].tolist()
velocity1 = df1['Vector velocidad (m/s)'].tolist()
aceleration1 = df1['Aceleración (m/s²)'].tolist()
fuerza1 = df1['Fuerza (N)']

t1 = np.array(time1, dtype=np.float64)
p1 = np.array(position1, dtype=np.float64)
v1 = np.array(velocity1, dtype=np.float64)
a1 = np.array(aceleration1, dtype=np.float64)
f1 = np.array(fuerza1, dtype=np.float64)

#----------------------------------------------
data2 = pd.read_csv('serie_8.csv') # <=====
df2 = data2.dropna()

time2 = df2['Tiempo (s)'].tolist()
position2 = df2['Posición (m)'].tolist()
velocity2 = df2['Vector velocidad (m/s)'].tolist()
aceleration2 = df2['Aceleración (m/s²)'].tolist()
fuerza2 = df2['Fuerza (N)']

t2 = np.array(time2, dtype=np.float64)
p2 = np.array(position2, dtype=np.float64)
v2 = np.array(velocity2, dtype=np.float64)
a2 = np.array(aceleration2, dtype=np.float64)
f2 = np.array(fuerza2, dtype=np.float64)

#-------------------------------------------------
data3 = pd.read_csv('serie_9.csv') # <=====
df3 = data3.dropna()

time3 = df3['Tiempo (s)'].tolist()
position3 = df3['Posición (m)'].tolist()
velocity3 = df3['Vector velocidad (m/s)'].tolist()
aceleration3 = df3['Aceleración (m/s²)'].tolist()
fuerza3 = df3['Fuerza (N)']

t3 = np.array(time3, dtype=np.float64)
p3 = np.array(position3, dtype=np.float64)
v3 = np.array(velocity3, dtype=np.float64)
a3 = np.array(aceleration3, dtype=np.float64)
f3 = np.array(fuerza3, dtype=np.float64)

#-------------------------------------------------------
data4 = pd.read_csv('serie_6.csv') # <=====
df4 = data4.dropna()

time4 = df4['Tiempo (s)'].tolist()
position4 = df4['Posición (m)'].tolist()
velocity4 = df4['Vector velocidad (m/s)'].tolist()
aceleration4 = df4['Aceleración (m/s²)'].tolist()
fuerza4 = df4['Fuerza (N)']

t4 = np.array(time4, dtype=np.float64)
p4 = np.array(position4, dtype=np.float64)
v4 = np.array(velocity4, dtype=np.float64)
a4 = np.array(aceleration4, dtype=np.float64)
f4 = np.array(fuerza4, dtype=np.float64)
#-------------------------------------------------------
data5 = pd.read_csv('serie_5.csv') # <=====
df5 = data5.dropna()

time5 = df5['Tiempo (s)'].tolist()
position5 = df5['Posición (m)'].tolist()
velocity5 = df5['Vector velocidad (m/s)'].tolist()
aceleration5 = df5['Aceleración (m/s²)'].tolist()
fuerza5 = df5['Fuerza (N)']

t5 = np.array(time5, dtype=np.float64)
p5 = np.array(position5, dtype=np.float64)
v5 = np.array(velocity5, dtype=np.float64)
a5 = np.array(aceleration5, dtype=np.float64)
f5 = np.array(fuerza5, dtype=np.float64)
#-------------------------------------------------------
data6 = pd.read_csv('serie_2.csv') # <=====
df6 = data6.dropna()

time6 = df6['Tiempo (s)'].tolist()
position6 = df6['Posición (m)'].tolist()
velocity6 = df6['Vector velocidad (m/s)'].tolist()
aceleration6 = df6['Aceleración (m/s²)'].tolist()
fuerza6 = df6['Fuerza (N)']

t6 = np.array(time6, dtype=np.float64)
p6 = np.array(position6, dtype=np.float64)
v6 = np.array(velocity6, dtype=np.float64)
a6 = np.array(aceleration6, dtype=np.float64)
f6 = np.array(fuerza6, dtype=np.float64)
# Plot
plt.style.use(['science', 'notebook', 'grid']) # 'dark_background
##########------------------------
ax = plt.axes(projection="3d")
ax.scatter(t1, f1, 1, color='blue', alpha=0.7)
ax.scatter(t2, f2, 2, color='green', alpha=0.7)
ax.scatter(t3, f3, 3, color='purple', alpha=0.7)
ax.set_title('Fuerza')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Fuerza [N]')
plt.show()

ax = plt.axes(projection="3d")
#ax.scatter(t6, f6, p6, color='red', alpha=0.5, label='Serie 2')
#ax.scatter(t5, f5, p5, color='cyan', alpha=0.6, label='Serie 5')
#ax.scatter(t4, f4, p4, color='orange', alpha=1, label='Serie 6')
ax.scatter(t1, f1, p1, color='blue', alpha=1, label='Serie 7')
ax.scatter(t2, f2, p2, color='green', alpha=1, label='Serie 8')
ax.scatter(t3, f3, p3, color='purple', alpha=1, label='Serie 9')
#ax.set_title('Fuerza')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Fuerza [N]')
ax.set_zlabel('Position [m]')
ax.legend(loc=0)
plt.show()







