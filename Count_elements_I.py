m,n=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
j=[]
c=0
for i in l:
    for k in l1:
        if i==k and i not in j:
            j.append(i)
            c+=1
print(c)

        