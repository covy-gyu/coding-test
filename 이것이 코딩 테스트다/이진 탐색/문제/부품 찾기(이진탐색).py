# 이진 탐색 소스코드 구현(반복)
def binary_search(arr, target, start, end):
    while start<=end:
        mid = (start + end) // 2
        #찾은 경우
        if arr[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif arr[mid] > target:
            end = mid - 1
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None
    
n = int(input())
arr = list(map(int,input().split()))
arr.sort() #이진 탐색을 수행하기 위해 사전에 정렬 수행
m = int(input())
x = list(map(int,input().split()))

#손님이  확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해딩 부품이 존재하는지 확인
    result = binary_search(arr,i,0,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')