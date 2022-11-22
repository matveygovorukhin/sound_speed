import numpy as np
import matplotlib.pyplot as plt

ref_voltage = 3.3
period = 0.002  # sampling period in ms
data_size = 4990
length = 1158

name0 = 'data_0_N_vyd.txt'
name1 = 'data_1_N_vyd.txt'

T1 = []
V1 = []
T2 = []
V2 = []

tm1 = #Время 1 пика
tm2 = #Время 2 пика
norm1 = #Макс значение 1
norm2 = #Макс значение 2
sdvig =  #Сдвиг по времени чтобы первые пики совпали

sum1 = 0
sum2 = 0
n1 = tm1//period
n2 = tm2//period

with open(name0, 'r') as file:
    for i in range(data_size):
        T1.append(period * i)
        V1.append(float(file.readline()))

    for i in range(int(n1)):
        sum1 += V1[i]

    sred1 = sum1 / n1

    for i in range(data_size):
        V1[i] -= sred1

    for i in range(data_size):
        V1[i] /= norm1

with open(name1, 'r') as file:
    for i in range(data_size):
        T2.append(period * i)
        V2.append(float(file.readline()))

    for i in range(int(n2)):
        sum2 += V2[i]

    sred2 = sum2 / n2

    for i in range(data_size):
        V2[i] -= sred2

    for i in range(data_size):
        V2[i] /= norm2

    for i in range(data_size):
        T2[i] -= sdvig

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