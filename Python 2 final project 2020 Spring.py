import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
from statistics import mean


#***    This program will ingest the tesla stock and coronavirus dataset,
#***    do some analysis, and ultimately output the data into a dumbbell plot,
#***    scatter plot,

#modules sometimes warn the user of things they want to do
#this ignores those warnings
def hide_warnings():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
        
hide_warnings()


#this is going to be called for each file to create dataframes
def load_data(filename):
    data = pd.read_csv(filename)

    return data

#Create one printable line seperator
def line_sep():
    print('____________________________________________________________________________')


#load raw dataset
data = load_data('All_Data.csv')

#converting date collumn to datetime format
data['Date'] = pd.to_datetime(data['Date']) #or use np.datetime64 in a loop
#print raw dataset
def Data_Open():
    print('\nFull, Raw Dataset')
    line_sep()
    print(data)
    line_sep()
Data_Open()

#find best fit slope and intercept to later plot trendline 
def best_fit_slope_and_intercept1(xval, yval):
    m = (((mean(xval)*mean(yval)) - mean(xval*yval)) /
         ((mean(xval)*mean(yval)) - mean(xval*xval)))
    
    b = mean(yval) - m*mean(xval)
    
    return m, b


#____________________________________________________________________________________________________
#print dataset of just date and average price
date_and_price = data[['Date','Average Price', 'year']]

print("\nDate and price")
print(date_and_price)
line_sep()

#Singular parts
'''print('Dates')
dates = date_and_price[['Date']].values
print(dates)
line_sep()'''

#Print Years    
'''print('Years')
years = date_and_price[['year']].values
print(years)
line_sep()'''

#Print Average Stock Price
'''print('Average Stock Price')
avgprice = date_and_price[['Average Price']].values
print(avgprice)
line_sep()'''

#Print Unique Years
print('\nDifferent years')
all_years = date_and_price['year'].unique()
print(all_years)
line_sep()

# Start the analysis

#create a dataframe with only average price, volume, and corona cases.
df_vars = data[['Volume', 'Average Price', 'CoronaCases']]

#generating a correlation matrix for analysis
print("Correlation Matrix")
corr_matrix = df_vars.corr(method='pearson')
print(corr_matrix)
line_sep()

# create data arrays for each individual variable
Volume = np.array(data['Volume']/1000000)
AvgP = np.array(data['Average Price'])
CovidC = np.array(data['CoronaCases'])

#Now that we have this data array, we can compute a variety of summary statistics:
#Volume
print("Daily Volume Stats:")
print("Mean Volume:       ", round(Volume.mean(), 4), 'Mil')
print("Minimum Volume:    ", Volume.min(), 'Mil')
print("Maximum Volume:    ", Volume.max(), 'Mil')
print("Volume Standard Deviation:", round(Volume.std(), 4), 'Mil')
print("\n")

#Average Price
print("Daily Avg Price Stats:")
print("Mean Price:       ", '$', round(AvgP.mean(), 4))
print("Minimum Price:    ", '$', AvgP.min())
print("Maximum Price:    ", '$', AvgP.max())
print("Average Price Standard Deviation:", '$', round(AvgP.std(), 3))
print("\n")

#Coronavirus Cases
print("Daily COVID 19 Stats:")
print("Mean COVID Cases:       ", round(CovidC.mean(), 4))
print("Minimum COVID Cases:    ", CovidC.min())
print("Maximum COVID Cases:    ", CovidC.max())
print("COVID Cases Standard Deviation:", round(CovidC.std(), 4))
print("\n")

line_sep()

#start plotting

#Plot group #1 Correlation Scatterplot with trendline
#create an array for each variable to find linear regression

Vs = np.array(df_vars['Volume'], dtype=np.float64)
Ps = np.array(df_vars['Average Price'], dtype=np.float64)
Cs = np.array(df_vars['CoronaCases'], dtype=np.float64)

#find slope and intercept for all variables correlations and linear regression
mVP, bVP = best_fit_slope_and_intercept1(Vs,Ps)
'''print(mVP,bVP)'''

mCP, bCP = best_fit_slope_and_intercept1(Cs,Ps)
'''print(mCP,bCP)'''

mCV, bCV = best_fit_slope_and_intercept1(Cs,Vs)
'''print(mCV,bCV)'''

#find regression line for each variable correlation
regression_lineVP = [(mVP*V)+bVP for V in Vs]
regression_lineCP = [(mCP*C)+bCP for C in Cs]
regression_lineCV = [(mCV*C)+bCV for C in Cs]

#plot scatter plots with lines of regression for all corelations:

#Volume and Average Price
df_vars[['Volume', 'Average Price']].plot(y='Average Price', x='Volume', kind='scatter')
plt.scatter(Vs, Ps)
plt.title('Volume Vs. Average Price')
plt.ylim(0, 1000)
plt.xlabel('Volume in Millions')
plt.plot(Vs, regression_lineVP)

#Coronavirus and Average Price
df_vars[['CoronaCases', 'Average Price']].plot(y='Average Price', x='CoronaCases', kind='scatter')
plt.scatter(Cs, Ps)
plt.title('COVID 19 Cases Vs. Average Price')
plt.ylim(0, 1000)
plt.plot(Cs, regression_lineCP)

#Coronavirus and Volume
df_vars[['CoronaCases', 'Volume']].plot(y='Volume', x='CoronaCases', kind='scatter')
plt.scatter(Cs, Vs)
plt.title('COVID 19 Cases Vs. Volume')
plt.plot(Cs, regression_lineCV)

#final plot : Date and Average Price

#create a dataframe of just Date and Price
df1= pd.DataFrame (date_and_price, columns = ['Date', 'Average Price'])
line_sep()

#plot with (x,y) of date and average price
ax = df1.plot(x='Date', y='Average Price')

#make labels
ax.set(title='Average Tesla Stock 2010-2020')
ax.set(xlabel='Years', ylabel='Mean Price')

#make intervals for x
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval = 2))

#set y range
plt.ylim(0, 1000)

#make grid
ax.grid(True)
plt.show()


'''plt.savefig('Average Tesla Stock graph 2010-2020.png')'''
plt.show()
#close matplotlib - so that the memory is released from the program before close
'''plt.close()'''

