def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        # print("This is L ", L)
        # print("This is R ", R)

        mergesort(L)
        mergesort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
            # print("This is arr ", arr)
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

if __name__ == "__main__":
    arr = [2, 4, 6, 1, 8, 5, 3, 7, 9, 0]
    mergesort(arr)
    print(arr)