def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__": # blocks the excuction of the code when the file is imported as a module in another file.
    arr = [1,2,3,4,5]
    target = 3
    res = linearsearch(arr,target)
    if res != -1:
        print(f"Element found at index: {res}")
    else:
        print("Element not found in the array.")

# Time complexity: O(n) where n is the number of elements in the array.
# Space complexity: O(1) as we are not using any extra space[ie few variables to store the index and target].