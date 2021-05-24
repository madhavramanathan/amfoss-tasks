n=int(input())#3
int a
if (n%2!=0) and (n>1):#yes
    for i in range(n):#i=0,i=1,i=2
        for j in range(n):#j=0,j=1,j=2,j=0,j=1,j=2
            if i==(n//2) or j==(n//2):#0!=1 and 0!=1 so no,j=1 so...,
             a[i][j]="D"#D gets printed,D gets printed,d print,d print,
            else:
             a[i][j]="*"#*gets printed,*gets printed
    print(a[i][j])


