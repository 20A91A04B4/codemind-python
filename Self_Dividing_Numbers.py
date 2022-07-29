m=int(input())
n=int(input())
p=[]
for i in range(m,n+1):
    l=list(str(i))
    c=0
    for j in l:
        if int(j)>0:
            if i%int(j)==0:
               c+=1
    if c==len(l):
        p.append(i)
print(*p)
            
    
    