import numpy as np
import random as rand
import warnings
import matplotlib.pyplot as plt
import pandas as pd
import time
warnings.simplefilter('ignore', FutureWarning)

t= time.time()
xydf = pd.DataFrame()
abcdf = pd.DataFrame()
x = pd.DataFrame([list([1,2,3])])

for i in range(0,100000):
    x = np.linspace(-50, 50, 500)
    a = rand.uniform(-25,25)
    b = rand.uniform(-25,25)
    c = rand.uniform(-25,25)
    y = a*x**2+b*x+c
    xdf = pd.DataFrame([list(x)])
    ydf = pd.DataFrame([list(y)])
    if i == 0:
        xydf = pd.concat([xdf,ydf])
        abcdf = pd.DataFrame([[a, b, c]]) 
    else:
        xydf = pd.concat([xydf,ydf])
        abcdf = pd.concat([abcdf, pd.DataFrame([list([a, b, c])])])

    

xydf.to_csv('\\Users\\Matth\\OneDrive\\Desktop\\Summer\\Python\\Quadratic_Guesser\\xy_data_rand.csv', index = False, header = False) #Paths Different for Everyone
abcdf.to_csv('\\Users\\Matth\\OneDrive\\Desktop\\Summer\\Python\\Quadratic_Guesser\\abc_data_rand.csv', index = False, header = ['a', 'b', 'c']) 
print(f"{time.time()-t}s")