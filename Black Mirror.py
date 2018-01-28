N = int(input())

words=[]
for a in range(N):
    words.append(input())
    
if(words[0]>words[1]):
    print("yo")


# Dynamic Programming implementation of LCS problem
 
def lcsx(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
    xi=[m-a-1 for a in range(m)]
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in xi:
        for j in range(n):
            if i == m-1 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j+1]:
                L[i][j] = L[i-1][j+1]+1
            else:
                L[i][j] =  L[i-1][j+1]
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L
#end of function lcs
 
    
# Dynamic Programming implementation of LCS problem
 
def lcs(X,Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    # declaring the array for storing the dp values
    #L = [[0]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    
    start_index = X.rfind(Y[0])
    
    if start_index == -1:
        return 0
    
    for i in range(start_index + 1, m):
        if Y[i - (start_index)] != X[i]:
            return 0
    return m - start_index
            
    
    
    ''' 
    yi=[n-a-1 for a in range(n)]
    for i in range(m+1):
        for j in yi:
            
           if i == 0 and  j == n-1 and X[i] == Y[j]:
                L[i][j] = 1
            elif i+1>=m:
                break               
            elif X[i+1] == Y[j-1]:
                L[i][j] = L[i-1][j+1]+1
            else:
                break
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L
    '''
#end of function lcs

arr=[]
dictX=[]
graph=[[0]*N for a in range(N)]
for a in range(N):
    for b in range(N):
        if words[a]<words[b]:
        
            graph[a][b]=lcs(words[a],words[b])
print("hello")
print(graph)

 