n=int(input())
l=list(map(int,input().split()))
k=int(input())
s1=0
for i in range(0,k):
    s1+=l[i]
print(s1)