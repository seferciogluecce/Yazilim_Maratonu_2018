
num=input().split(' ')
L=int(num[0])
H=int(num[1])
olmadi=True

if L==H :
    olmadi=False
    print("YES")
while(L<H and olmadi):
    if H%2==1:
        H=H-1
        H=H/2
        if L==H :
            print("YES")
            olmadi=False
            break
    else:
        H=H/2
        if L==H :
            print("YES")
            olmadi=False
            break
if olmadi:           
    print("NO")