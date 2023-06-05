import sys
import os
import glob
import pandas as pd
import re
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def remove_outliers(columns,n_std):
    filtered_columns = []
    for col in columns:
        print('Working on column: {}'.format(col))

        col=col[pd.to_numeric(col, errors='coerce').notnull()]
        mean = col.mean()
        sd = col.std()

        col = col[(col <= mean+(n_std*sd))]
        filtered_columns.append(col)
    return columns

path = "Data"
#find all files to be read
extension = 'CSV'
os.chdir(path)
filelist = []
for p,n,f in os.walk(os.getcwd()):
    for a in f:
        a = str(a)
        if a.endswith('.CSV'):
            filelist.append(p+"/"+a)
#read one file and extract time-temperature values
DL1=[]
str1="DL_1_2_3_4"
col = ['date', 'time']
sDL1 = col+['1', '2', '3', '4']
DL2=[]
str2="DL_6_7_8_5"
sDL2 = col + ['6', '7', '8', '5']
DL3=[]
str3="DL_9_10_11_12"
sDL3= col+['9', '10', '11', '12']
DL4=[]
str4="DL_13_14_15_16"
sDL4= col+['13', '14', '15', '16']
for i in filelist:
    if str1 in i:
        DL1.append(i)
    if  str2 in i:
        DL2.append(i)
    if str3 in i:
        DL3.append(i)
    if str4 in i:
        DL4.append(i)
data = [[DL1,sDL1], [DL2,sDL2], [DL3, sDL3], [DL4, sDL4]]
col_names=['date', 'time']
all_sensors = []
for DL in data:
    sensors = []
    for file in DL[0]:
        file=pd.read_csv(file)
        file.set_axis(DL[1], axis=1, inplace=True)
        file.set_index(pd.to_datetime(file['date']+' ' + file['time'], dayfirst=True), inplace=True)
        file=file[DL[1][2:6]]
        sensors.append(file)
    sensors=pd.concat(sensors, axis=0)
    all_sensors.append(sensors)
min_max=[[],[]]

fig = plt.figure()

for sensor_bundle in all_sensors:
    for i in [0, 1, 2, 3]:
        sen= sensor_bundle.iloc[:,i]
        sen= sen[pd.to_numeric( sen, errors='coerce').notnull()]
        sen= sen.astype(float)
        sen.replace([np.inf, -np.inf], 0, inplace=True)
        sen=sen.sort_index()
        sen = sen[sen>10]
        diff = sen.pct_change()
        dneg = diff[diff<0]
        #print(dneg.describe())
        dneg_med = dneg.median()
        dneg_std = dneg.std(ddof=0)
        dpos = diff[diff>0]
        #print(dpos.describe())
        dpos_med = dpos.median()
        dpos_std = dpos.std(ddof=0)
        print("med neg: ",dneg_med, "std neg: ", dneg_std,"med pos: ",dpos_med, "std pos: ",dpos_std)



        sen.plot(legend=True)
        plt.show()
        #sen.to_csv("../Clean_Data/"+sen.name +".csv")

        #sen_np = np.array(sen, dtype=np.float64)
        #sen_np=sen_np[(np.abs(stats.zscore(sen_np)) < 3).all(axis=1)]
plt.show()

    #sensor.resample('5T')
    #sensor=sensor[sensor.applymap(np.isreal).all(1)]
    #sensor=sensor[(np.abs(stats.zscore(sensor)) < 3).all(axis=1)]
    #print(len(sensor))
    #min_max[0].append(sensor.index[0])
#remove outliers


#all_sensors=pd.concat(all_sensors, axis=1,ignore_index=True)



