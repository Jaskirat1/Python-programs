import pandas as pd

#create a dataframe 
a = pd.DataFrame()

dict = {
    'id': [1,2,3],
    'val': ['a','b','c']

}

a = pd.DataFrame(dict)
print(a)

#another dataframe

b = pd.DataFrame()

dict2 = { 
    'id':[4,2,6],
    'val':['d','e','f']
}

b = pd.DataFrame(dict2)

print(b)

#inner join
""" inner join will returns a dataframe with only those rows that have common charateristics."""
"""this is similar to intersection of two sets."""

ij = pd.merge(a, b, on='id', how='inner')

print(ij)