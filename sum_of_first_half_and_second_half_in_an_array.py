n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(n//2):
    s1+=l[i]
for j in range(n//2,n):
    s2+=l[j]
print(s1)
print(s2)
    