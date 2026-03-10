#def sum(arr):
#    n=len(arr) #5 // 4 // 3 // 2 // 1
#    if n==2:
#        return add
#    else:
#        add=arr[n-1]+1 # arr[4]+arr[3] // arr[3]+arr[2] // arr[2]+arr[1] // arr[1]+arr[0]
       
#       sum( arr[:n-1] ) #[43, 3453, 3554, 56]  //  [43, 3453, 3554] // [43, 3453] // [43] 
           
         

#list_sum=[43, 3453, 3554, 56, 567];

##print(sum(list_sum));
##print(list_sum[:3]);  --> [43, 3453, 3554]
##print(list_sum[1:]); [3453, 3554, 56, 567]


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

