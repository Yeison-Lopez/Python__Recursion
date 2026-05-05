def list_length(arr):
    if arr==[]:
        return 0
    else:
        return 1 + list_length(arr[1:])
         
    

print(list_length([1, 2, 3, 4, 5,20,25]))


# Example:
# list_length([1, 2, 3, 4, 5]) should return 5

#Step 1: arr = [1, 2, 3, 4, 5, 20, 25]
#Is it empty? No.
#Return 1 + list_length([2, 3, 4, 5, 20, 25]) → waits for the recursive call.#

#Step 2: arr = [2, 3, 4, 5, 20, 25]
#Return 1 + list_length([3, 4, 5, 20, 25])

#Step 3: arr = [3, 4, 5, 20, 25]
#Return 1 + list_length([4, 5, 20, 25])

#Step 4: arr = [4, 5, 20, 25]
#Return 1 + list_length([5, 20, 25])

#Step 5: arr = [5, 20, 25]
#Return 1 + list_length([20, 25])

#Step 6: arr = [20, 25]
#Return 1 + list_length([25])

#Step 7: arr = [25]
#Return 1 + list_length([])

#Step 8: arr = []
#Is it empty? Yes.
#Return 0 → this is the base case.

####### Now it UNWINDS backward (each +1 gets added):

#Step 7 gets 1 + 0 = 1 → returns 1 to #Step 6

#Step 6 gets 1 + 1 = 2 → returns 2 to #Step 5

#Step 5 gets 1 + 2 = 3 → returns 3 to #Step 4

#Step 4 gets 1 + 3 = 4 → returns 4 to #Step 3

#Step 3 gets 1 + 4 = 5 → returns 5 to #Step 2

#Step 2 gets 1 + 5 = 6 → returns 6 to #Step 1

#Step 1 gets 1 + 6 = 7 → final result
