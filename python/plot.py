import sys
import os
import glob
import pandas as pd
import re
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Plotting aaaall the data

## QUALITY ASSESSMENT ####
path = 'Clean_Data/'
sens = []
fig = plt.figure()
for f in ['2','3','4','5','6','7', '8','9','10','11','12', '13', '14', '15','16']:
    file = path + f + ".csv"
    sen = pd.read_csv(file, parse_dates=True, index_col=0,header=0)

    #drop zeros and nan values, resample
    sen = sen[sen!=0]
    sen = sen.groupby(sen.index).mean()
    sen.dropna(inplace=True)
    #sen = sen.resample(rule='5T').sum()
    #print(sen.head)

    #create column delta with seconds passed since start of measurements
    sen['date']=sen.index.values
    sen['hour']=0

    for i in range(1,len(sen)):
        sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()/3600
    sensor=pd.DataFrame(index=sen['hour'])
    sen.index=sen['hour']
    sen.drop(columns=['hour', 'date'], inplace=True)
    sen.columns=[f]

    plt.fill_between(
        x= sen.index,
        y1= sen[f],
        where= (899 < sen[f]),
        color= "r",
        alpha= 1,
        label='T>=900')
    plt.fill_between(
        x= sen.index,
        y1= sen[f],
        where= ((900 > sen[f]) & (sen[f]>599)),
        color= "m",
        alpha= 1,
        label='600<=T<900')
    plt.fill_between(
        x= sen.index,
        y1= sen[f],
        where= (600 > sen[f]),
        color= "b",
        alpha= 1,
        label='T<600')
    plt.title("Sensor " + str(f))
    plt.legend()
    #sen.plot(legend=True)
    plt.ylabel('Temperature [°C]')
    plt.xlabel('Time [hours]')
    #plt.plot(sen.index, sen.iloc[:,0], label=sen.columns[0])
    plt.plot(sen.index,sen[f], label=f)
    plt.show()
plt.legend()
plt.show()


#### PLOT LONGEST SENSORS NR 3, 6, 9, 12, 15####

path = 'Clean_Data/'
sens = []
fig = plt.figure()
for f in ['3','6','9', '12', '15']:
    file = path + f + ".csv"
    sen = pd.read_csv(file, parse_dates=True, index_col=0,header=0)

    #drop zeros and nan values, resample
    sen = sen[sen!=0]
    sen = sen.groupby(sen.index).mean()
    sen.dropna(inplace=True)
    #sen = sen.resample(rule='5T').sum()
    #print(sen.head)

    #create column delta with seconds passed since start of measurements
    sen['date']=sen.index.values
    sen['hour']=0

    for i in range(1,len(sen)):
        sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()/3600
    sensor=pd.DataFrame(index=sen['hour'])
    sen.index=sen['hour']
    sen.drop(columns=['hour', 'date'], inplace=True)
    sen.columns=[f]

    #sen.plot(legend=True)
    plt.ylabel('Temperature [°C]')
    plt.xlabel('Time [hours]')
    #plt.plot(sen.index, sen.iloc[:,0], label=sen.columns[0])
    plt.plot(sen.index,sen[f], label=f)
plt.legend()
plt.title("Lowest layer temperatures")
plt.show()


# #### PLOT MIDDLE SENSORS NR 4, 7, 10, 13####
### CONVERT DATE TO TIMESPAN ####
path = 'Clean_Data/'
sens = []
fig = plt.figure()
for f in ['4','7', '10','13']:
    file = path + f + ".csv"
    sen = pd.read_csv(file, parse_dates=True, index_col=0,header=0)

    #drop zeros and nan values, resample
    sen = sen[sen!=0]
    sen = sen.groupby(sen.index).mean()
    sen.dropna(inplace=True)
    #sen = sen.resample(rule='5T').sum()
    #print(sen.head)

    #create column delta with seconds passed since start of measurements
    sen['date']=sen.index.values
    sen['hour']=0

    for i in range(1,len(sen)):
        sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()/3600
    sensor=pd.DataFrame(index=sen['hour'])
    sen.index=sen['hour']
    sen.drop(columns=['hour', 'date'], inplace=True)
    sen.columns=[f]

    #sen.plot(legend=True)
    plt.ylabel('Temperature [°C]')
    plt.xlabel('Time [hours]')
    #plt.plot(sen.index, sen.iloc[:,0], label=sen.columns[0])
    plt.plot(sen.index,sen[f], label=f)
