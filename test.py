n=3
graph = [[] for i in range(n+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
print(graph)
