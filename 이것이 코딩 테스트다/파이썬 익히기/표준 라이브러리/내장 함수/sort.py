#리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어서 굳이 sorted() 함수를 사용하지 않고도 sort() 함수를 사용해서 정렬할 수 있다.
data = [9,1,8,5,4]
data.sort()
print(data)

data.sort(reverse=True)
print(data)