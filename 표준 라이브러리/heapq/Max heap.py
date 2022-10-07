#파이썬의 힙은 최대 힙을 제공하지 않는다.
#원소의 부호를 임시로 변경하는 방식을 사용한다.
#O(NlogN), 내림차순 정렬
import heapq
def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
