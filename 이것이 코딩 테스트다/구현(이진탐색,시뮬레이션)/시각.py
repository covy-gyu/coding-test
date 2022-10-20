# 00시 00분 00초 부터 23시 59분 59초까지 모든 경우는 86,400가지 존재
# 파이썬에서 100,000개 이하는 시간제한 2초 안에 해결 가능!
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)