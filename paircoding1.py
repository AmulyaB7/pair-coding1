n=int(input())
array=list(map(int,input().split()))
issorted=True
for i in range(n):
    for j in range(i+1,n):
        if array[j]<array[i]:
            issorted=False

print(issorted)
        
            