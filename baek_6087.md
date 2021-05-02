# python

## baek 6087 레이저 통신 골드4

https://www.acmicpc.net/problem/2631

> python3 1816ms
>
> pypy3 356ms



* 문제

  > 크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 '`C`'로 표시되어 있는 칸이다.
  >
  > '`C`'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.
  >
  > 레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('`/`', '`\`')을 설치해서 방향을 90도 회전시킬 수 있다. 
  >
  > 아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '`.`', 벽은 '`*`'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 '`C`'를 연결한 것이다.
  >
  > ```
  > 7 . . . . . . .         7 . . . . . . .
  > 6 . . . . . . C         6 . . . . . /-C
  > 5 . . . . . . *         5 . . . . . | *
  > 4 * * * * * . *         4 * * * * * | *
  > 3 . . . . * . .         3 . . . . * | .
  > 2 . . . . * . .         2 . . . . * | .
  > 1 . C . . * . .         1 . C . . * | .
  > 0 . . . . . . .         0 . \-------/ .
  >   0 1 2 3 4 5 6           0 1 2 3 4 5 6
  > ```

* 입력

  > 첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)
  >
  > 둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.
  >
  > - `.`: 빈 칸
  > - `*`: 벽
  > - `C`: 레이저로 연결해야 하는 칸
  >
  > '`C`'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.
  >
  > ```python
  > 7 8
  > .......
  > ......C
  > ......*
  > *****.*
  > ....*..
  > ....*..
  > .C..*..
  > .......
  > ```
  >
  > 

* 출력

  > 첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.
  >
  > ```python
  > 3
  > ```



- 첫 번째 시도 1816

```python
from collections import deque
import sys
input = sys.stdin.readline


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
dir = (0, 1, 2, 3)  # 상하좌우


def sol():
    w, h = map(int, input().split())
    arr, v = [], [[float('inf')] * w for _ in range(h)]
    laser, res = [], float('inf')
    for i in range(h):
        arr.append(list(input()))
        for j in range(w):
            if 'C' == arr[i][j]:
                laser.append([i, j])

    q = deque([[laser[0][0], laser[0][1], -1, 0]])
    v[laser[0][0]][laser[0][1]] = 0
    while q:
        r, c, d, cnt = q.popleft()
        if r == laser[1][0] and c == laser[1][1]:
            res = min(res, cnt-1)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] != '*':
                ncnt = cnt
                if i != d:
                    ncnt = cnt + 1
                if ncnt <= v[nr][nc]:
                    q.append([nr, nc, i, ncnt])
                    v[nr][nc] = ncnt

    print(res)


sol()
```

> 처음에 다양한 시도를 했었다. 방문 표시를 만들었는데 최소 거울로 목적지까지 가기에 분명 겹치는 동선들이 있기 때문이었다. 그래서 현재 갈 곳인 거리와 겹치는 방향이 중복되지 않도록 했다. 이것도 오류가 있었다. 최소 거울, 같은 방향으로 또 그 지점을 들를 수 있기 때문이었다. 그래서 고안해낸 게 최소 거울 개수를 v배열에 적는 거다. 현재 갈 지점보다 내가 사용한 거울이 많으면 지나가지 않고 빠져나오기.. 결론적으로 이 방법은 성공이었다. 그런데 시간이 엄청 오래 걸렸다.

- 두번째 방법 108

```python
'''
7 8
.......
......C
.......
*****.C
....*..
....*..
....*..
.......
'''

from collections import deque
import sys
input = sys.stdin.readline


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    w, h = map(int, input().split())
    arr, v = [], [[float('inf')] * w for _ in range(h)]
    laser, res = [], float('inf')
    for i in range(h):
        arr.append(list(input()))
        for j in range(w):
            if 'C' == arr[i][j]:
                laser.append([i, j])

    q = deque([[laser[0][0], laser[0][1]]])
    v[laser[0][0]][laser[0][1]] = 0
    while q:
        # bfs. deque를 사용.
        r, c = q.popleft()
        if r == laser[1][0] and c == laser[1][1]:
            res = min(v[r][c]-1, res)
            # 목표지점에 도달했을 때 결과값 갱신
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            while 0 <= nr < h and 0 <= nc < w and arr[nr][nc] != '*':
                # 범위 내에서 쭉 직진을 하면서 (최소 거울로 갈 수 있는 거리 갱신)
                if v[r][c] + 1 > v[nr][nc]:
                    # 만약 기록된 거울 개수보다 현재 사용한 거울 개수가 크다면
                    break
                    # 빠져나감.
                q.append([nr, nc])
                v[nr][nc] = v[r][c] + 1
                nr, nc = nr + dr[i], nc + dc[i]
                # 직진을 하며 거울 개수 갱신

    print(res)


sol()
```

> 애초에 사용한 거울 개수를 함께 q에 넣지 않고 v에 기록하는 거다. 그리고 진행하는 방향도 while로 했다. while로 직진을 해가며 장애물이나 범위를 뚫고 나가지 않은 동안에 계속 q에 거쳐온 지점과 지점의 v를 최솟값으로 갱신해 주는 것.
>
> 이건 다른 사람 풀이를 참조한 거라 왜 짧게 나왔는지 납득을 못함,, 단순히 생각하기에 직진을 하면서 빠르게 현재 가야할 곳들을 최소 거울로 만들어 주기 때문인 것 같은데,,, 본질적으로는 그게 그렇게 크게 시간이 차이날 법한 일인가 의문이 생기기도,,

* 모범답안

  ```python
  
  ```

  > 

