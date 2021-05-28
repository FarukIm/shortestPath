import pandas as pd
names = pd.read_csv('cityName.csv')
edges = pd.read_csv('FromTo.csv')

def getName(num):
    return names.query(f'City_ID == {num}')['Name']

def listNames(ids):
    result = []
    for i in ids:
        result.append(getName(i))
    return result

print(listNames([1,2,3,4,5,6,10]))
