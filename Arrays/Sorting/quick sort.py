def partition(arr, low, high):
    i = low -1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high: # base case
        pi = partition(arr, low, high) # pi is partition index
        quickSort(arr, low, pi-1) # quick sort the left part 
        quickSort(arr, pi +1, high) # quick sort the right half 

if __name__ == "__main__":
    arr = [5, 1, 4, 3, 6, 2, 9, 8, 7]
    n = len(arr)
    quickSort(arr, 0, n-1)
    print(arr)