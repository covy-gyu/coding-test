n = int(input())
arr = [0]*1000001

for i in input().split():
    arr[int(i)] = 1

m = int(input())
x = list(map(int,input().split()))

for i in x:
    #해당 부품이 존재하는지 확인
    if arr[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')
