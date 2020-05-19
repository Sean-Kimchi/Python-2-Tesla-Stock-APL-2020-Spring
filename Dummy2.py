from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('All_Data.csv')
Vs = np.array(data['Volume'], dtype=np.float64)
Ps = np.array(data['Average Price'], dtype=np.float64)
Cs = np.array(data['CoronaCases'], dtype=np.float64)

##def best_fit_slope_and_intercept1(xval, yval):
##    m = (((mean(xval)*mean(yval)) - mean(xval*yval)) /
##         ((mean(xval)*mean(yval)) - mean(xval*xval)))
##    
##    b = mean(yval) - m*mean(xval)
##    
##    return m, b
##
##m, b = best_fit_slope_and_intercept1(Vs,Ps)
##
##print(m,b)
##
##regression_line = [(m*V)+b for V in Vs]
##
##plt.scatter(Vs, Ps)
##plt.title('Parameters')
##plt.plot(Vs, regression_line)
##plt.show()


def best_fit_slope_and_intercept1(xval, yval):
    m = (((mean(xval)*mean(yval)) - mean(xval*yval)) /
         ((mean(xval)*mean(yval)) - mean(xval*xval)))
    
    b = mean(yval) - m*mean(xval)
    
    return m, b

#find slope and intercept for all variables correlations and linear regression
mVP, bVP = best_fit_slope_and_intercept1(Vs,Ps)
print(mVP,bVP)

mCP, bCP = best_fit_slope_and_intercept1(Cs,Ps)
print(mCP,bCP)

mCV, bCV = best_fit_slope_and_intercept1(Cs,Vs)
print(mCV,bCV)

#find regression line for each variable correlation
regression_lineVP = [(mVP*V)+bVP for V in Vs]
regression_lineCP = [(mCP*C)+bCP for C in Cs]
regression_lineCV = [(mCV*C)+bCV for C in Cs]

#plot scatter plots with lines of regression for all corelations
#Volume and Average Price
plt.scatter(Vs, Ps)
plt.title('Volume Vs. Average Price')
plt.plot(Vs, regression_lineVP)

plt.show()
