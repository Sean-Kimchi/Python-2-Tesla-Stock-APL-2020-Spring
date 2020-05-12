import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import os

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


#Create one printable line seperator
def line_sep():
    print('____________________________________________________________________________')
    print("\n")


#read dataset with pandas
data = pd.read_csv('All_Data.csv')

#converting date collumn to datetime format
data['Date'] = pd.to_datetime(data['Date']) #or use np.datetime64 in a loop
#print raw dataset
def Data_Open():
    print('Full, Raw Dataset')
    line_sep()
    print(data)
    line_sep()
Data_Open()


#print dataset of just date and average price
date_and_price = data[['Date','Average Price', 'year']]

print("Date and price")
print(date_and_price)
line_sep()

#Singular parts
print('Dates')
dates = date_and_price[['Date']].values
print(dates)
line_sep()

#Print Years    
#print('Years')
years = date_and_price[['year']].values
print(years)
line_sep()

#Print Average Stock Price
print('Average Stock Price')
avgprice = date_and_price[['Average Price']].values
print(avgprice)
line_sep()

#Print Unique Years
print('Different years')
all_years = date_and_price['year'].unique()
print(all_years)
line_sep()
line_sep()

# Start the analysis

# aggreate the data based on year
#make seperate dataset with only year and VOlume
date_and_volume = data[['year', 'Volume']]

#print Volume data
print('Volume per year\n')
print(date_and_volume)
line_sep()

# create a new dataframe from year and agg of Tesla VOlume
def T_Volume_stats():
    print('Volume stats per year\n')
    year_grouped_data = date_and_volume.groupby('year').agg({'Volume': ['mean', 'min', 'max']})
    print(year_grouped_data)
    line_sep()
T_Volume_stats()










#plot

#create a dataframe of just Date and Price
df1= pd.DataFrame (date_and_price, columns = ['Date', 'Average Price'])
print("Date and Price Dataframe")
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

#save graph
plt.savefig('Average Tesla Stock graph 2010-2020.png')
plt.show()
#close matplotlib - so that the memory is released from the program before close
plt.close()

