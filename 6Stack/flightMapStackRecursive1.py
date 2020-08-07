adjacencyList = {
    'Z': [], 
    'Y': ['Z', 'R'],
    'W': ['Y', 'S'],
    'S': ['T'],
    'T': ['W'],
    'P': ['W', 'R'],
    'R': ['X'],
    'X': [],
    'Q': ['X']
}

mark = {
    'Z': False,
    'Y': False,
    'W': False,
    'S': False,
    'T': False,
    'P': False,
    'R': False,
    'X': False,
    'Q': False
}

def searchS(originCity, destinationCity):
    if originCity == destinationCity:
        return True
    else:
        mark[originCity] = True
        arrived = False
        adjacentCities = adjacencyList[originCity]
        for city in adjacentCities:
            if mark[city] != True:
                arrived = searchS(city, destinationCity)
                if arrived == True:
                    return True
        return False

originCity, destinationCity = input().split()
print(searchS(originCity, destinationCity))