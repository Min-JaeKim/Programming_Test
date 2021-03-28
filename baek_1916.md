# Python

## baek 1916 최소비용 구하기 골드5

https://www.acmicpc.net/problem/1916



> python3 452ms
>
> pypy3 292ms



* 문제

  > N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

* 입력

  > 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
  >
  > 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
  >
  > ```bash
  > 5
  > 8
  > 1 2 2
  > 1 3 3
  > 1 4 1
  > 1 5 10
  > 2 4 2
  > 3 4 1
  > 3 5 1
  > 4 5 3
  > 1 5
  > ```

* 출력

  > 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
  >
  > ```bash
  > 4
  > ```



```python
from collections import deque           # deque사용
import sys
input = sys.stdin.readline


n = int(input())                        # 도시 개수 5
arr = [[] for _ in range(n+1)]          # 도시 배열 생성
m = int(input())                        # 버스 개수 8
for _ in range(m):                      # 버스 개수를 돌면서
    s, e, w = map(int, input().split()) # 버스의 경로 저장.
    arr[s].append([e, w])
'''
arr 형태 [(갈 수 있는 도시), (가중치)]
[[], 
[[4, 1], [2, 2], [3, 3], [5, 10]], -> 1에서 연결된 도시 (4로 갈 수 있고 가중치는 1 ...)
[[4, 2]],                          -> 2에서 연결된 도시 (4로 갈 수 있고 가중치는 2)
[[4, 1], [5, 1]], 
[[5, 3]], 
[]]
'''

for i in range(n+1):
    arr[i].sort(key=lambda x : x[1])    # 간선의 가중치를 기준으로 정렬. 위와 주석 형태와 같음.

start, end = map(int, input().split())  # 시작 도시, 도착 도시
startarr = [float('inf') for _ in range(n+1)]
# 모든 도시들의 가중치를 최대값으로 만들어줌.
# [inf, inf, inf, inf, inf, inf]

q = deque([])                           # queue를 생성했고
q.append([start, 0])                    # 시작 도시, 가중치 push

while q:                                # 갈 수 있는 도시들의 큐가 존재하는 동안에
    st, wt = q.popleft()                # 시작 도시, 가중치 pop
    for en, tmpwt in arr[st]:           # 시작 도시에서 갈 수 있는 도시들 순회
        # 1이라면 [4, 1], [2, 2], [3, 3], [5, 10] 포문으로 이 좌표를 돌게 됨 [방문가능도시, 가중치]

        if wt + tmpwt < startarr[en]:   # 만약 가중치가 기록되어 있는 가중치보다 작다면
            startarr[en] = wt + tmpwt   # 기록된 가중치 갱신
            # <class 'list'>: [0:inf, 1:inf, 2:inf, 3:inf, 4:1, 5:inf] -> 1에서 4로 가는 가중치는 1.

            q.append([en, wt+tmpwt])    # 현재 위치와 가중치를 큐에 넣어서 최솟값을 찾을 때까지 반복.

print(startarr[end])
```

> - `[float('inf') for _ in range(n+1)]` : 파이썬의 최댓값
> - `arr[i].sort(key=lambda x : x[1]) ` : 람다 형식으로 정렬



* 모범답안

  ```python
  import sys
  import heapq

  input = sys.stdin.readline
  
  
  def dijkstra(s, e):
      pq = []
      heapq.heappush(pq, (0, s))  # 출발지로 가는데 0원의 비용
      visited = [0] * (N + 1)
      while pq:
          cost, w = heapq.heappop(pq)
          if w == e:
              return cost
  
          if visited[w]:
              continue
  
          visited[w] = 1
          for newt_w, next_cost in adj[w]:
              if not visited[newt_w]:
                  heapq.heappush(pq, (cost + next_cost, newt_w))
  
  
  if __name__ == '__main__':
      N = int(input())  # 도시의 개수
      M = int(input())  # 버스의 개수
      adj = {x + 1: [] for x in range(N)}
      for _ in range(M):
          a, b, c = map(int, input().split())
          adj[a].append((b, c))
  
      departure, arrival = map(int, input().split())
      answer = dijkstra(departure, arrival)
      print(answer)
  ```
  
  > 정렬이랑 똑같은 느낌인데 힙큐를 써서 훨씬 시간복잡도를 줄일 수 있었던듯.