n,k=map(int,input().split())
l=list(map(int,input().split()))
j=[]
c=0
for i in l:
    if i%k!=0:
        j.append(i)
        c+=1
print(c)