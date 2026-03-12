
def sum(arr):
    if len(arr) == 0:  # Base case: empty list 
        return 0
    elif len(arr) == 1:  # Base case: single element
        return arr[0] #(4) return 567
    else:
        # Recursive case: first element + sum of remaining elements
        return arr[0] + sum(arr[1:])    # (1) [3453, 3554, 56, 567] // (2) [ 3554, 56, 567] // (3) [56, 567] //

list_sum=[1, 2, 3, 4, 5]
print(sum(list_sum))  # Output: 15