plt.legend()
plt.title("Middle layer temperatures")
plt.show()

# #### PLOT SURFACE SENSORS NR 2, 5, 8, 11, 14, 16####
### CONVERT DATE TO TIMESPAN ####
path = 'Clean_Data/'
sens = []
fig = plt.figure()
for f in ['2','5','8','11','14','16']:
    file = path + f + ".csv"
    sen = pd.read_csv(file, parse_dates=True, index_col=0,header=0)

    #drop zeros and nan values, resample
    sen = sen[sen!=0]
    sen = sen.groupby(sen.index).mean()
    sen.dropna(inplace=True)
    #sen = sen.resample(rule='5T').sum()
    #print(sen.head)

    #create column delta with seconds passed since start of measurements
    sen['date']=sen.index.values
    sen['hour']=0

    for i in range(1,len(sen)):
        sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()/3600
    sensor=pd.DataFrame(index=sen['hour'])
    sen.index=sen['hour']
    sen.drop(columns=['hour', 'date'], inplace=True)
    sen.columns=[f]

    #sen.plot(legend=True)
    plt.ylabel('Temperature [°C]')
    plt.xlabel('Time [hours]')
    #plt.plot(sen.index, sen.iloc[:,0], label=sen.columns[0])
    plt.plot(sen.index,sen[f], label=f)
plt.legend()
plt.title("Surface layer temperatures")
plt.show()
# #### PLOT CENTER SLICE NR 2, 5, 8, 7, 4, 6, 3####

path = 'Clean_Data/'
sens = []
#fig = plt.figure()
fig, ax = plt.subplots()
for f in ['2','3','4','5','6','7', '8']:
    file = path + f + ".csv"
    sen = pd.read_csv(file, parse_dates=True, index_col=0,header=0)

    #drop zeros and nan values, resample
    sen = sen[sen!=0]
    sen = sen.groupby(sen.index).mean()
    sen.dropna(inplace=True)
    #sen = sen.resample(rule='5T').sum()
    #print(sen.head)

    #create column delta with seconds passed since start of measurements
    sen['date']=sen.index.values
    sen['hour']=0

    for i in range(1,len(sen)):
        sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()/3600
    sensor=pd.DataFrame(index=sen['hour'])
    sen.index=sen['hour']
    sen.drop(columns=['hour', 'date'], inplace=True)
    sen.columns=[f]
    sen=sen[sen.index<=50]

    #sen.plot(legend=True)
    plt.ylabel('Temperature [°C]')
    plt.xlabel('Time [hours]')
    #plt.plot(sen.index, sen.iloc[:,0], label=sen.columns[0])
    plt.plot(sen.index,sen[f], label=f)
plt.legend()
ax.set_ylim(0, 1200)
plt.title("Center slice temperatures")
plt.show()


#### PLOT FRONT SLICE NR 16, 14, 11, 13, 10, 15, 12, 9####
path = 'Clean_Data/'
sens = []
#fig = plt.figure()
fig, ax = plt.subplots()
for f in ['9','10','11','12', '13', '14', '15','16']:
    file = path + f + ".csv"
    sen = pd.read_csv(file, parse_dates=True, index_col=0,header=0)

    #drop zeros and nan values, resample
    sen = sen[sen!=0]
    sen = sen.groupby(sen.index).mean()
    sen.dropna(inplace=True)
    #sen = sen.resample(rule='5T').sum()
    #print(sen.head)

    #create column delta with seconds passed since start of measurements
    sen['date']=sen.index.values
    sen['hour']=0

    for i in range(1,len(sen)):
        sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()/3600
    sensor=pd.DataFrame(index=sen['hour'])
    sen.index=sen['hour']
    sen.drop(columns=['hour', 'date'], inplace=True)
    sen=sen[sen.index<=50]
    sen.columns=[f]

    plt.ylabel('Temperature [°C]')
    plt.xlabel('Time [hours]')
    plt.plot(sen.index,sen[f], label=f)
