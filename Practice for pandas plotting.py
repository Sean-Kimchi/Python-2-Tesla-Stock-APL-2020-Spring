import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import (MultipleLocator)


'''Making a dataframe and plotting dummy integer data by converting the data
with pandas dataframe'''
##
##data= {'Date':  [5, 10, 15, 20],
##        'Price': [10, 100, 90, 45],
##        }
##df = pd.DataFrame(data, columns = ['Date', 'Price'])
##print(df)
##
##ax = df.plot(x='Date', y='Price')
##plt.show()



'''Making a dataframe and plotting dummy string data by converting the data
to datatime using numpy datatime and pandas dataframe.
Then setting the ticks for the x-axis'''
##data= {'Date':  [np.datetime64('2018-01-02'), np.datetime64('2018-01-03'), np.datetime64('2018-01-04'), np.datetime64('2018-05-12')],
##        'Price': [10, 100, 90, 45],
##        }
##
##df = pd.DataFrame (data, columns = ['Date','Price'])
##
##print(df)
##
##ax = df.plot(x='Date', y='Price')
##ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 2))
###ax.xaxis.set_minor_locator(mdates.MonthLocator())
##plt.show()

