array = list(input('Enter your array: ').split())
a,b = input('Type in two elements that you want to swap: ').split()
indA = array.index(a)
indB = array.index(b)
array[indA], array[indB] = array[indB], array[indA]
for i in range(len(array)):
    print(array[i],end=' ')