# python

## baek 10026 카드 정렬하기 골드5

https://www.acmicpc.net/problem/10026

> python3 120ms



* 문제

  > 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
  >
  > 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
  >
  > 예를 들어, 그림이 아래와 같은 경우에
  >
  > ```
  > RRRBB
  > GGBBB
  > BBBRR
  > BBRRR
  > RRRRR
  > ```
  >
  > 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
  >
  > 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
  >
  > 둘째 줄부터 N개 줄에는 그림이 주어진다.
  >
  > ```bash
  > 5
  > RRRBB
  > GGBBB
  > BBBRR
  > BBRRR
  > RRRRR
  > ```
  >
  
* 출력

  > 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
  >
  > ```bash
  > 4 3
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    n = int(input())
    arr = [list(input().strip()) for _ in range(n)]
    v, v2, res, res2 = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)], 0, 0

    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                alpha, q, v[i][j] = arr[i][j], deque([[i, j]]), 1
                res += 1

                while q:
                    r, c = q.popleft()

                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] and arr[nr][nc] == alpha:
                            q.append([nr, nc])
                            v[nr][nc] = 1

            if not v2[i][j]:
                alpha, q, v2[i][j] = arr[i][j], deque([[i, j]]), 1
                res2 += 1

                while q:
                    r, c = q.popleft()

                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n and not v2[nr][nc]:
                            if alpha == 'R' or alpha == 'G':
                                if arr[nr][nc] == 'R' or arr[nr][nc] == 'G':
                                    q.append([nr, nc])
                                    v2[nr][nc] = 1
                            else:
                                if alpha == arr[nr][nc]:
                                    q.append([nr, nc])
                                    v2[nr][nc] = 1

    print(res, res2)


sol()
```

> 아 분명 이것보다 더 현명하게 푸는 방법이 있을 것 같은데 그냥 이렇게 풀엇다



* 모범답안

  ```python
  72
  import sys
  
  sys.setrecursionlimit(10**5)
  n=int(input())
  a=[[" "]*(n+2)]+[list(" "+input()+" ")for i in[0]*n]+[[" "]*(n+2)]
  b=[i.copy()for i in a]
  def cnt(s,x,y,c):
      s[x][y]=" "
      if s[x-1][y]==c:cnt(s,x-1,y,c)
      if s[x+1][y]==c:cnt(s,x+1,y,c)
      if s[x][y-1]==c:cnt(s,x,y-1,c)
      if s[x][y+1]==c:cnt(s,x,y+1,c)
  c=d=0
  for i in range(1,n+1):
      for j in range(1,n+1):
          if a[i][j]!=" ":
              cnt(a,i,j,a[i][j]);c+=1
  for i in range(1,n+1):
      for j in range(1,n+1):
          if b[i][j]=="G":b[i][j]="R"
  for i in range(1,n+1):
      for j in range(1,n+1):
          if b[i][j]!=" ":
              cnt(b,i,j,b[i][j]);d+=1
  print(c,d)
  ```
  
  > 왜 나보다 빠른 걸까 비슷하게 푼 것 같은데

