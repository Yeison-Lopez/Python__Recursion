def sumatoria(n):
    if n==0:
        return 0
    if n>0:
        return sumatoria(n-1)+n
    
print(sumatoria(10))
