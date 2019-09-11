#Your code below
a=input().strip()
b=int(input())
a=list(a)
b1=[['0' for i in range(b)] for k in range(len(a)//b)]
c=[]
j,k=0,0
for i in range(len(a)):        
    b1[j][k]=a[i]
    if k==b-1:
        j=j+1
        k=0
    else:
        k=k+1
for i in range(len(b1)):
    b1[i]=list(b1[i])
    if (i+1)%2==0:
        b1[i].reverse()
    c.append(b1[i])
j,k=0,0
for i in range(len(a)):
    print(c[j][k],end="")
    if j==len(a)//b-1:
        j=0
        k=k+1
        continue   
    j=j+1
    
