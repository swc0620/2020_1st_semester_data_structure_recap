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

stack = []
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
    stack.append(originCity)
    mark[originCity] = True

    while stack and stack[len(stack) - 1] != destinationCity:
        adjacentCities = adjacencyList[stack[len(stack) - 1]]
        if not adjacentCities:
            temp = stack.pop()
        else:
            mark[adjacentCities[len(adjacentCities) - 1]] = True
            stack.append(adjacentCities[len(adjacentCities) - 1])
            adjacentCities.pop()
        # print(stack)
    
    if stack:
        return True
    else:
        return False

originCity, destinationCity = input().split()
print(searchS(originCity, destinationCity))