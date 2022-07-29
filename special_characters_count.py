s=input()
l=list(s)
c=0
j=[]
for i in l:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz':
        c+=1
    j.append(i)
print(c)