
k=input()
num=int(k[::-1])

def is_prime(n):
    return all(n%j for j in range(2, int(n**0.5)+1)) and n>1
if int(k)==num:
    print("No")
    
elif is_prime(num):
    print("Yes")
else:
    print("No")
    
