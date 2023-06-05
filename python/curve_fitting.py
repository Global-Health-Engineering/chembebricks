# fit a polynomial to chosen temperature measurements
from numpy import arange
import pandas as pd
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
import numpy as np

# define the true objective function
def objective(x, a, b, c, d, e, f, g):#, h):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + e * x**5 + f* x**6 +g#* x**7# +h

# load the dataset
#url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
path="high_heat_profiles/all_deep_sens.csv"
df = read_csv(path, parse_dates=True, index_col=0,header=0)
#drop zeros and nan values
df = df[df!=0]
df.dropna(inplace=True)
#create column delta with seconds passed since start of measurements
df['date']=df.index.values
df['delta']=0
print(df.head)
for i in range(1,len(df)):
    df.iloc[i,2]=(df.iloc[i,1]-df.iloc[0,1]).total_seconds()

#cut dataframe in two: one will be quadratically approximated, the other just interpolated
df2=df.iloc[int(len(df)*3/4):,:]
df = df.iloc[0:int(len(df)*3/4),:]
#drop date column
df.drop('date', axis=1, inplace=True)
df2.drop('date', axis=1, inplace=True)

data = df.values
# choose the input and output variables
x, y = data[:, 1], data[:, 0]
# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b, c, d, e, f, g=popt#, h = popt
#print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
# plot input vs output
pyplot.scatter(x/3600, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
x_line1=x_line/3600
# calculate the output for the range
y_line = objective(x_line, a, b, c, d, e, f, g)#, h)
y_line2=df2.values[:,0]
x_line2=df2.values[:,1]
x_line2=np.append(x_line,x_line2)
y_line2= np.append(y_line,y_line2)
y_line=y_line[:180000]
x_line=x_line[:180000]
fit = pd.DataFrame(index=None,data=y_line)
print(fit.head)

#fit.to_csv("high_heat_profiles/interpolated3.csv", sep=',', index=False)
#create a line plot for the mapping function
pyplot.plot(x_line/3600, y_line, '--', color='red')
pyplot.xlabel("Time [h]")
pyplot.ylabel("T [°C]")
pyplot.show()