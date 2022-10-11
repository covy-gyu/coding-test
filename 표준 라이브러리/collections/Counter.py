#리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
from collections import Counter
from itertools import count
import math
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(counter['red'])
print(dict(counter))
print(counter)

# str = "dccccd"
# k=3
# list_splited = list(str)
# list_num = [ord(char)-96 for char in list_splited]
# list_num_chunked = [list_num[i:i+k] for i in range(0,len(list_num)-k+1,1)]
# res_sum = 0
# list_sum = [0 for _ in range(len(list_num_chunked)) ]
# for i in range(len(list_num_chunked)):
#     counter = Counter(list_num_chunked[i])
#     values = list(counter.values())
#     keys = list(counter.keys())
#     for j in range(len(keys)):
#         if(values[j]>1):
#             list_sum[i]+=math.pow(keys[j],values[j])
#         else: list_sum[i]+=keys[j]
# list_sum.sort(reverse=True)
# print(int(list_sum[0]))