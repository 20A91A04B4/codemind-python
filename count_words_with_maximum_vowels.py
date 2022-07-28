n=input().split()
v='aeiouAEIOU'
k=[]
l=list(n)
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    k.append(c)
m=max(k)
p=[]
for e in k:
    if m==e:
        p.append(e)
print(len(p))

    

