#sorted() 함수는 iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다.
result = sorted([9,1,8,5,4])                #오름차순으로 정렬
print(result)
result = sorted([9,1,8,5,4],reverse=True)   #내림차순으로 정렬
print(result)

#튜플의 두번째 원소를 기준으로 정렬하기
result = sorted([('홍길동',35),('이순신',75),('이무개',50)], key = lambda x: x[1], reverse = True)
print(result)