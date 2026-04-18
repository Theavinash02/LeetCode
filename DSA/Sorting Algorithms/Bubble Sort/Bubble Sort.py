def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubblesort(arr)
    print("Sorted array:", arr)

    # Time complexity: O(n^2) where n is the number of elements in the array.
    # Space complexity: O(1) as we are sorting the array in place without using
      