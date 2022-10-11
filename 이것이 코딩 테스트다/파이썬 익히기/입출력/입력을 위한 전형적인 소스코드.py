#입력을 위한 전형적인 소스코드
#데이터의 개수 입력
n = int (input())
#각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse = True)
print(data)

#공백을 기준으로 구분하여 적은 수의 데이터 입력
# n, m, k를 공백으로 구분하여 입력
n,m,k = map(int, input().split())
print(n,m,k)