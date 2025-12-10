import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system('cls')
# a1 = np.array([[2, 4, 6],[4, 3, 2]])
# b1 = np.array([10, 20, 30])
# print(a1.argmax(1))
# print((a1 * b1))
# print((a1 * b1).shape)

# a1 = pd.DataFrame({'a': [2, 4, 6], 'b' : [4, 3, 2]})
# b1 = pd.array([10, 20, 30])
# print(pd.Series(b1, ['a', 'c','b']))
# print(a1)
a = pd.read_csv("C:\\Users\\Admin\\MBCA\\scores.csv")
# print(a)
# print(a[['영어']])
# print(sum([4, 3, 2]))
# a.insert(5,'합계',a.iloc[:,range(1,4)].sum(axis=1))
# a['합계'] = a.iloc[:,range(1,4)].sum(axis=1)
# a.iloc[:,range(1,4)].sum(axis=1)
# a.loc[len(a)] = a.sum([range(1,4)])
print(a.sum([4, 3, 2]))
# print( a[].sum(axis=1))
# print(a.divide())

# col = ['col1','col2','col3']
# row = ['row1','row2','row3']
# data = [[1,2,3],[4,5,6],[7,np.NaN,9]]
# df = pd.DataFrame(data=data,index=row,columns=col)
# print(df)

# print(df.sum(axis=0))



# fread = pd.read_excel("C:\\Users\\Admin\\MBCA\\seoul_weather_2025.xlsx")
# print(fread )
# plt.rcParams['font.family']= 'Malgun Gothic'
# hours = [6, 9, 12, 15, 18, 21, 24]           # 그래프의 x 축 데이터
# temperature = [10, 14, 18, 20, 17, 13, 11]   # 그래프의 y 축 데이터
# plt.plot(hours,temperature, marker='o', linestyle='-', color='orange')
# hours = [i for i in range(3, 25, 3)]
# temperature  = list(i for i in range(10, 30, 3))
# temperature2 = [10, 14, 18, 20, 17, 13, 11]
# plt.plot(hours, temperature, marker='o')
# print(type(hours))
# print(type(temperature))
# print(type(temperature2))
# # plt
# print(temperature)

#한글깨지면..한글글꼴로 지정
# plt.rcParams['font.family']= 'Malgun Gothic'

#예제1: 하루 동안의 온도 변화 그래프 [ 선 그래프 : plot() ]
# 시간(시)별 온도
# hours = [6, 9, 12, 15, 18, 21, 24]           # 그래프의 x 축 데이터
# hours = [i for i in range(6, 25, 3)]
# temperature = [10, 14, 18, 20, 17, 13, 11]   # 그래프의 y 축 데이터

# #plt.plot(hours,temperature)
# #plt.plot(hours,temperature, marker='o')
# #plt.plot(hours,temperature, marker='x')
# #plt.plot(hours,temperature, marker='v')
# #plt.plot(hours,temperature, marker='o', linestyle='-')
# #plt.plot(hours,temperature, marker='o', linestyle='--')
# #plt.plot(hours,temperature, marker='o', linestyle=':')
# plt.plot(hours,temperature, marker='o', linestyle='-', color='orange')

# plt.title('하루 동안의 온도 변화')
# plt.xlabel('시간 (시)')
# plt.ylabel('온도 (°C)')
# plt.show()

