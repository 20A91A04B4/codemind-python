n=int(input())
k=n**2
l=list(str(k))
s=0
for i in l:
    s=s+int(i)
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    
    