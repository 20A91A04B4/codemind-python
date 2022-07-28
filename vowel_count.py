n=input()
l=list(n)
v='aeiouAEIOU'
c=0
j=[]
for i in range(len(n)):
    if l[i] in v:
        j.append(l[i])
        c+=1
if c==0:
    print('0')
else:
    print(c)