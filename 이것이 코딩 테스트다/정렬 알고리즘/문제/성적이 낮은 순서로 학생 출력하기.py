
n = int(input())

## sorted 이용
# arr = []
# for i in range(n):
#     input_data = input().split()
#     #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
#     arr.append((input_data[0],int(input_data[1])))

# #키를 이용하여 점수를 기준으로 정렬
# arr = sorted(arr,key=lambda student: student[1])

# #정렬이 수행된 결과를 출력
# for student in arr:
#     print(student[0], end=' ')

#사전 자료형 이용
data = dict()
for i in range(n):
    input_data = input().split()
    data[input_data[0]] = input_data[1]

data = sorted(data.items(),key=lambda student: student[1])

for i in range(n):
    print(data[i][0], end=' ')