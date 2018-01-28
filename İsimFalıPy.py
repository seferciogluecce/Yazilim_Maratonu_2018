
def applyPerm(arr,perx):
    arr2=[0 for a in range(len(arr))]
    for a in range(len(arr)):
        arr2[perx[a]-1]=arr[a]    
    return arr2

Q,N,K = [int(x) for x in input().split(" ")]



per = [int(x) for x in input().split(" ")]
others=[]
for i in range(Q):
    arr=[int(x) for x in input().split(" ")]
    others.append(arr)


latestPerm=per

for a in range(K):
    latestPerm=applyPerm(latestPerm,per)


lenstr=0

def fact(n) :
    f = 1
    while n >= 1 :
        f = f * n
        n = n - 1
    return f

def populateAndIncreaseCount(count,strX):
    for i in range(lenstr):
        count[strX[i]]+=1
    for i in range(1,lenstr):
        count[i]+=count[i-1]
    return count

def updatecount(count,char):
    for i in range(char,lenstr):
        count[i]-=1
    return count
def findrank(strX):
    lenX=N
    mul=fact(lenX)
    rank=1
    count=[0 for a in range(lenstr+1)]
    count=populateAndIncreaseCount(count,strX)
    for a in range(lenX):
        mul=mul/(lenX-a)
        rank+=count[strX[a]-1]*mul
        count=updatecount(count,strX[a])
    return rank




for a in range(Q):

    sP=list(applyPerm(others[a],latestPerm))
    lenstr=max(sP)

    if(findrank(sP)%2==0):
        print("YES")
    else :
        print("NO")




