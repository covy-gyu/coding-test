# 퀵과 비슷한 병합 정렬+삽입정렬의 하이브리드 기반
# 일반적으로 퀵보다는 느리지만 최악의 경우에도 O(NlogN)을 보장
# #

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(arr)
print(result)

#내림차순 reverse속성
result = sorted(arr, reverse=True)
print(result)
