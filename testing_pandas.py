from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series([4, 7, -5, 3])
#print(obj)

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
#print('z' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
#print(obj3)

states = ['california', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4.name = 'Population'
obj4.index.name = 'state'
#print(obj4)
#print(pd.notnull(obj4))
#print(obj3 + obj4)

# DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                                 index=['1', '2', '3', '4', '5'])
#print(frame2)
frame2['debt'] = np.arange(5)
#print(frame2)

val = Series([-1.2, -1.5, -1.7], index=['2', '4', '5'])
frame2['debt'] = val

frame2['eastern'] = frame2.state == 'Nevada'
del frame2['eastern']

#print(frame2.columns)
#print(frame2.values)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
#print(frame3)
#print(frame3.T)

#frame3 = DataFrame(pop, index=[2001, 2002, 2003])

frame3.index.name = 'year'; frame3.columns.name = 'state'

#print(frame3)
#print(frame3.values)

#pdata = {'Ohio': frame3['Ohio'][:-1],
#         'Nevada': frame3['Nevada'][:2]}
#print(DataFrame(pdata))


# TESTING OBJECTS

obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
#print(index)
#print(index[1:])

index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
#print(obj2.index is index)

#print('Ohio' in frame3.columns)
#print(2003 in frame3.index) 

# REINDEXING

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=0)
#print(obj2)

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
#print(obj3.reindex(range(6), method='ffill'))

frame = DataFrame(np.arange(9).reshape((3, 3)),
                  index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
#print(frame)

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
#print(frame2)

states = ['Texas', 'Utah', 'California']
#print(frame.reindex(columns=states))
#print(frame.reindex(index=['a', 'b', 'c', 'd'], columns=states))
#print(frame.loc[['a', 'b', 'c', 'd'], states])

# .drop()

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
#print(obj)
new_obj = obj.drop('c')
#print(new_obj)

data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data.index.name = 'ChodBhangra'
data.columns.name = 'Bhangbosda'
#print(data.drop(['Ohio', 'Colorado']))
#print(data.drop('two', axis=1))


# INDEXING, SELECTION, AND FILTERING

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])