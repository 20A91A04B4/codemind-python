n=int(input())
s=n**2
l=list(str(s))
st=len(str(n))
k=l[-st:]
d=''
for i in k:
    d+=str(i)
if int(d)==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')