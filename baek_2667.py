# python

## baek 2667 단지 번호 붙이기 실버1

https://www.acmicpc.net/problem/2667

> python3 100ms

* 문제

  > <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
  >
  > ![img](md-images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)

* 입력

  > 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
  >
  > ```bash
  >7
  > 0110100
  >0110101
  > 1110101
  >0000111
  > 0100000
  >0111110
  > 0111000
  > ```
  > 
  
* 출력

  > 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
  >
  > ```bash
  > 3
  > 7
  > 8
  > 9
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    res = []

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                q, number, arr[i][j] = deque([[i, j]]), 1, 0

                while q:
                    r, c = q.popleft()

                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < n and 0 <= nc < n and \
                            arr[nr][nc]:
                            q.append([nr, nc])
                            arr[nr][nc] = 0
                            number += 1

                res.append(number)

    res.sort()
    length = len(res)
    print(length)
    for i in range(length):
        print(res[i])


sol()
```

> 



* 모범답안

  ```python
  52
  
  N  = int(input())
  
  arr = []
  
  
  for i in range(N):
      arr.append(list(map(int,list(input()))))
  
  
  
  def bfs(startx,starty):
      num = 1
      queuex = []
      queuey = []
      queuex.append(startx)
      queuey.append(starty)
      arr[startx][starty]=0
      
      while(len(queuex)>0 and len(queuey)>0):
          px = queuex[0]
          del queuex[0]
          py = queuey[0]
          del queuey[0]
  
          if ((py-1)>=0 and arr[px][py-1]==1):
              queuex.append(px)
              queuey.append(py-1)
              arr[px][py - 1] = 0
              num+=1
  
          if ((px-1)>=0 and arr[px-1][py]==1):
              queuex.append(px-1)
              queuey.append(py)
              arr[px - 1][py] = 0
              num+=1
          if (py+1<N and arr[px][py+1]==1):
              queuex.append(px)
              queuey.append(py+1)
              arr[px][py + 1] = 0
              num+=1
          if (px+1<N and arr[px+1][py]==1):
              queuex.append(px+1)
              queuey.append(py)
              arr[px + 1][py] = 0
              num+=1
      return num
  
  
  
  flag = 0
  quantity=[]
  
  for i in range(N):
      for j in range(N):
          if arr[i][j]==1:
              m = bfs(i,j)
              quantity.append(m)
              flag+=1
  
  print(flag)
  quantity.sort()
  for i in range (flag):
      print(quantity[i])
  ```

  > 어차피 for문을 안쓰고 코드를 길게 해서 나열한 것 밖에 없는데 이게 두 배나 속도가 차이가 난다고? 신기하다.

