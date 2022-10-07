#permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
from itertools import permutations
data = ['A','B','C'] #데이터 준비
result = list(permutations(data,3)) # 모든 순열 구하기
print(result)
