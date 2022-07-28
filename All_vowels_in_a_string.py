s=input()
l=[]
v='aeiou'
for i in v:
    if i in v and i in s:
        l.append(i)
if len(v)==len(l):
    print('True')
else:
    print('False')