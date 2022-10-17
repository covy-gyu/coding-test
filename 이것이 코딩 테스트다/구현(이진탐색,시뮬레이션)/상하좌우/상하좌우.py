#nxn 정사각형 여행자의 이동 순서대로 도착하게 되는 곳의 좌표 구하기
n = int(input())
direction = list(map(str,input()))
x =0 
y =0

arr = [[0 for j in range(n)] for i in range(n)]

for i in range(len(direction)):
    d = direction[i]
    if d == "L" and (x-1)>=0:
        x-=1
    elif d == "R" and (x+1)<len(direction):
        x+=1
    elif d == "U" and (y-1)>=0:
        y-=1
    elif d == "D" and (y+1)<len(direction):
        y+=1
    else: continue

print(x,y)
