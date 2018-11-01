#Pandas library helps with importing datasets , working with series, dataframes

import pandas as pd
import numpy as np

from pandas import Series, DataFrame
# Series and Data Frame are two data structures available in python

series_a= Series([5,4,3,2,1])# a simple series
print(series_a)        # A series is represented by index on the left and values on the right
print(series_a.values) # similar to dictionary. ".values" command returns values in a series
print (series_a.index) # returns the index values of the series


# series_b = Series([5,4,3,2,1,-7,-29], index =['a','b','c','d','e','f','h']) # The index is specified
# print (series_b) # try series_b.index and series_b.values
# print (series_b['a']) # selecting a particular value from a Series, by using index
#
# series_b['d'] = 9 # change the value of a particular element in series
# print (series_b)
# series_b ([['a','b','c']]) # select a group of values
#
# print (series_b[series_b>0]) # returns only the positive values
# print (series_b *2) # multiplies 2 to each element of a series
#
# np.mean(series_b) # you can apply numpy functions to a Series
#
# print ('b' in series_b) # checks whether the index is present in Series or not
# print ('z' in series_b)
#
# player_salary ={'Rooney': 50000, 'Messi': 75000, 'Ronaldo': 85000, 'Fabregas':40000, 'Van persie': 67000}
# new_player = Series(player_salary)# converting a dictionary to a series 
# print (new_player) # the series has keys of a dictionary
#
# players =['Klose', 'Messi', 'Ronaldo', 'Van persie', 'Ballack']
# player_1 =Series(player_salary, index= players)
# print (player_1) # Changed the index of the Series. Since, no value was not found for Klose and Ballack, it appears as NAN
#
# pd.isnull(player_1)#checks for Null values in player_1, pd denotes a pandas dataframe
#
# pd.notnull(player_1)# Checks for null values that are not Null
#
# player_1.name ='Bundesliga players' # name for the Series
# player_1.index.name='Player names' #name of the index
# print(player_1)
#
# player_1.index =['Neymar', 'Hulk', 'Pirlo', 'Buffon', 'Anderson'] # is used to alter the index of Series
# print(player_1)
#
#
# #Data_frames
# states ={'State' :['Kaduna', ' Lagos', 'Kano', 'Plateau', 'Zamfara'],
#                   'Population': [360, 4400, 6798,8987,3400],
#                   'Language' :['Hausa', 'Yoruba', 'Berom', 'Kagoro', 'Igbo']}
# nigeria = DataFrame(states) # creating a data frame
# print(nigeria)
#
# DataFrame(states, columns=['State', 'Language', 'Population']) # change the sequence of column index
#
# new_frame = DataFrame(states, columns=['State', 'Language', 'Population', 'Per Capita Income'], index =['a','b','c','d','e'])
# #if you pass a column that isnt in states, it will appear with Na values
#
# print (new_frame.columns)
# print (new_frame['State'] )# retrieveing data like dictionary
#
# new_frame.Population # like Series
#
# new_frame.ix[3] # rows can be retrieved using .ic function
# # here I have retrieved 3rd row
#
# print(new_frame)
#
# new_frame['Per Capita Income'] = 99 # the empty per capita income column can be assigned a value
# print(new_frame)
#
# new_frame['Per Capita Income'] = np.arange(5) # assigning a value to the last column
# print(new_frame)
#
# series = Series([44,33,22], index =['b','c','d'])
# new_frame['Per Capita Income'] = series
#
# #when assigning list or arrays to a column, the values lenght should match the length of the DataFrame
# print(new_frame)
# # again the missing values are displayed as NAN
#
# new_frame['Development'] = new_frame.State == 'Kaduna'# assigning a new column
# print (new_frame)
# del new_frame['Development'] # will delete the column 'Development'
# print(new_frame)
#
# new_data ={'Enugu': {2010: 72, 2012: 78, 2014 : 98},'Borno': {2010: 55, 2012: 34, 2014: 22}}
# elections = DataFrame(new_data)
# print (elections)# the outer dict keys are columns and inner dict keys are rows
# elections.T # transpose of a data frame
#
# DataFrame(new_data, index =[2012, 2014, 2016]) # you can assign index for the data frame
#
# ex= {'Kaduna':elections['Zamfara'][:-1], 'Nigeria': elections['Borno'][:2]}
# px =DataFrame(ex)
# px
#
# px.index.name = 'year'
# px.columns.name = 'politicians'
# print(px)
#
# print(px.values)
#
# series_c = Series([5,4,3,2,1,-7,-29], index =['a','b','c','d','e','f','h'])
# index = series_c.index
# print (index) #u denotes unicode
# print (index[1:])# returns all the index elements except a.
# index[1] = 'f' # you cannot modify an index element. It will generate an error. In other words, they are immutable
#
# print (px)
# print(2013 in px.index) # checks if 2003 is an index in data frame px
#
# var = Series(['Python', 'Java', 'c', 'c++', 'Php'], index =[5,4,3,2,1])
# print (var)
# var1 = var.reindex([1,2,3,4,5])# reindex creates a new object
# print (var1)
#
# var.reindex([1,2,3,4,5,6,7])# introduces new indexes with values Nan
#
# var.reindex([1,2,3,4,5,6,7], fill_value =1) # you can use fill value to fill the Nan values. Here I have used fill value as 1. You can use any value.
#
# series_d =Series(['Ibadan', 'Nassarawa', 'Borno'], index =[0,2,4])
# print (series_d)
# series_d.reindex(range(6), method ='ffill') #ffill is forward fill. It forward fills the values
#
# series_d.reindex(range(6), method ='bfill')# bfill, backward fills the values
#
#
# reshape = DataFrame(np.arange(9).reshape((3,3)),index =['a','b','c'], columns =['Ibadan','Nassarawa', 'Borno'])
# print(reshape)
#
# reshape_2 =reshape.reindex(['a', 'b', 'c', 'd'], columns = states) # reindexing columns and indices
# print(reshape)
#
# series_e = Series(np.arange(5), index =['a','b','c','d','e'])
# print (series_e)
# series_e.drop(['a','b']) #drop method will return a new object  with values deleted from an axis
#
# states ={'State' :['Kaduna', 'Enugu', 'Nassarawa', 'lagos', 'Borno'],
#                   'Population': [306, 944, 9867,899,340],
#                   'Language' :['kagoro', 'Igbo', 'Margi', 'Kurama', 'Yoruba']}
# nigeria = DataFrame(states, columns =['State', 'Population', 'Language'])
# print (nigeria)
# nigeria.drop([0,1])# will drop index 0 and 1
#
# nigeria.drop(['State', 'Population'], axis =1 )# the function dropped population and state columns. Apply the same concept with axis =0
#
# series_f = Series(['Python', 'Java', 'c', 'c++', 'Php'], index =[5,4,3,2,1])
# print(series_f)
#
# print(series_f[5])
# print(series_f[2:4])
#
# print(series_f[[3,2,1]])
#
# print(var[var == 'Php'])
#
# states ={'State' :['Kaduna', 'Enugu', 'Nassarawa', 'lagos', 'Borno'],
#                   'Population': [306, 944, 9867,899,340],
#                   'Language' :['kagoro', 'Igbo', 'Margi', 'Kurama', 'Yoruba']}
# nigeria = DataFrame(states, columns =['State', 'Population', 'Language'])
# print(nigeria)
#
# print(nigeria[['Population', 'Language']]) # retrieve data from data frame
#
# print(nigeria[nigeria['Population'] > 50]) # returns data for population greater than 50
#
# print(nigeria[:3]) # first three rows
#
# # for selecting specific rows and columns, you can use ix function
# states ={'State' :['Kaduna', 'Enugu', 'Nassarawa', 'lagos', 'Borno'],
#                   'Population': [306, 944, 9867,899,340],
#                   'Language' :['kagoro', 'Igbo', 'Margi', 'Kurama', 'Yoruba']}
# nigeria = DataFrame(states, columns =['State', 'Population', 'Language'])
# print(nigeria)
#
# print(nigeria.ix[['a','b'], ['State','Language']]) # this is how you select subset of rows
