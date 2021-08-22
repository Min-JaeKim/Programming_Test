# python

## baek 1238 파티 골드3

https://www.acmicpc.net/problem/1238

> python3 1592ms

* 문제

  > N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
  >
  > 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
  >
  > 각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.
  >
  > 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

* 입력

  > 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.
  >
  > 모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.
  >
  > ```bash
  > 4 8 2
  > 1 2 4
  > 1 3 2
  > 1 4 7
  > 2 1 1
  > 2 3 5
  > 3 1 2
  > 3 4 4
  > 4 2 3
  > ```
  >
  
* 출력

  > 첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
  >
  > ```bash
  > 10
  > ```



```python
import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline


def sol():

    def dijk(start, heap):

        while heap:
            wt, node = heappop(heap)
            if dist[start][node] < wt:
                continue

            if wt < dist[start][node]:
                dist[start][node] = wt

            for wt2, node2 in arr[node]:
                if wt + wt2 < dist[start][node2]:
                    heappush(heap, [wt + wt2, node2])
                    dist[start][node2] = wt + wt2

    n, m, x = map(int, input().split())
    arr, answer = [[] for _ in range(n+1)], 0
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b, wt = map(int, input().split())
        arr[a].append([wt, b])

    for root in range(1, n+1):
        tmp, dist[root][root] = arr[root][:], 0
        heapify(tmp)
        dijk(root, tmp)

    for root in range(1, n+1):
        if answer < dist[root][x] + dist[x][root]:
            answer = dist[root][x] + dist[x][root]

    print(answer)


sol()
```

> 하,,, 일단 처음에 dijk 매개변수로 heapify(arr[root])를 넣었다가 답이 안나옴. 저건 NONE이 계속 출력되는데 그 이유는 모르겠다. 걍 tmp에 옮기는 수 밖에 없었다. 



* 모범답안

  ```python
  72
  
  import sys
  from heapq import *
  input = sys.stdin.readline
  n, m, x = map(int, input().split())
  home = [[] for _ in range(n+1)]
  home2 = [[] for _ in range(n+1)]
  for _ in range(m):
      s, e, t = map(int, input().split())
      home[s].append((e, t))
      home2[e].append((s, t))
  
  def dijkstra(g, start):
      d=[9876543210]*(n+1)
      d[start] = 0
      heap = [(0,start)]
      while heap:
          total, node = heappop(heap)
          if d[node]<total:continue
          for nxt, cost in g[node]:
              if d[nxt]>d[node]+cost:
                  d[nxt] = d[node]+cost
                  heappush(heap, (d[nxt],nxt))
      return d[1:]
  
  print(max([a+b for a, b in zip(dijkstra(home, x), dijkstra(home2,x))]))
  ```

  > 단방향이라고 해서 정직하게 단방향이라고 했는데 생각해보니
  >
  > 마을 -> 2 
  >
  > 2 -> 마을
  >
  > 이면 양방향인 것 마냥 모두 배열을 만들어서 2로 도달할 때, 2에서 출발할 때 두 번만 다익스트라 쓸 수 있으니 시간을 절약할 수 있군. 명심하자.
