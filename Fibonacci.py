def fibonacci (n):

    ficvec= [0]*(n+1)

    if n == 0:
        ficvec[0]=0

    elif n == 1:
        ficvec[0]=0
        ficvec[1]=1

    else:
        ficvec[0]=0
        ficvec[1]=1
        for i in range(2, n+1):
            ficvec[i]=ficvec[i-1]+ficvec[i-2]
    
    return ficvec

print(fibonacci(10))