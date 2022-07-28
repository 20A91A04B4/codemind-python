n=input()
e=input()
v='aeiou'
l=list(n)
k=[]
for i in range(len(l)):
    if e in l[i] and e in v:
        print('True',i,sep='
')
        break
else:
    print('False')
