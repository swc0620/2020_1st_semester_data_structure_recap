def writeBackward(inputString):
    if inputString == "":
        return 
    else:
        print(inputString[len(inputString) - 1], end="")
        writeBackward(inputString[:len(inputString) - 1])

inputString = input()
writeBackward(inputString)