import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수, 시작 노드
n, m, start = map(int, input().split())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    #x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] =0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost,i[0]))

dijkstra(start)

count =0
max_distance = 0
for d in distance:
    if d != INF:
        count +=1
        max_distance = max(max_distance,d)

print(count -1, max_distance)

