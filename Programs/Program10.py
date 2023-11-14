def linearSearch(array, n, x):

    for i in range(0, n):
        if (array[i] == x):
            return i


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        elif array[mid] > x:
            high = mid - 1

        else:
            print("Key not found\n")

    return -1


arr = [10, 20, 30, 40, 50, 60]
res = linearSearch(arr, 6, 50)
if (res is not None):
    print("Key found through Linear Search...\n")
res = binarySearch(arr, 50, 0, 5)
if (res is not None):
    print("Key found through Binary Search...\n")
