n=int(input())
l=list(str(n))
c=0
j=[]
for i in l:
    if i in l and i not in j:
        j.append(i)
if len(j)==len(l):
    print('Unique Number')
else:
    print('Not Unique Number')