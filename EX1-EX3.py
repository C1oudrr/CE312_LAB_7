global array
array = [10,9,8,7,6,4,5,2,3,1,11,12,13,15,18,80]

def Bubblesort():
    print("Bubblesort")
    print("Unsorted Array =", array)
    max = len(array)
    for i in range(max - 1):
        for j in range(max - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    print("Sorted Array =", array)
    return inputnumber()

def Selectionsort():
    print("Selectionsort")
    print("Unsorted Array =", array)
    max = len(array)
    for i in range(max):
        for j in range(i + 1, max):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print("Sorted Array =", array)
    return inputnumber()
def InsertionSort():
    print("InsertionSort")
    print("Unsorted Array =", array)
    max = len(array)
    for i in range(max):
        for j in range(0, i):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print("Sorted Array =", array)
    return inputnumber()
def inputnumber():
    while (True):
        print(array)
        i = int(input("Enter Input 1-3 For sorting algorithm 0 to Exit: "))
        if(i == 1):
            return Bubblesort()
        if(i == 2):
            return Selectionsort()
        if (i == 3):
            return InsertionSort()
        if (i == 0):
            print("Exit...")
            break
        else:
            print("Wrong Input !!?")
            return inputnumber()
inputnumber()