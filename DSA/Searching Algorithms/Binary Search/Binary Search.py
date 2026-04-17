def iterative_binarysearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <=right : 
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Time complexity: O(log n) where n is the number of elements in the array.
# Space complexity: O(1) as we are not using any extra space[ie few variables to store the index and target].

def recur_binarysearch(arr, target, low,high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recur_binarysearch(arr, target, mid + 1,high)
    elif arr[mid] > target:
        return recur_binarysearch(arr, target, low, mid - 1)
    else:
        return -1
    
# Time complexity: O(log n) where n is the number of elements in the array.
# Space complexity: O(log n) due to recursive call stack.

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 14
    res = recur_binarysearch(arr, target, 0, len(arr) - 1)
    if res != -1:
        print(f"Element found at index: {res}")
    else:
        print("Element not found in the array.")

