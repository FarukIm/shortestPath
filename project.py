import pandas as pd
names = pd.read_csv('cityName.csv')
edges = pd.read_csv('FromTo.csv')
left_node = []
for from_ID in edges:
    left_node.append(edges[from_ID])

print(left_node)


def getName(num):
    return names.query(f'City_ID == {num}')['Name']

def listNames(ids):
    result = []
    for i in ids:
        result.append(getName(i))
    return result

def travel(a, b):
    ids = []
    count = 0
   