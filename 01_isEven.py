def isEven(num):
    return num&1 == 0

for i in range(10):
    print(i, isEven(i))