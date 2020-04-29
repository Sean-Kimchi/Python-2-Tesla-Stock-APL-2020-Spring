import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
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


def Raw_stock_scatter():
    

    
    #plot
    print('Dates')
    dates = date_and_price[['Date']].values
    print(dates)
    line_sep()
    
    print('Years')
    years = date_and_price[['year']].values
    print(years)
    line_sep()

    print('Average Stock Price')
    avgprice = date_and_price[['Average Price']].values
    print(avgprice)
    line_sep()

    print('Different years')
    all_years = date_and_price['year'].unique()
    print(all_years)
    line_sep()
    line_sep()
    
    #list comprehension to aggregate the data
    plot_list = [[i, avgprice[years==i].mean()] for i in all_years]

    #creating the graph by looping through the data
    

    fig, ax = mp.subplots(figsize=(12,10))
    for plot in plot_list:
        mp.scatter(date_and_price['Date'], date_and_price['Average Price'])

    ax.set(title='Average Tesla Stock 2010-2020')
    ax.set(xlabel='year-month', ylabel='mean price')
    mp.ylim(0, 1000)
    mp.xticks(all_years)
    ax.get_xscale
    mp.show()
    '''mp.savefig('Average_Tesla_Stock_Scatter_Plot.png')'''
    
    #close matplotlib - so that the memory is released from the program before close
    mp.close()
    
Raw_stock_scatter()
   



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




