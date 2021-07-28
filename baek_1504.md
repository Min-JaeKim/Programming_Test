# python

## baek 1504 특정한 최단 경로 골드4

https://www.acmicpc.net/problem/1504

> python3 588ms

* 문제

  > 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
  >
  > 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
  >
  > ```bash
  >4 6
  > 1 2 3
  >2 3 3
  > 3 4 1
  >1 3 5
  > 2 4 5
  >1 4 4
  > 2 3
  > ```
  > 
  
* 출력

  > 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
  >
  > ```bash
  > 7
  > ```



```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def sol():
    n, e = map(int, input().split())
    arr = [[] for _ in range(n+1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        arr[a].append([b, c])
        arr[b].append([a, c])

    v1, v2 = map(int, input().split())

    # 1 <-> v1 <-> v2 <-> n
    # 1 <-> v2 <-> v1 <-> n

    def dij(start, *end):

        dist = [float('inf')] * (n+1)
        heap, dist[start] = [], 0
        heappush(heap, (0, start))

        while heap:
            wt, node = heappop(heap)

            if dist[node] < wt:
                continue

            for node2, wt2 in arr[node]:
                if dist[node2] > wt + wt2:
                    dist[node2] = wt + wt2
                    heappush(heap, (wt+wt2, node2))

        return (dist[i] for i in end)

    # 1에서 v1, v1->v2, v1->n
    v1_to_1, v1_to_v2, v1_to_n = dij(v1, 1, v2, n)
    # 1-> v2, v2->n
    v2_to_1, v2_to_n = dij(v2, 1, n)
    # 1->v1->v2->n  vs  1->v2->v1->n
    res = min(v1_to_1+v2_to_n, v2_to_1+v1_to_n) + v1_to_v2
    print(res if res != float('inf') else -1)


sol()
```

> 하,,,,,,,,,,,,,,,,,,, 멍청이 빠가사리 ㅜ 모든 노드 방문하는 줄 알고 한참 풀었다 어굴해 ㅠ 슬프다.



* 모범답안

  ```python
  import sys
  import heapq
  import math
  
  
  def solve():
      read = sys.stdin.readline
      v, e = map(int, read().split())
      graph = [{} for _ in range(v + 1)]
      for _ in range(e):
          v1, v2, d = map(int, read().split())
          if v2 in graph[v1]:
              graph[v1][v2] = min(graph[v1][v2], d)
              graph[v2][v1] = min(graph[v2][v1], d)
          else:
              graph[v1][v2] = d
              graph[v2][v1] = d
      v_1, v_2 = map(int, read().split())
  
      def dijkstra(start, *end):
          h = []
          heapq.heappush(h, (0, start))
          dist = [math.inf for _ in range(v + 1)]
          dist[start] = 0
          while h:
              d1, v1 = heapq.heappop(h)
              if dist[v1] < d1:
                  continue
              for v2, d2 in graph[v1].items():
                  if dist[v2] > d1 + d2:
                      dist[v2] = d1 + d2
                      heapq.heappush(h, (dist[v2], v2))
          return tuple([dist[i] for i in end])
  
      # 여기서 엄청난 발견이 있다. 1 -> v_1 -> v_2 -> v와 1 -> v_2 -> v_1 -> v중에서 더 작은 것을 골라야 되는데
      # 방향이 없는 그래프이기에, 1 -> v_1과 v_1 -> 1이 같다. 다른 간선들도 모두 마찬가지다.
      # 그래서 dijkstra를 최소한으로 돌리기 위해서는, 시작 노드의 수를 최대한 줄이는 것이 좋다.
      # 그래서 v_1 -> 1, v_1 -> v_2, v_1 -> v를 한방에 구하고
      # 마찬가지로 v_2 -> 1, v_2 -> v를 한방에 구하는 것이다.
      d_v1_1, d_v1_v2, d_v1_v = dijkstra(v_1, 1, v_2, v)
      d_v2_1, d_v2_v = dijkstra(v_2, 1, v)
      res = min(d_v1_1 + d_v2_v, d_v2_1 + d_v1_v) + d_v1_v2
      print(-1 if math.isinf(res) else res)
  
  
  solve()
  ```

  > 딕셔너리로 그래프 받으면 더 빠름

