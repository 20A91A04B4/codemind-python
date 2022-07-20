n=int(input())
l=list(map(int,input().split()))
l.reverse()
s=0
for i in range(n):
    j=2
    s+=l[i]*(j**i)
print(s)