import numpy as np
import matplotlib.pyplot as plt

ref_voltage = 3.3
period = 0.002  # sampling period in ms
data_size = 4990
length = 1158

name0 = 'data_0_1_vyd_3.txt'
name1 = 'data_1_1_vyd_3.txt'

T1 = []
V1 = []
T2 = []
V2 = []
with open(name0, 'r') as file:
    for i in range(data_size):
        T1.append(period * i)
        V1.append(float(file.readline()))

with open(name1, 'r') as file:
    for i in range(data_size):
        T2.append(period * i)
        V2.append(float(file.readline()))

plt.plot(T1, V1, c='red')
plt.plot(T2, V2, c='blue')

plt.minorticks_on()
plt.grid(which='major',
         color='grey',
         linewidth=1)

plt.grid(which='minor',
         color='k',
         linewidth=0.3,
         linestyle=":")

plt.xlabel("t, мсек")
plt.title("График зависимости дБ от времени")
plt.show()