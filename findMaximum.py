def find_max(arr):
    n=len(arr);
    if n == 1:
        return arr[0]
    elif arr[n-1]>find_max(arr[:n-1]):
        return arr[n-1]
    else:
        return find_max(arr[:n-1])

    
print(find_max([3, 10, 30, 9, 1, 500]))








# Example:
# find_max([3, 7, 2, 9, 1, 5]) should return 9