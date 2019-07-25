import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import numpy and pandas
# pandas is built on numpy, so it is helpful to import both, even if only using pandas


plt.plot([0, 1, 2, 3])
# returns a plot object

# matplotlib will not show plot object without calling plt.show()
plt.show()

# always use the magic " %matplotlib inline " in your first cell when working with Jupyter notebooks
# This makes sure your images will always generate in the notebook instead of as popups and rendering errors from slow compilations

%matplotlib inline
plt.plot([0, 1, 2, 3])
plt.show()
# this will now plot without error in jupyter notebooks


# make the random function consistent and replicable
# use NumPy's random.seed() func to set the random seed value
np.random.seed(666)

# initialize an empty dataframe
df = pd.DataFrame()

# add a column of random numbers between 0 and 100
df['rand'] = np.random.rand(100)
# square 'rand' column
df['rand_sq'] = df['rand'] ** 2
# shift 'rand' column values by 2
df['rand_shift'] = df['rand'] + 2

# when initializing a data frame an index column of counts in created, counting from 0
# transform that index to create some extra columns
# square index and store as 'counts_sq'
df['counts_sq'] = df.index ** 2
# get square root of index and store as 'counts_sqrt'
df['counts_sqrt'] = np.sqrt(df.index) 
