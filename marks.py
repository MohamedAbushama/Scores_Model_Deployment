
from telnetlib import X3PAD
import pandas as pd 
import numpy as np

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def marks_prediction(hrs):

    df = pd.read_csv('student_scores.csv')

    # Defining X, y 
    X = df.iloc[:,:-1].values  #independent variable array
    y = df.iloc[:,1].values 
 # defining x_test as hrs function and reshape it 
    x_test = np.array(hrs)
    x_test = x_test.reshape((1,-1))

# create a regressor mobject 
    reg_mod = LinearRegression()
#Fitting the model
    reg_mod.fit(X,y)
    
# Y prtediction 
    reg_mod.predict(x_test)

# create a pipeline for the regressor after applying degree 3 polynomial on the model 

#     poly_mod = make_pipeline(PolynomialFeatures(degree=3),LinearRegression(fit_intercept=False))
# # Fitting the model 

#     poly_mod.fit(X,y)
# # new prediction variable
    
    return reg_mod.predict(x_test)[0]


