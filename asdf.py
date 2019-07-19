a=input().strip()
b=list(a)
t=0
c=['a','e','i','o','u']
for i in b:
    if i in c:
        t=t+1
if t%2==0 and t>0:
    for i in range(1,len(b),2):
        print(b[i],end="")
elif t==0:
    print("-1")
else:
    for i in  range(0,len(b),2):
        print(b[i],end="")
