n=input()
l=list(n)
s=0
pr=1
j=[]
p=[]
for i in l:
    s=s+int(i)
    j.append(s)
for i in l:
    pr=pr*int(i)
    p.append(pr)
if s==pr:
    print('Spy Number')
else:
    print('Not Spy Number')
    
    