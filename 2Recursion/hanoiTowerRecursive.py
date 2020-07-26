def hanoiTower(n, source, destination, spare):
    if n == 1:
        print(f'{source} -> {destination}')
    else:
        hanoiTower(n-1, source, spare, destination)
        hanoiTower(1, source, destination, spare)
        hanoiTower(n-1, spare, destination, source)

n = int(input())
hanoiTower(n, "A", "B", "C")