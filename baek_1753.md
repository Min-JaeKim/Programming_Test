# python

## baek 1753 최단경로 골드5

https://www.acmicpc.net/problem/1753

> python3 784ms
>
> pypy3 ms



* 문제

  > 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

* 입력

  > 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
  >
  > ```python
  > 5 6
  > 1
  > 5 1 1
  > 1 2 2
  > 1 3 3
  > 2 3 4
  > 2 4 5
  > 3 4 6
  > ```
  >
  > 

* 출력

  > 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
  >
  > ```python
  > 0
  > 2
  > 3
  > 7
  > INF
  > ```



```python
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def Solution():
    v, e = map(int, input().split())
    k = int(input())
    INF = float('inf')
    d = [INF for _ in range(v+1)]
    d[k] = 0
    arr = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        arr[a].append([b, c])

    q = [[0, k]]
    while q:
        wt, node = heappop(q)
        if d[node] < wt:
            continue
        for j, wwt in arr[node]:
            if wt + wwt < d[j]:
                d[j] = wt + wwt
                heappush(q, [wt+wwt, j])

    for i in range(1, v+1):
        print(d[i] if d[i] != float('inf') else 'INF')

Solution()
```

> - `if d[node] < wt:` 이부분이 대박인 게 이거랑 힙큐를 안썼다고 시간초과 났다.. 힙큐는 위대한 것인갑다..
> - `Solution()` : 이게 제일 대박인 부분,,, 메인을 함수로 바꿨더니 시간 엄청 줄였다.. 진짜 신기하다. 왜지?



* 모범답안

  ```python
  import sys
  import heapq
  
  input = sys.stdin.readline
  inf = int(1e9)
  
  
  def dijkstra(G, s, distance):
      q = []
      heapq.heappush(q, (0, s))
      distance[s] = 0
  
      while q:
          dist, now = heapq.heappop(q)
          if distance[now] < dist:
              continue
  
          for i in G[now]:
              cost = dist + i[1]
              if cost < distance[i[0]]:
                  distance[i[0]] = cost
                  heapq.heappush(q, (cost, i[0]))
  
  
  def Solution():
      v, e = map(int, input().split())
      s = int(input())
      G = [[] for _ in range(v + 1)]
      distance = [inf] * (v + 1)
  
      for _ in range(e):
          u, v, w = map(int, input().split())
          G[u].append((v, w))
  
      dijkstra(G, s, distance)
  
      for result in distance[1:]:
          if result == inf:
              print('INF')
          else:
              print(result)
  
  
  Solution()
  ```

  > 이분을 보고 함수를 쓰는 게 시간을 줄일 수 있는 것이란 걸 알게 되었다.
  >
  > `inf = int(1e9)`
  >
  > 요거 정말 멋진게 최댓값을 int(le9) 로 표현할 수 있다는 점이다.

