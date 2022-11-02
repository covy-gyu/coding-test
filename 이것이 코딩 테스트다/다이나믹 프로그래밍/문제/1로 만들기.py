x = int(input())

count = 0

while x != 1:
    share = x//5
    rest = x%5
    count+=1
    x = share
    if rest == 0:
        continue
    elif rest ==4:
        count+=2
    else:
        count+=1

print(count)