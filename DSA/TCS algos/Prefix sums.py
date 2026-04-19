def prefix(arr):
    pre = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        pre[i+1]= pre[i] + arr[i]
    return pre

def range_sum(pre,l,r):
    return pre[r+1] - pre[l]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    pre = prefix(arr)
    print("Prefix sums array:", pre)
    l, r = 1, 3
    print(f"Sum of elements from index {l} to {r} is: {range_sum(pre,l,r)}")
