# 리스트 내부에 반복 작성
n = 5

list = [[0 for j in range(n)] for i in range(n)]
print(list)

list = [[0] * n for _ in range(n)]
print(list)