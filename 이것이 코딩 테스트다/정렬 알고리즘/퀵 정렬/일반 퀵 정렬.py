# 호어 분할Hoare partition방식
# 리스트에서 첫 번째 데이터를 피벗으로 정한다
# 피벗pivot이라는 기준을 설정하고 (설정방법에 따라 여러 방식으로 퀵정렬을 구분함)
# 왼쪽에서부터 피벗보다 큰 데이터를 찾고
# 오른쪽에서부터 피벗보다 작은 데이터를 찾는다
# 그리고 서로 교환해준다
# 엇갈린 경우 작은데이터와 피벗의 위치를 서로 변경한다#

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):  # 리스트, 시작인덱스, 마지막인덱스(길이-1)
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소의 인덱스
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾는 것을 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾는 것을 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)

# 평균의 경우 O(NlogN)
# 최악의 경우 O(N^2)
# 이미 정렬되어 있는 경우 가장 느림 > 삽입정렬과 반대#
