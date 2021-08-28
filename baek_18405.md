# python

## baek 18405 경쟁적 전염 실버1

https://www.acmicpc.net/problem/18405

> python3 644ms

* 문제

  > *N*x*N* 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 *K*번까지의 바이러스 종류 중 하나에 속한다.
  >
  > 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
  >
  > 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, *S*초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 만약 *S*초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.
  >
  > 예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 1초가 지난 후에 시험관의 상태는 다음과 같다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 2초가 지난 후에 시험관의 상태는 다음과 같다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 결과적으로 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류는 3번 바이러스다. 따라서 3을 출력하면 정답이다.

* 입력

  > 첫째 줄에 자연수 *N*, *K*가 공백을 기준으로 구분되어 주어진다. (1 ≤ *N* ≤ 200, 1 ≤ *K* ≤ 1,000) 둘째 줄부터 *N*개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 *N*개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 *K*이하의 자연수로만 주어진다. *N*+2번째 줄에는 *S*, *X*, *Y*가 공백을 기준으로 구분되어 주어진다. (0 ≤ *S* ≤ 10,000, 1 ≤ *X*, *Y* ≤ *N*)
  >
  > ```bash
  > 3 3
  > 1 0 2
  > 0 0 0
  > 3 0 0
  > 2 3 2
  > ```
  >
  
* 출력

  > *S*초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 *S*초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
  >
  > ```bash
  > 3
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    dic = {}
    for i in range(1, k+1):
        dic[i] = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                dic[arr[i][j]].append([i, j])

    for _ in range(s):
        for i in range(1, k+1):
            if dic[i]:
                for j in range(len(dic[i])):
                    r, c = dic[i].popleft()

                    for m in range(4):
                        nr, nc = r + dr[m], c + dc[m]

                        if 0 <= nr < n and 0 <= nc < n and not arr[nr][nc]:
                            arr[nr][nc] = i
                            dic[i].append([nr, nc])

    print(arr[x-1][y-1])


sol()
```

> 아놩 변수 겹치게 써서 한 번 틀렸다 까비. 파이썬은 이래서 조심조심 해야됨 변수 하나를 쓰더라도 중복되지 않은 건지 확인해야 한다고.



- 두번째 풀이

```python
192

import sys
from heapq import *
input = sys.stdin.readline


def sol():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    heap = []

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                heappush(heap, [arr[i][j], i, j])

    for _ in range(s):
        heap2 = []

        while heap:
            wt, i, j = heappop(heap)

            for d in range(4):
                ni, nj = i + dr[d], j + dc[d]

                if 0 <= ni < n and 0 <= nj < n and not arr[ni][nj]:
                    arr[ni][nj] = wt
                    heap2.append([wt, ni, nj])

        heap = heap2[:]

    print(arr[x-1][y-1])


sol()
```

> 우선순위큐를 써서 더 빨라짐.



* 모범답안

  ```python
  72
  
  import sys
  input = sys.stdin.readline
  
  def solution():
      n, k = map(int, input().split())
      maps = [(list(map(int, input().split()))) for _ in range(n)]
      s, x, y = map(int, input().split())
  
      dx = [-1, 0, 1, 0]
      dy = [0, 1, 0, -1]
  
      x -= 1
      y -= 1
      if maps[x][y] != 0 :
          print(maps[x][y])
          return
      
      q = []
      visited = [(x, y)]
      maps[x][y] = 1001
      for i in range(s):
          temp = []
          while visited:
              x, y = visited.pop()
              for d in range(4):
                  nx = x+dx[d]
                  ny = y+dy[d]
                  if nx > -1 and ny > -1 and nx < n and ny < n:
                      if maps[nx][ny] != 0 and maps[nx][ny] != 1001:
                          q.append(maps[nx][ny])
                      elif maps[nx][ny] == 0:
                          temp.append((nx, ny))
                      maps[nx][ny] = 1001
          visited = temp[:]
          if q :
              print(min(q))
              return
      if not q :
          print(0)
  
  solution()
  
  ```

  > 뭔말인지 모르겠는데 무튼 수시로 목표 좌표에 값이 들어와있는지 확인한다음 값이 있으면 바로 출력해서 시간을 아낀다는 점은 알겠음. 굿.

