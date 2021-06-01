#@Author: Faruk Imamovic
#@Student_ID: 190302086
#International University of Sarajevo
#MATH209 Project 2

#imports pandas, used for data manipulation,
#I've used pandas library over the csv library because I found it easier to work with
import pandas as pd
#imports queue, enables working with queues
import queue 
#read both of the csvs into lists
names = pd.read_csv('cityName.csv')
edges = pd.read_csv('FromTo.csv')
#declare left_node as global variable, it will store the first column
#of FromTo.csv
left_node = []

#declare right_node as global variable, it will store the second column 
#of FromTo.csv
right_node = []

#adjecancy_list is a global variable, which stores city_id and list of all
#adjacent nodes to the specific city_id
adjecancy_list = []

#populates left_node
for from_ID in edges['from_ID']:
    left_node.append(from_ID)

#populates right_node
for to_ID in edges['to_ID']:
    right_node.append(to_ID)

#input: city_id
#returns: list of all adjacent city_id's to the inputted city_id
def get_neighbours(city_id):
    neighbours = []
    for i in range(len(left_node)):
        if(left_node[i] == city_id):
            neighbours.append(right_node[i])
        elif(right_node[i] == city_id):
            neighbours.append(left_node[i])
    return neighbours

#populates adjecancy_list
for City_ID in names['City_ID']:
    adjecancy_list.append([City_ID, get_neighbours(City_ID)])

#input: city id
#returns: name of city
def get_name(num):
    return names.loc[names['City_ID'] == num, 'Name'].item()

#input: name of city
#returns: city id
def get_id(name):
    return names.loc[names['Name'] == name, 'City_ID'].item()

#input: city_id, visited_cities
#returns: True if city_id is in visited_vities, else fFalse
def is_visited(city_id, visited_cities):
    for i in visited_cities:
        if i == city_id:
            return True
    return False

#input: city_id, list
#returns: returns distance of city_id from first city, throws exception otherwise
def get_distance(city_id, list):
    try:
        for i in list:
            if i[0] == city_id:
                return i[2]
    except: 
        print('Item not in list error')

#Here I've used the breadth first search algorithm
#input: starting city, destination city
#returns: list of all cities visited andtheir distance from starting city
def travel(a, b):
    #get id of starting city
    start = get_id(a)
    #get id of destination city
    end = get_id(b)
    #initialize distance, the elements are[city_id, parent_city_id, distance from start]
    distance = [[start, start, 0]]
    #initialize list of visited cities
    visited = []
    #add starting city to visited[]
    visited.append(start)
    #result queue will store which nodes we have to visit next
    result = queue.Queue()
    #add starting city id to result
    result.put(start)
    #the while loop goes on until we visit the destination city
    while visited[-1] != end:
        #get function removes the first item from the queue and returns it
        #@current is the node which we are itterating
        current = result.get()
        #initialize adjacent as a list of all adjacent cities to the @current variable
        adjacent = [y for (x, y) in adjecancy_list if x == current]
        #since @adjacent is of the form [item,[items]] when we get the adjacent cities
        # we get [[items]] so we need to itterate over @adjacent[0] to itterate through
        #list of list
        for i in adjacent[0]:
            #if node is visited move to next itteration of loop
            if is_visited(i, visited) == True:
                continue
            #append i, current(parent city), distance of previous node from start + 1
            distance.append([i, current, get_distance(current, distance) + 1])
            #add i to queue so we can traverse it's adjacent nodes
            result.put(i)
            #add i to visited so we don't visit it again
            visited.append(i)
            #break from for loop if i is our destination city
            if(i == end):
                break
    #return distance variable which contains[city_id, parent_city_id, distance_from_start]
    return distance

#input: distance list we get from travel function, end node
#returns: path from start node to end node including [city_ID, city_Name]
def get_path(list, b):
    #initialize list of [city_ID, city_Name]
    names = []
    #add destination city id and name to names
    names.append([b, get_name(b)])
    #initialize @previous which contains informations of last city's parent_city
    previous = list[-1][1]
    #traverse list in reverse so we can track which node is next based on parent_city
    for i in reversed(list):
        #if i is the last item of our list we skip
        if i == list[-1]:
            continue
        #if i is equal to the previous city's parent 
        if i[0] == previous:
            #add i city_id and city_name to @names
            names.append([i[0], get_name(i[0])])
            #update @previous to the parent_city of i
            previous = i[1]

    names.reverse()
    return names

more = 'y'
while more == 'y':
    first = input("Please enter the starting city: ")
    last = input("Please enter the destination city: ")

    distances = travel(first, last)
    last_id = get_id(last)

    print(f'The distance from {first} to {last} is: {distances[-1][2]}')
    print('The order in which the cities are visited is(City_ID, Name): ')

    for i in get_path(distances, last_id):
        print(i)

    more = input("Please enter 'y' if you want to run this program once more, else enter anything else: ")