plt.legend()
ax.set_ylim(0, 800)
plt.title("Front slice temperatures")
plt.show()

#### PLOT MAXIMUM TEMPERATURES VS SURFACE DISTANCE####
dsurf = []
path = 'Clean_Data/'
depths = [18, 112, 70, 23, 132, 70, 29, 112, 70, 19, 112, 70, 14, 112, 35]
index = ['2','3','4','5','6','7', '8','9','10','11','12', '13', '14', '15','16']
max = []
tmax = []
depth_pairs = pd.DataFrame(index=index, data=depths, columns=['Distance to surface'])
for i in index:
    deep_path = path + i + ".csv"
    sen = pd.read_csv(deep_path, parse_dates=True, index_col=0,header=0)
    sen=sen.loc[~(sen==0).all(axis=1)]
    max.append(sen.max())
    tdelta = (sen.idxmax()-sen.index[0])[0]
    print(tdelta)
    tdelta = tdelta.seconds/3600
    tmax.append(tdelta)
print(max)
print(tmax)
fig, ax = plt.subplots()
ax.scatter(max[:6], depths[:6], label='center', marker="o")
ax.scatter(max[7:], depths[7:], label='front', marker="^")
ax.legend()
plt.xlabel('Maximum temperature [°C]')
plt.ylabel('Distance to surface [cm]')
#plt.title("Max temperatures vs distance from clamp surface")
plt.show()

#### PLOT TIME TO REACH MAXIMUM TEMPERATURES VS SURFACE DISTANCE ####
fig, ax = plt.subplots()
ax.scatter(tmax[:6], depths[:6], label='center', marker="o")
ax.scatter(tmax[7:], depths[7:], label='front', marker="^")
ax.legend()
plt.xlabel('Time at max. T [h]')
plt.ylabel('Distance to surface [cm]')
#plt.title("Time to reach max temperatures vs distance from clamp surface")
plt.show()

### APPROXIMATE TEMPERATURE PROFILE OF BURNING CHAMBERS####
path = 'Clean_Data/'
deep_sens = []
fig = plt.figure()
for i in ['3', '6']:#, '9', '12', '15']:
    deep_path = path + i + ".csv"
    deep_sen = pd.read_csv(deep_path, parse_dates=True, index_col=0,header=0)
    deep_sen=deep_sen.loc[~(deep_sen==0).all(axis=1)]
    deep_sen = deep_sen.groupby(deep_sen.index).mean()
    deep_sen = deep_sen.resample(rule='5T').bfill()
    print(deep_sen.head)
    print(len(deep_sen))
    deep_sens.append(deep_sen)
sensors=pd.concat(deep_sens, axis=1)
sensors=sensors.dropna(axis='rows')
mean_heat = sensors.mean(axis=1)
mean_heat.plot()
plt.show()

# use glob to get all the csv files 
# # in the folder
# path = "Clean_Data/"
# csv_files = glob.glob(os.path.join(path, "*.csv"))
# # loop over the list of csv files
# sensors= []
# plt.figure()
# for f in csv_files:
#     sen = pd.read_csv(f, parse_dates=True, index_col=0,header=0)

#     #drop zeros and nan values
#     sen = sen[sen!=0]
#     sen = sen.groupby(sen.index).mean()
#     sen.dropna(inplace=True)

#     #create column delta with seconds passed since start of measurements
#     sen['date']=sen.index.values
#     sen['delta']=0
#     print(sen.head)
#     for i in range(1,len(sen)):
#         sen.iloc[i,2]=(sen.iloc[i,1]-sen.iloc[0,1]).total_seconds()
#     #sen.plot(legend=True)
#     #plt.plot(sen.index, sen.iloc[:,0], label=sen.columns[0])
#     sensors.append(sen)
# sensors=pd.concat(sensors, axis=0)
# print(sensors.head)
# #plt.legend()
# plt.show()
# for sen in sensors:
#     sen = sen.resample(rule='5T').sum()
#     print(sen.head)