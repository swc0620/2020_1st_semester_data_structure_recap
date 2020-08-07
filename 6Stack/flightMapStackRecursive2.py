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
        adjacentCities = adjacencyList[originCity]
        for city in adjacentCities:
            if mark[city] != True and searchS(city, destinationCity) == True:
                return True
        return False

originCity, destinationCity = input().split()
print(searchS(originCity, destinationCity))