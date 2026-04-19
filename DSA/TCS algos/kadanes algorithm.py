def kadanes_algo(arr):
    curr_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        curr_sum = max(curr_sum + arr[i],arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print("Maximum subarray sum is:", kadanes_algo(arr))