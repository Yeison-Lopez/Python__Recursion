We will unwind step by step each iteration of the function

a)	Iteration 1 (initial call)
- sum([1, 2, 3, 4, 5]) is called
- len(arr)=5, then we go  to the recursive case
- Returns : 1+sum([2, 3, 4, 5]) -> Waiting for the recursive result

b)	Iteration 2
- sum[2, 3, 4, 5]is called
- len(arr)=4, then we go  to the recursive case
- Returns : 2+sum([3, 4, 5]) -> Waiting for the recursive result

c)	Iteration 3
- sum([3, 4, 5]) is called
- len(arr)=3, then we go  to the recursive case
- Returns : 3+sum([4, 5])-> Waiting for the recursive result

d)	Iteration 4
- sum([4, 5]) is called
- len(arr)=2, then we go  to the recursive case
- Returns : 4+sum([5])-> Waiting for the recursive result

e)	Iteration 5 
- sum([5]) is called
- len(arr)=1, then we go  to the base case
- Returns : 5

Now the results bubble back up

f)	Iteration 5 returns 5 to iteration 4
g)	Iteration 4: 4+5 =9 returns 9 to iteration 3
h)	Iteration 3: 3+9 =12 returns 12 to iteration 2
i)	Iteration 2: 2+12 =14 returns 14 to iteration 1
j)	Iteration 1: 1+14 =15 returns 15
