# 매번 가장 작은 것을 선택함.
# 모든 원소 위치 바꿈
# 이중 for문으로 O(N^2),
# 비효율적이지만 특정 리스트에서 가장 작은 데이터를 찾는 일이 잦음#
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # 스와프
print(arr)

# 스와프란 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업을 의미한다.#
