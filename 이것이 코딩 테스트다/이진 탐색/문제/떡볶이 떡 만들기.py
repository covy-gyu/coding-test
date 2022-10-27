# 파라메트릭 서치 Parametric Search
# 최적화 문제를 결정 문제(예 아니오)로 바꾸어 해결하는 기법
# 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정
# 입력이 10억까지 > 바로 이진탐색

def binary_search(arr,target, start, end):
    while start<=end:
        mid = (start+end)//2
        if (sum(arr) - len(arr)*mid) == target:
            return mid
        elif (sum(arr) - len(arr)*mid) > target:
            end = mid - 1
        else:
            start = mid +1
    while target != arr[mid]:
        if target < arr[mid]:
            arr[mid] -= 1
        elif target > arr[mid]:
            arr[mid] += 1
    return mid

n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

print(arr[binary_search(arr,m,0,n-1)])