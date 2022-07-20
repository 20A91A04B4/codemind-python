n=int(input())
arr=list(map(int,input().split()))
o=[]
e=[]
for i in range(n):
    if arr[i]%2:
        o.append(arr[i])
    else:
        e.append(arr[i])
m=o+e
print(*m)
        