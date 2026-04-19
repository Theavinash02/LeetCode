'''
When to use
Problem mentions:

Subarray / substring of size K
Longest / shortest / max / min in a contiguous window
"Window of size K" or "at most K distinct"

Converts O(n²) brute force → O(n).
'''

# Type 2: Variable-size window (expand + shrink)
# Example: Longest subarray with sum ≤ K.
def sliding_window(arr, k):
    left = 0
    curr_sum = 0
    max_length = 0
    for r in range(len(arr)):
        curr_sum += arr[r]
        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        max_length = max(max_length, r - left + 1)
    return max_length

def sliding_window_without_dup_char(k):
    left = 0
    seen = set()
    best = ""
    max_length = 0
    for r in range(len(k)):
        while k[r] in seen:
            seen.remove(k[left])
            left += 1
        seen.add(k[r])
        if r - left + 1 > max_length:
            max_length = r - left + 1
            best = k[left:r+1]
            
    return best, max_length


if __name__ == "__main__":
    # arr = [1,1,1,1,1,1,1,1,1,1, 2, 3, 4, 5]
    # K = 10
    # print("Length of longest subarray with sum ≤ K is:", sliding_window(arr, K))
    a = "abcabcbb"
    longest_substring, length = sliding_window_without_dup_char(a)
    print(f"Longest substring without repeating characters is: '{longest_substring}' with length {length}")