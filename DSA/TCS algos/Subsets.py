# def subsets(arr):
#     result = []

#     def backtrack(start, current):
#         result.append(current[:])          # every state is a valid subset

#         for i in range(start, len(arr)):
#             current.append(arr[i])
#             backtrack(i + 1, current)
#             current.pop()                  # undo

#     backtrack(0, [])
#     return result

# if __name__ == "__main__":
#     arr = [1, 2, 3]
#     print(subsets(arr))

def subsets(arr):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

if __name__ == "__main__":
    arr = [1, 2, 3]
    print(subsets(arr))