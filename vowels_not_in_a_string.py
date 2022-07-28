n=input()
v='aeiou'
j=[]
for i in v:
    if i in v and i not in n:
        if i not in j:
            j.append(i)
if len(j)==0:
    print('0')
else:
    print(*j)
