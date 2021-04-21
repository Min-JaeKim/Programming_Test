# python

## baek 14496 그대, 그머가 되어 실버1

https://www.acmicpc.net/problem/14496

> python3 100ms
>
> pypy3 160ms



* 문제

  > 선린에 합격한 대호에게는 큰 고민이 있다. 대호는 중학교 3년 내내 공부만 했기 때문에, 요즘 학생들이 사용하는 ‘야민정음’에 대해서는 문외한이다. 친구들의 대화에 끼고 싶은 대호는 야민정음을 공부하기로 했다.
  >
  > 야민정음이란, 비슷한 모양의 글자를 원래 문자 대신에 사용하는 것을 일컫는다. 예를 들어, ‘그대’는 ‘그머’로, ‘팔도비빔면’은 ‘괄도네넴댼’으로, ‘식용유’는 ‘식용윾’으로, ‘대호’는 ‘머호’로 바꿀 수 있다. 아무 문자나 치환할 수 있는 건 아니며 치환이 가능한 몇 개의 문자들이 정해져있다.
  >
  > 예를 들어보자. (a, b), (a, c), (b, d), (c, d)가 주어지는 경우, a를 d로 바꾸는 방법은 a-b-d, a-c-d로 2개가 있다. (a, b), (b, c), (a, c)가 주어지는 경우, a를 c로 바꾸는 방법은 a-b-c, a-c의 2개가 있다. 하지만 이 경우에는 치환횟수에 차이가 생기게 된다.
  >
  > 머호는 문자 a를 문자 b로 바꾸려하고, N개의 문자와 치환 가능한 문자쌍 M개가 있다. 머호에게 a를 b로 바꾸기 위한 치환의 최소 횟수를 구해서 머호에게 알려주자!
  >
  > 프로그램 작성의 편의를 위해, 머호가 공부하는 모든 문자는 자연수로 표현되어 주어진다.

* 입력

  > 첫째 줄에 머호가 바꾸려 하는 문자 a와 b가 주어진다. 둘째 줄에 전체 문자의 수 N과 치환 가능한 문자쌍의 수 M이 주어진다. (1 <= N <= 1,000, 1 <= M <= 10,000) 이후 M개의 줄에 걸쳐 치환 가능한 문자쌍이 주어진다. 모든 문자는 N이하의 자연수로 표현된다.
  >
  > ```python
  > 1 2
  > 4 4
  > 1 3
  > 1 4
  > 3 2
  > 4 2
  > ```
  >
  > 

* 출력

  > a를 b로 바꾸기 위해 필요한 최소 치환 횟수를 출력한다. 치환이 불가능한 경우는 –1을 출력한다.
  >
  > ```python
  > 2
  > ```



```python
from collections import deque
import sys
input = sys.stdin.readline


a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
v = [0 for _ in range(n+1)]
for _ in range(m):
    s1, s2 = map(int, input().split())
    arr[s1].append(s2)
    arr[s2].append(s1)

res, flag = 0, 0
q = deque([[a, 0]])
while q:
    num, move = q.popleft()
    if num == b:
        flag = 1
        res = move
        break
    for i in range(len(arr[num])):
        if not v[arr[num][i]]:
            v[arr[num][i]] = 1
            q.append([arr[num][i], move+1])
print(res if flag == 1 else -1)
```

> 멍청이! 이걸 dfs로 풀고 시간초과 나서 어리둥절했다.. 어이없음...
>
> 재귀로 짤 수 있는 건 웬만하면 반복문으로도 다 짤 수 있으니 반복문으로 짜는 연습을 들여야겠다..... 바봉



* 모범답안

  ```python
  80
  
  import heapq
  import sys
  input = sys.stdin.readline
  INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
  a, b = map(int, input().split())
  n, m = map(int, input().split())
  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
  graph = [[] for i in range(n + 1)]
  # 최단 거리 테이블을 모두 무한으로 초기화
  distance = [INF] * (n + 1)
  # 모든 간선 정보를 입력받기
  for _ in range(m):
      frm, to = map(int, input().split())
      graph[frm].append(to)
      graph[to].append(frm)
  
  def dijkstra(start):
      q = []
      # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
      heapq.heappush(q, (0, start))
      distance[start] = 0
      while q: # 큐가 비어있지 않다면
          # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
          dist, now = heapq.heappop(q)
          # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
          if distance[now] < dist:
              continue
          # 현재 노드와 연결된 다른 인접한 노드들을 확인
          for i in graph[now]:
              cost = dist + 1
              # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
              if cost < distance[i]:
                  distance[i] = cost
                  heapq.heappush(q, (cost, i))
  # 다익스트라 알고리즘을 수행
  dijkstra(a)
  # 모든 노드로 가기 위한 최단 거리를 출력
  if distance[b] == INF:
      print(-1)
  else:
      print(distance[b])
  ```

  > 

