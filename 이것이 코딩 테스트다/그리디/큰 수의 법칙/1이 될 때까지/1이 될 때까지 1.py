# n, k
n, k = map(int, input().split())

count =0
while True:
    if(n%k==0):
        n/=k
    elif(n==1):
        break
    else:
        n-=1
    count+=1
    
print(count)
