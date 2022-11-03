# 최단 경로, '음의 간선'이 없을 때
# 기본적으로 그리디 알고리즘 - 매번 가장 비용이 적은 노드를 선택하는 임의의 과정을 반복
# 1. 출발 노드 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 5. 위 과정에서 3과 4를 반복
# 무한 = 1e9
#
# 간단 구현#
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한값 10억
#노드, 간선
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

#방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드의 번호를 반환
def get_smalleset_node():
    min_value = INF
    index = 0 # 최단 거리가 가장 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] =0
    visited[start] = True
    #그래프 노드 순서대로 간선 비용(거리) 값 설정
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1(시작노드)개의 노드에 대해 반복 
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smalleset_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now]+j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    #도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

# 시간 복잡도 O(V^2)
# 노드 개수가 5000개 이하라면 이 코드로 해결 가능
# 10,000개이상은 어려움#
    