s=input()
u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l=list(s)
c=0
j=[]
for i in l:
    if i in u:
        c+=1
    j.append(i)
print(c)
        
    