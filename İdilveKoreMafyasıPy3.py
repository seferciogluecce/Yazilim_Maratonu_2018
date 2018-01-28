

n=int(input())
temp=input().split(" ")
arr=[int(x) for x in temp]


i=0
j=n-1
bool_id=True
while(j-i>=1):
    if bool_id:
        if arr[i]<arr[j]:
            i+=1
        elif arr[i] == arr[j]:
            temp_i = i
            temp_j = j
            while(arr[temp_i] == arr[temp_j]):
                temp_i += 1
                temp_j -= 1
            if arr[temp_i] < arr[temp_j]:
                i += 1
            else:
                j-=1
        else :
            j-=1
        bool_id=False
    else:
         if arr[i]<arr[j]:
            j-=1
         elif arr[i] == arr[j]:
            temp_i = i
            temp_j = j
            while(arr[temp_i] == arr[temp_j]):
                temp_i += 1
                temp_j -= 1
            if arr[temp_i] < arr[temp_j]:
                j -= 1
            else:
                i += 1
         else :
             i+=1
         bool_id=True

print(arr[i])