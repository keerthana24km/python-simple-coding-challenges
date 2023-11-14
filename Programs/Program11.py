def MaxHeapify(arr, i, N):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < N and arr[l] > arr[i]:
        largest = l
    if r < N and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, N)


def convertMaxHeap(arr, N):

    # Start from bottommost and rightmost
    # internal node and heapify all
    # internal nodes in bottom up way
    for i in range(int((N - 2) / 2), -1, -1):
        MaxHeapify(arr, i, N)


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()


arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
N = len(arr)

print("Min Heap array : ")
printArray(arr, N)

convertMaxHeap(arr, N)

print("Max Heap array : ")
printArray(arr, N)
