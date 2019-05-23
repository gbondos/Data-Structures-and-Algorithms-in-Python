"""
Program for array rotation
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
Array = [1, 2, 3, 4, 5, 6, 7]

Rotation of the above array by 2 will make array
Array = [3, 4, 5, 6, 7, 1, 2]
ArrayRotation1
"""
# METHOD 1
"""
Method 1
"""
def rotate_by_one(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

def rotate_by_d_elements(d, arr):
    for i in range(d):
        rotate_by_one(arr)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate_by_d_elements(2, arr)
    print(arr)

main()
