import pandas as pd
names = pd.read_csv('cityName.csv')
edges = pd.read_csv('FromTo.csv')
left_node = []
right_node = []

for from_ID in edges['from_ID']:
    left_node.append(from_ID)

for to_ID in edges['to_ID']:
    right_node.append(to_ID)
     
def get_name(num):
    return names.query(f'City_ID == {num}')['Name']

def list_names(ids):
    result = []
    for i in ids:
        result.append(get_name(i))
    return result

def get_id(name):
    return names.query(f'Name == {name}')['City_ID']

def travel(a, b):
    start = get_id(a)
    end = get_id(b)

