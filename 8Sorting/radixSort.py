target = [123, 2154, 222, 4, 283, 1560, 1061, 2150]

def stableSort(array, exponent):
    output = [0] * len(array)
    count = [0] * 10

    for i in range(len(array)):
        index = array[i] // exponent
        count[index % 10] += 1

    for i in range(10):
        count[i] += count[i-1]

    i = len(array) - 1
    while i >= 0:
        index = array[i] // exponent
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(array)):
        array[i] = output[i]


def radixSort(array):
    maximum = max(array)

    exponent = 1
    while maximum/exponent > 0:
        stableSort(array, exponent)
        exponent *= 10

radixSort(target)
print(target)