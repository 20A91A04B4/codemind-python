s=input()
l=list(s)
c=0
for i in l:
    if i not in ' ':
        c+=1
print(c)