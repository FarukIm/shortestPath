import pandas as pd
import queue 

names = pd.read_csv('cityName.csv')
edges = pd.read_csv('FromTo.csv')
left_node = []
right_node = []
adjecancy_list = []

for from_ID in edges['from_ID']:
    left_node.append(from_ID)

for to_ID in edges['to_ID']:
    right_node.append(to_ID)

def get_neighbours(id):
    neighbours = []
    for i in range(len(left_node)):
        if(left_node[i] == id):
            neighbours.append(right_node[i])
        elif(right_node[i] == id):
            neighbours.append(left_node[i])
    return neighbours

for City_ID in names['City_ID']:
    adjecancy_list.append([City_ID, get_neighbours(City_ID)])

def get_name(num):
    return names.query(f'City_ID == {num}')['Name']

def list_names(ids):
    result = []
    for i in ids:
        result.append(get_name(i))
    return result

def get_id(name):
    return names.query(f'Name == {name}')['City_ID']

def is_visited(id, nodes):
    for i in nodes:
        if i == id:
            return True
    return False

def get_distance(id, list):
    for i in list:
        if i[0] == id:
            return i[1]
    return print('Item not in list error')

def travel(a, b):
    start = get_id(a)
    end = get_id(b)
    distance = [[a, 0]]
    visited = []
    visited.append(a)
    result = queue.Queue()
    result.put(a)
    current = -1
    while current != end:
        
        current = result.get()

        for i in get_neighbours(current):
            if is_visited(i, visited) == True:
                continue
        
            distance.append([current, get_distance(current, distance) +1])
            result.put(current)
            visited.append(current)
    
    return get_distance(end, visited)

for i in adjecancy_list:
    print(i)
