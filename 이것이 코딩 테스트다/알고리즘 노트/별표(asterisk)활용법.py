print(["-"*sum(j in "369"for j in str(i)) or i for i in range(1,int(input())+1)])

# 숫자중 3,6,9가 포함되면 포함된 수만큼 '-'로 출력
# *(Asterisk)가 컨테이너를 Unpacking하는 기능으로 사용됨

# sum()활용법 공부하기