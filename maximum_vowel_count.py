n=input().split()
v='aeiouAEIOU'
m=[]
l=list(n)
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
        m.append(c)
e=max(m)
print(e)
    