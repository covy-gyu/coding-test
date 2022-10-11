#combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아
#순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다. 다만 원소를 중복해서 뽑는다.
from itertools import combinations_with_replacement
data = ['A','B','C'] #데이터 준비
result = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)