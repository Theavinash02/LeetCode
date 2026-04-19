def pair_sm_sorted(arr,t):
    left,right = 0,len(arr)-1
    while left<right:
        if arr[left]+arr[right] == t:
            return True
        elif arr[left]+arr[right] < t:
            left+=1
        else:
            right-=1
    return None

def pair_sm_unsorted(arr,t):
    s = sorted(arr)
    left,right = 0,len(s)-1
    while left<right:
        if s[left]+s[right] == t:
            return True
        elif s[left]+s[right] < t:
            left+=1
        else:
            right-=1
    return False



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    t = 9
    print(pair_sm_sorted(arr,t))
    arr = [5,4,3,2,1]
    t = 9
    print(pair_sm_unsorted(arr,t))

