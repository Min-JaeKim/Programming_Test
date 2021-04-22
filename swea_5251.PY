# python

## swea 5251 d4 최소 이동 거리

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

learn - advanced - MST

> 

* 문제

  > 
  
* 입력

  > 
  >
  > ```bash
  >
  > ```
  
* 출력

  > 
  >
  > ```bash
  >
  > ```



```python
from heapq import heappush, heappop

for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    v = [[1000001] * (n+1) for _ in range(n+1)]
    # 출발지를 기준으로 노드들의 거리를 표현한 리스트
    startd = [1000001] * (n+1)
    res = 1000001
    for i in range(e):
        a, b, c = map(int, input().split())
        v[a][b] = c
    q = [[0, 0]]
    while q:
        node, wt = heappop(q)
        if node == n:
            res = wt
            break
        for i in range(n + 1):
            # 현재 방문할 때가 가장 짧은 거리의 방문이라면
            if v[node][i] + wt < startd[i]:
                startd[i] = v[node][i] + wt
                heappush(q, [i, v[node][i] + wt])
    print('#%d %d' % (tc, res))
```

> 어줍잖게 방문 표시를 썼다가 안풀려서 고통스러웠다..



* 모범답안

  ```python
  import heapq
   
  for t in range(int(input())):
      N, E = map(int, input().split())
      distance =[0] + [float('inf') for _ in range(N)]
      node = [[] for _ in range(N+1)]
      visited = [0 for _ in range(N+1)]
      for _ in range(E):
          a, b, c = list(map(int, input().split()))
          node[a].append((b, c))
      queue = []
      heapq.heappush(queue, (0, 0))
      while queue:
          d, idx = heapq.heappop(queue)
          if visited[a]:
              continue
          visited[idx] = 1
          for a, b in node[idx]:
              if distance[a] > d + b:
                  distance[a] = d + b
                  heapq.heappush(queue, (distance[a], a))
      print('#{} {}'.format(t+1, distance[N]))
  ```
  
  > 음,,