def selectionsort(arr):
    n  = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    selectionsort(arr)
    print("Sorted array:", arr)

# Time complexity: O(n^2) where n is the number of elements in the array.
# Space complexity: O(1) as we are sorting the array in place without using any extra space.

