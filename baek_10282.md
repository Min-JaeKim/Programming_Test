# python

## baek 10282 해킹 골드4

https://www.acmicpc.net/problem/10282

> python3 1132ms

* 문제

  > 최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다. 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.
  >
  > 최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 개수는 최대 100개이다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
  >
  > - 첫째 줄에 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c가 주어진다(1 ≤ n ≤ 10,000, 1 ≤ d ≤ 100,000, 1 ≤ c ≤ n).
  > - 이어서 d개의 줄에 각 의존성을 나타내는 정수 a, b, s가 주어진다(1 ≤ a, b ≤ n, a ≠ b, 0 ≤ s ≤ 1,000). 이는 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨을 뜻한다.
  >
  > 각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않는다.
  >
  > ```bash
  > 2
  > 3 2 2
  > 2 1 5
  > 3 2 5
  > 3 3 1
  > 2 1 2
  > 3 1 8
  > 3 2 4
  > ```
  >
  
* 출력

  > 각 테스트 케이스마다 한 줄에 걸쳐 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력한다.
  >
  > ```bash
  > 2 5
  > 3 6
  > ```



- 

```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    t = int(input())

    for _ in range(t):

        n, d, c = map(int, input().split())
        # 출발지에서 모든 컴퓨터까지의 거리를 좁혀나가는 방식으로 해결.
        v = [float('inf')] * (n+1)
        arr = [[] for _ in range(n+1)]

        for _ in range(d):
            aa, bb, s = map(int, input().split())
            arr[bb].append([aa, s])

        q, v[c] = deque([[c, 0]]), 0

        while q:
            node, wt = q.popleft()

            for hacking, time in arr[node]:
                if time + wt < v[hacking]:
                    v[hacking] = time + wt
                    q.append([hacking, wt + time])

        hacking_cnt, hacking_time = 0, 0
        for i in range(1, n+1):
            if v[i] != float('inf'):
                hacking_cnt += 1
                if hacking_time < v[i]:
                    hacking_time = v[i]

        print(hacking_cnt, hacking_time)


sol()
```

> 아 별것도 아닌 문젠데 왜이렇게 오래 풀었지,, 짱난다 증말 ㅠㅠ~



* 모범답안

  ```python
  780
  
  import sys
  import heapq
  MAX = 1e9
  input = sys.stdin.readline
  
  
  def solve():
      def dijkstra(u):
          dist = [MAX]*(n+1)
          dist[u] = 0
          q = [(0, u)]
          while q:
              t, u = heapq.heappop(q)
              if t > dist[u]:
                  continue
              for v, tt in adj[u]:
                  tt += t
                  if tt >= dist[v]:
                      continue
                  dist[v] = tt
                  heapq.heappush(q, (tt, v))
          resc = rest = 0
          for time in dist:
              if time < MAX:
                  resc += 1
                  if rest < time:
                      rest = time
          print(resc, rest)
  
      n, d, c = map(int, input().split())
      adj = [[] for _ in range(n+1)]
      for _ in range(d):
          a, b, s = map(int, input().split())
          adj[b].append((a, s))
      dijkstra(c)
  
  
  if __name__ == '__main__':
      for _ in range(int(input())):
          solve()
  ```

  > 으음
  >
  > 힙큐를 써서 빠르군.

