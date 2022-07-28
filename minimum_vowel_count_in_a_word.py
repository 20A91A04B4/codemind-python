n=input().split()
l=list(n)
v='aeiouAEIOU'
c=0
k=[]
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    k.append(c)
m=min(k)
print(m)