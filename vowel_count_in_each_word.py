n=input().split()
v='aeiouAEIOU'
l=list(n)
l1=[]
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    l1.append(c)
print(*l1)
        
        


