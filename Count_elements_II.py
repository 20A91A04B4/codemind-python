m,n=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
c=0
j=[]
for i in l:
    if i not in l1 and i not in j:
        j.append(i)
        c+=1
for k in l1:
    if k not in l and k not in j:
        j.append(k)
        c+=1
print(c)