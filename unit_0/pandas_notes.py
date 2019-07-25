import pandas as pd
import numpy as np
# pandas is built on numpy, so it is helpful to import both, even if only using pandas


# a DataFrame is like a NumPy array, but with column names and row indexing
# Create a DataFrame from either csv files, by querying databases, or explicitly


# step 1: create a DataFrame
my_array = np.array([['Montgomery','Yellohammer state',52423],
                     ['Sacramento','Golden state',163707],
                     ['Oklahoma City','Sooner state',69960 ]])
# first, create a numpy array
df = pd.DataFrame(my_array)
# convert array to DF with pandas pd.DataFrame() func
print(df)


# The DataFrame rows and columns are nameable
# Columns are labeled with names, rows with an index number (starting at 0)
# You can set both column names and row indexes explicitly during the creation of the DF or after
df.columns = ['Capital', 'Nickname','Area']
# Use .columns method on DF to set the column names with a list of strings
df.index = ['Alabama', 'California', 'Oklahoma']
# Use .index method on DF to set row indexes, either pass a list of strings or integers
print(df)


# To set the column and index labels of a DF during creation,
# Pass the arguments columns and index to the pd.to_DataFrame() func
col_list = ['Capital', 'Nickname','Area']
index_list = ['Alabama', 'California', 'Oklahoma']
df2 = pd.DataFrame(my_array, columns = col_list, index = index_list)
# Pass the array, a list of column names and a list of row labels
print(df2)


# It is possible to add data to a DataFrame after creating it
names = ['George', 'John', 'Thomas', 'James', 'Andrew', 'Martin', 'William', 'Zachary', 'Millard', 'Franklin']
# This list will become our row names.
purchases = pd.DataFrame(index=names)
# Create an empty data frame with named rows.
purchases['country'] = ['US', 'CAN', 'CAN', 'US', 'CAN', 'US', 'US', 'US', 'CAN', 'US']
purchases['ad_views'] = [16, 42, 32, 13, 63, 19, 65, 23, 16, 77]
purchases['items_purchased'] = [2, 1, 0, 8, 0, 5, 7, 3, 0, 5]
# Add our columns to the data frame one at a time.
print(purchases)


# We can access data from a DF using either bracket [] or dot . notation
# df.column_name or df['column_name'] both work
print(purchases.name)
print(purchases['name'])
# Both lines will return the same info


# Pandas also makes it very easy to create a new column out of existing data
purchases['items_purch_per_ad'] = purchases['items_purchased'] / purchases['ad_views']
# This will create a new column 'items_purch_per_ad'
# Pandas will fill the column will data from 'items_purchased' and 'ad_views'
print(purchases)


# Locating, slicing, and subsetting data
purchases['country']
# this will return all data from the 'country' column, with the DF column names and row indexes
# if we want to more precisely access data, use .loc and iloc methods
# .loc (or label indexing) will select data over the row index first, then column name
# .iloc (or integer indexing) will select data over column names then row indexes 
# that is, .loc is label (string) based and .iloc is index (number) based

