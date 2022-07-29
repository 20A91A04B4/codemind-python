s=input()
l=list(s)
c=0
j=[]
v=' '
for i in l:
    if i in v:
        c+=1
    j.append(i)
print(c)