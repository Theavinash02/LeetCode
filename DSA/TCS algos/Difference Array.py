def diff_array(arr,updates):
    diff = [0] * (len(arr) + 1)
    for l,r,val in updates:
        diff[l] += val
        diff[r+1] -= val
    return diff
def prefix_sum(diff):
    pre = [0] * len(diff)
    pre[0] = diff[0]
    for i in range(1,len(diff)):
        pre[i] = pre[i-1] + diff[i]
    return pre[:-1]

if __name__ == "__main__":
    arr = [0, 0, 0, 0, 0]
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    diff = diff_array(arr, updates)
    print("Difference array:", diff)
    pre = prefix_sum(diff)
    print("Updated array after applying updates:", pre)
