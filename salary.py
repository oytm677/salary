# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
def use_money(age,year):
    tmp_use = 0
    if age < 35:
        tmp_use += 15*12 #家賃
        tmp_use += 10*12 #生活費
    else:
        tmp_use += 200 #住宅ローン
        tmp_use += 30*12 #生活費（家族含む）
    
    tmp_use += 150 #外車買う
    tmp_use += 300 #旅行に行くお金
    tmp_use += 25 #ワールドカップの積み立て
        
    return tmp_use
    
#２２歳から６５歳までの必要年収を計算する
ave_money =[]
x = np.arange(21,65,1)
my_age = 22
nowy = 2019

for i in range(22,66,1):
     ave_money.append(use_money(my_age,nowy))
     nowy = nowy + 1
     my_age = my_age+1 
 


#三菱重工業
salary_Mz = [334.4,667,764.8,791.5,889.3,996,1067.2,1058.3,1058.3]
#三菱商事
salary_Ms = [328,1074,1232,1275,1432,1604,1719,1704,1704]
#パイロット
salary_py =[370,800,913,998,1383,1486,1389,1230,1239]
#３5まで一般企業（JAXAor助教）35で准教授45で教授
salary_pd = [0,0,618.9,618.7,695.2,1245.4,1334.4,1278.8,900.7]
#コンサル　pwc
salary_cn = [568.3,707.9,777.7,887.3,997,1116,1196,1146,807]
age = [22,27,32,37,42,47,52,57,62]

font = {'family':'IPAGothic'}

fig = plt.figure(figsize=(16,9),facecolor='white')
ax = fig.add_subplot(1,1,1)
ax.set_ylabel('money',fontsize=25)
ax.set_xlabel('age',fontsize=25)
ax.plot(age,salary_Ms,'o-',c='black',label = 'mitubishi_shouzi')
ax.plot(age,salary_Mz,'o-',c='tan',label = 'mitubishi_industry')
ax.plot(age,salary_py,'o-',c='grey',label='pilot')
ax.plot(age,salary_pd,'o-',c='darkcyan',label='researcher')
ax.plot(age,salary_cn,'o-',c='pink',label='pwc')
ax.plot(x,ave_money,'o-',c='red',label='need')
ax.legend(bbox_to_anchor=(0, -0.1), loc='upper left', borderaxespad=0, fontsize=18)
plt.show()
