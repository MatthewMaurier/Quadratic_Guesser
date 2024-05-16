import numpy as np
import random as rand
import warnings
import matplotlib.pyplot as plt
import pandas as pd
import time
warnings.simplefilter('ignore', FutureWarning)


def XandYQuadValues(x1,x2,c):
# Calculate 'a' from the y-intercept and x-intercepts
    if x1 * x2 != 0:
        a = c / (x1 * x2)
    else:
        a = 1  # Default to 1 if x1 or x2 is zero to avoid division by zero
    
    # Define the range of x values to cover the extended plot
    x_min = -50 # Extending beyond the smallest intercept
    x_max = 50  # Extending beyond the largest intercept
    x = np.linspace(x_min, x_max, 500)
    
    # Calculate the corresponding y values based on the quadratic formula
    y = a * (x - x1) * (x - x2)

    return x,y,a

#RUN
t= time.time()
xydf = pd.DataFrame()
abcdf = pd.DataFrame()
x = pd.DataFrame([list([1,2,3])])

for i in range(0,1):
    x_int1 = rand.uniform(-25,25)
    x_int2 = rand.uniform(-25,25)
    factor = rand.uniform(-25,25)
    x,y,a = XandYQuadValues(x_int1,x_int2,factor)
    xdf = pd.DataFrame([list(x)])
    ydf = pd.DataFrame([list(y)])
    b = a*-(x_int1+x_int2)
    c = a*x_int1*x_int2
    
    if i == 0:
        xydf = pd.concat([xdf,ydf])
        abcdf = pd.DataFrame([[a, b, c]]) 
    else:
        xydf = pd.concat([xydf,ydf])
        abcdf = pd.concat([abcdf, pd.DataFrame([list([a, b, c])])])
    print(i)

    

xydf.to_csv('\\Users\\Matth\\OneDrive\\Desktop\\Summer\\Python\\Quadratic_Guesser\\xy_data.csv', index = False, header = False) #Paths Different for Everyone
abcdf.to_csv('\\Users\\Matth\\OneDrive\\Desktop\\Summer\\Python\\Quadratic_Guesser\\abc_data.csv', index = False, header = ['a', 'b', 'c']) 
print(f"{time.time()-t}s")