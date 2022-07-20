n=int(input())
l=list(map(int,input().split()))
s=sum(l)
avg=s//n
k=[]
c=0
for i in range(n):
    if l[i]<=avg:
        c+=1
print(c)

        
    