print(purchases.loc['George'])
# this will return all data across the row indexed 'George'
print(purchases.loc[:, 'country'])
# the semicolon will return data from all row indexes sliced by the 'country' column
# in other words, this notation will return the entire 'country' column
print(purchases['George', 'country']
# this will return the entire row indexed 'George' subset by the 'country' column
# in other words, this will only return the 'country' data from the 'George' row

print(purchases.iloc[1:3, 1])
# this will return all data from rows 2-3 sliced by column 2
# this can get a little confusing because python uses zero indexing
# to add to that confusion, python notation 1:3 specifies UP TO BUT NOT INCLUDING the last number
# therefore 1:3 will start slicing at the second row (index 0 being the first) and include UP TO the third row (which is indexed as 2)
# functionally this is the same as purchases.loc['John':'James', 'ad_views']
print(purchases.iloc[0, :])
# this will return all data across all columns of the first index
# functionally the same as purchases['George'] or purchases.loc['George']
print(purchases.iloc[:, 0])
# this will return all data from all rows sliced the first column
# functionally the same as purchase.loc[:, 'country']
print(purchases.iloc[0,0])
# this will return the data from the first row sliced by the first column
# functionally the same as purchases.loc['George','Country']


# it's possible to slice dataframes in many other ways
purchases.loc[lambda df: purchases['items_purchased'] > 1, :]
# using .loc and lambda, we can select all entries from the 'items_purchased' column that are greater than 1
# this will select all rows where 'items_purchased' > 1, then return data from all columns of the rows selected
# lambda functions are useful for quickly defining a function in the moment
# ex: x=lambda a,b: a ** b
# passing x(4,2) will return 16 or 4 ** 2
      
# it is possible to index DF w/ boolean logic
purchases[purchases['items_purchased'] > 1]
# this will return the same results as the lambda function above
# boolean indexing ins't as robust as explicit indexing (such as the lambda function)
      
# grouping data in a DF is a great way to analyze data
purchases.groupby('country').sum()
# the .groupby() method must have a parameter passed to it by which to index the DF
# then it must also have a way to group the date specified. in this case, the .sum() method
purchases.groupby('country').aggregate(np.mean)
# it's possible to utilize NumPy to create very sophisticated ways to group and view data


# importing files into python
df = pd.read_csv(r'c:\users\aaron\appdata\local\programs\python\python37\purchases.csv')
# create a DataFrame with pd.read_csv('filename')
# pass filename and location to the function to create a DataFrame
# in the case above pd.read_csv(r... ) the 'r' is a special character and means carriage return
# prefix it to your string literal if you are having trouble importing the file

# converting data back to a csv file
df.to_csv('my_data.csv')
# this will save the DataFrame 'df' to a csv file 'my_data'
# if you skip the filepath ('my_data') .to_csv will return a single string containing all the data that you can copy/paste elsewhere
 

# json files are similar to csv files, but with more structure
# they are human-readable out of the box, though some may be too large to fit in your local computer memory
# json files are a series of key-value pairs, just like python dictionaries
# json stands for "javascript object notation" but with python, we can intrept it as "python dictionary notation"
df = pd.read_json('purchase.json')
# import a json file into python with pandas .read_json() method and pass it the filename

df.to_json('my_data.json')
# just like outputting a csv file, python can easily save and output a json file
# more commonly json files are sent via the web
df_string = df.to_json()
# the do that, pass .to_json() without a path argument and store as a string

# xml is a heirarchical semi-structured data format, like json
# both are used to transdata over the web, but the newer json is more common
import xml.etree.ElementTree as ET
# to read xml files with python import xml module 
# convert xml file to an element tree then manually process it into a list to feed into Pandas

tree = ET.parse('purchases.xml')
# Load and parse the XML file into a tree
root = tree.getroot()
# Find the root of the tree. This is the node of the tree where we'll start our iteration
def xml_to_list(root):
    result = []
    for row in root:
        row_list = []
        for column in row:
            row_list.append(column.text)
        result.append(row_list)
    return result
# Define a function to loop over our tree, extract values, and return a two-dimensional list
df = pandas.DataFrame(xml_to_list(root))
# Feed our two-dimensional list into Pandas and view.
print(df)

# NOTE: The custom xml_to_list() function is designed for the specific XML file we're working with
# If you're working with differently structured XML, you'll need to iterate over your XML tree differently

# python has a native function to access files
# the built-in open() function is a more general way to open any files
# to open the poem.txt file, create a file object, and print out the file text line by line
with open('poem.txt') as poem_file:
    text = poem_file.readlines()
    print("This file is {} lines long".format(len(text)))
    for line in text:
        print(line)
# use the open() function to create a file object
# use .readlines() method of the file object to create list of strings
# each element of the list is a line of text from our file

# Opening a file with open() will leave it open until you close it
# use the .close() file object method to close a file
# It's easy to forget to manually close files, which can keep resources tied up and cause unexpected trouble
# Luckily, the with statement you see used above so we doesn't require us to have to remember to use .close()
# files opened in a with statement will automatically be closed once the with statement exits

