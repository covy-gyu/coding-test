#리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(counter['red'])
print(dict(counter))
print(counter)