# python

## baek 1774 우주신과의 교감 골드4

https://www.acmicpc.net/problem/1774

> python3 3016ms
>
> pypy3 1840ms



* 문제

  > 황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다. 이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.
  >
  > 하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.
  >
  > 우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.
  >
  > 또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.
  >
  > 이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

* 입력

  > 첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.
  >
  > 두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다. 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.
  >
  > ```python
  > 4 1
  > 1 1
  > 3 1
  > 2 3
  > 4 3
  > 1 4
  > ```
  >
  > 

* 출력

  > 첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라. 출력은 소수점 둘째짜리까지 출력하여라.
  >
  > ```python
  > 4.00
  > ```



```python
'''
4 1
1 1
2 5
2 4
4 3
1 4
3.24

4 2
1 1
4 5
7 5
4 3
1 4
2 3
2.00

실수를 세 가지 저질렀다.
1. 이미 방문한 지점에서는 다른 노드로 가는 계산 방법을 안따짐.
2. 이미 어느 한 곳과 연결된 우주신을 체크하여 다른 우주선들과 연결 안 짓도록 함.
3. 이건 아직도 왜인지 알아내지 못했다.
for i in range(n):
    x1, y1 = arr[i]
    for j in range(i+1, n):
이부분을
for i in range(n):
    x1, y1 = arr[i]
    for j in range(n):
이렇게 적으면 틀림,,

'''

from math import sqrt
import sys
input = sys.stdin.readline


def union(i, j):
    i = find(i)
    j = find(j)
    if i > j:
        anc[i] = find(j)
    else:
        anc[j] = find(i)


def find(i):
    if anc[i] == i:
        return i
    anc[i] = find(anc[i])
    return anc[i]


n, m = map(int, input().split())
anc = [i for i in range(n+1)]
arr = []
dist = []
res = 0
line = 0        # 간선 개수 세기
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

for _ in range(m):      # 연결되어 있는 것들 체크
    a, b = map(int, input().split())
    union(a, b)
    line += 1

for i in range(n):      # 거리 계산 코드,,
    # 현재 좌표에서 존재하는 모든 다른 좌표까지의 거리 계산.
    x1, y1 = arr[i]
    for j in range(i+1, n):
        # 이 부분을 for j in range(n)으로 바꾸면 틀리는데, 왜일까요?
        if i == j:
            continue
        x2, y2 = arr[j]
        tmp = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        dist.append([tmp, i+1,  j+1])


dist.sort()
# 거리가 짧은 순서대로

for wt, i, j in dist:
    if find(i) != find(j):
        union(i, j)
        res += wt
        line += 1
    if line == n-1:
        # 모든 간선을 찾았으면 탈출
        break

print('%0.2f' % (res))
```

> 



* 모범답안

  ```python
  972
  
  from heapq import heappop, heappush
  import sys
  
  
  def find(x):
      if home[x] < 0:
          return x
  
      home[x] = find(home[x])
      return home[x]
  
  
  def union(a, b):
      a, b = find(a), find(b)
      home[b] = a
  
  
  N, M = map(int, sys.stdin.readline().split())
  home = [-1] * (N + 1)
  arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  my_heap = []
  answer, cnt = 0, 0
  
  for i in range(N):
      for j in range(i+1, N):
          weight = pow(pow(arr[i][0] - arr[j][0], 2) + pow(arr[i][1] - arr[j][1], 2), 0.5)
          heappush(my_heap, (weight, i+1, j+1))
  
  for _ in range(M):
      x, y = map(int, sys.stdin.readline().split())
      if find(x) != find(y):
          union(x, y)
          cnt += 1
  
  for i in range(len(my_heap)):
      w, a, b = heappop(my_heap)
  
      if find(a) != find(b):
          union(a, b)
          answer += w
          cnt += 1
  
          if cnt == N-1:
              break
  
  print(format(answer, ".2f"))
  ```

  > 휴,,
  >
  > 이게 최저시간이 나온 이유에 대해서 연구하느라 좀 늦었다.
  >
  > 1. `if find(x) != find(y):` 이코드가 필요한가보다. 그 이유는 연결되어 있는 노드 중에 중복된 게 좀 있기 때문인듯
  > 2. `home[b] = a` : 글고 유니온할 때 비교를 안해서 시간을 줄일 수 있었던듯,, 휴 어렵다 어려워
  > 3. `arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]` 입력을 이런식으로 받음. 이건 시간 줄이기는 아니고 걍 코드줄이기 ㅎㅎ

