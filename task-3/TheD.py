n=int(input())
i=0
c=1;
if (n%2!=0) and (n>1):
    while i>-1:
        for j in range(n):
            if j>=(n//2-i) and j<=(n//2+i):
             print("D",end='')
            else:
             print("*",end='')
        if(i==n//2):
            c=-1
        i+=c;
        print()
        