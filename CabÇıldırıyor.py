N=int(input())

temp=input().split(" ")
A=[int(x) for x in temp]

Q=int(input())

S=[]
for a in range(Q):
    temp=input().split(" ")

    S.append([int(x) for x in temp])
    
binArr=[ list(bin(x)[2:]) for x in A ]
for a in range(Q):
    case=S[a][0]
    if case==1:

        sumX=0
        for b in range(S[a][1]-1,S[a][2]):
            sumX+=int( "".join(binArr[b]),2)
        print(sumX)
    elif case==2:
        x= S[a][3]
        for b in range(S[a][1]-1,S[a][2]):
            if (x<len(binArr[b])):
                binArr[b][len(binArr[b])-x]='1'
            else:
                for a in range(x-len(binArr[b])+1):
                    binArr[b].insert(0,'0')
                binArr[b].insert(0,'1')

    else:
        x= S[a][3]

        for b in range(S[a][1]-1,S[a][2]):
            if (x<len(binArr[b])):

                binArr[b][len(binArr[b])-x]='0'

