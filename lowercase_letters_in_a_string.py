s=input()
l=list(s)
j=[]
c=0
v='abcdefghijklmnopqrstuvwxyz'
for i in l:
    if i in v:
        c+=1
    j.append(i)
print(c)