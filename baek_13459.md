# python

## baek 13459 구슬 탈출 골드3

https://www.acmicpc.net/problem/13459

> python3 188ms



* 문제

  > 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
  >
  > 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
  >
  > 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
  >
  > 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
  >
  > 보드의 상태가 주어졌을 때, 10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '`.`', '`#`', '`O`', '`R`', '`B`' 로 이루어져 있다. '`.`'은 빈 칸을 의미하고, '`#`'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, '`O`'는 구멍의 위치를 의미한다. '`R`'은 빨간 구슬의 위치, '`B`'는 파란 구슬의 위치이다.
  >
  > 입력되는 모든 보드의 가장자리에는 모두 '`#`'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
  >
  > ```bash
  > 5 5
  > #####
  > #..B#
  > #.#.#
  > #RO.#
  > #####
  > ```
  >
  
* 출력

  > 파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 1을 없으면 0을 출력한다.
  >
  > ```bash
  > 1
  > ```



```python
'''
7 7
#######
#...O.#
#.....#
#.....#
#.B...#
#..R..#
#######
0
'''
import sys
from collections import deque
input = sys.stdin.readline

# 1 상, 2 하 , 3 좌, 4 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def move(n, m, arr, dir, cnt):
    if cnt > 10:
        return 0

    if dir == 1:
        red, blue = False, False

        for i in range(1, n-1):
            for j in range(1, m-1):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    v = [[0] * m for _ in range(n)]
                    if arr[i][j] == 'R':
                        q = deque([[i, j, 'R']])
                    if arr[i][j] == 'B':
                        q = deque([[i, j, 'B']])
                    arr[i][j] = '.'
                    v[i][j] = 1

                    while q:
                        r, c, color = q.popleft()

                        if arr[r][c] == 'O':
                            if color == 'R':
                                red = True
                            else:
                                blue = True
                            break

                        if 0 <= r - 1 and not v[r-1][c]:
                            if arr[r-1][c] == '.' or arr[r-1][c] == 'O':
                                v[r-1][c] = 1
                                q.append([r-1, c, color])
                            else:
                                arr[r][c] = color

        if blue:
            return 0

        if not red:
            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 3, cnt + 1):
                return 1

            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 4, cnt + 1):
                return 1
        else:
            return 1

    elif dir == 2:
        red, blue = False, False

        for i in range(n-2, 0, -1):
            for j in range(1, m-1):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    v = [[0] * m for _ in range(n)]
                    if arr[i][j] == 'R':
                        q = deque([[i, j, 'R']])
                    if arr[i][j] == 'B':
                        q = deque([[i, j, 'B']])
                    arr[i][j] = '.'
                    v[i][j] = 1

                    while q:
                        r, c, color = q.popleft()

                        if arr[r][c] == 'O':
                            if color == 'R':
                                red = True
                            else:
                                blue = True
                            break

                        if r + 1 < n and not v[r+1][c]:
                            if arr[r + 1][c] == '.' or arr[r + 1][c] == 'O':
                                v[r+1][c] = 1
                                q.append([r + 1, c, color])
                            else:
                                arr[r][c] = color
        if blue:
            return 0

        if not red:
            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 3, cnt + 1):
                return 1

            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 4, cnt + 1):
                return 1
        else:
            return 1

    elif dir == 3:
        red, blue = False, False

        for i in range(1, n-1):
            for j in range(1, m-1):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    v = [[0] * m for _ in range(n)]
                    if arr[i][j] == 'R':
                        q = deque([[i, j, 'R']])
                    if arr[i][j] == 'B':
                        q = deque([[i, j, 'B']])
                    arr[i][j] = '.'
                    v[i][j] = 1

                    while q:
                        r, c, color = q.popleft()

                        if arr[r][c] == 'O':
                            if color == 'R':
                                red = True
                            else:
                                blue = True
                            break

                        if 0 <= c - 1 and not v[r][c-1]:
                            if arr[r][c-1] == '.' or arr[r][c-1] == 'O':
                                v[r][c-1] = 1
                                q.append([r, c-1, color])
                            else:
                                arr[r][c] = color

        if blue:
            return 0

        if not red:
            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 1, cnt + 1):
                return 1

            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 2, cnt + 1):
                return 1
        else:
            return 1

    else:
        red, blue = False, False

        for i in range(1, n-1):
            for j in range(m-2, 0, -1):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    v = [[0] * m for _ in range(n)]
                    if arr[i][j] == 'R':
                        q = deque([[i, j, 'R']])
                    if arr[i][j] == 'B':
                        q = deque([[i, j, 'B']])
                    arr[i][j] = '.'
                    v[i][j] = 1

                    while q:
                        r, c, color = q.popleft()

                        if arr[r][c] == 'O':
                            if color == 'R':
                                red = True
                            else:
                                blue = True
                            break

                        if c + 1 < m and not v[r][c+1]:
                            if arr[r][c + 1] == '.' or arr[r][c + 1] == 'O':
                                v[r][c+1] = 1
                                q.append([r, c + 1, color])
                            else:
                                arr[r][c] = color

        if blue:
            return 0

        if not red:
            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 1, cnt + 1):
                return 1

            arr_tmp = []
            for i in range(n):
                arr_tmp.append(arr[i][:])

            if move(n, m, arr_tmp, 2, cnt + 1):
                return 1
        else:
            return 1

    return 0


def sol():
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]

    arr_tmp = []
    for i in range(n):
        arr_tmp.append(arr[i][:])

    if move(n, m, arr_tmp, 1, 1):
        return 1

    arr_tmp = []
    for i in range(n):
        arr_tmp.append(arr[i][:])

    if move(n, m, arr_tmp, 2, 1):
        return 1

    arr_tmp = []
    for i in range(n):
        arr_tmp.append(arr[i][:])

    if move(n, m, arr_tmp, 3, 1):
        return 1

    arr_tmp = []
    for i in range(n):
        arr_tmp.append(arr[i][:])

    if move(n, m, arr_tmp, 4, 1):
        return 1

    return 0


print(sol())
```

> 이걸 대체 몇날 며칠 풀었는지,,
>
> 우선 제일 먼저 나의 발목을 잡았던 건, 리스트의 변화되는 속성 때문이었다.현재 리스트를 함수에 넣어서 그 함수에서 해당 리스트를 변형시키면, 그 함수를 빠져나왔을 때도 여전희 변화된 값으로 존재 한다는 것이다. 이를 막기 위해 새로운 임시 리스트를 만들어줬어야 했다. 해당 리스트와 똑같은, 하지만 메모리 주소는 다른 새로운 리스트를 만들고 해당 리스트를 변형해 주었다.
>
> 또 두번째로 나를 힘들 게 한 건 if문에서 break을 통한 while 반복문 빠져나오기. 첫번째 if문에서는 적어 줬는데 왜 그다음 if문에서는 안적어줬는지 모를일
>
> 세번째는 flag,, 빨구와 파구 모두 구멍에 들어갔을 때 통합하여 res flag를 두었다. 빨구가 들어가면 true고 파구가 들어가면 false다. 그렇게 하다보니, 파구가 구멍에 들어가서 false가 됐을 때 다음 함수로 진행되어 해당 함수에서 빨구가 들어가면 true가 되기 때문에 정답이 아닌데도 정답처리를 하는 것이다. 그래서 res를 정리하기 귀찮아서 파구가 구멍에 들어갔을 때를 처리하는 파구 flag를 만들었는데, 웬열 80퍼에서 틀렸다. 고민하다가 두 개 다 통합된 flag를 없애고 빨구 flag와 파구 flag를 완전히 나눠버렸다. 그러니까 정답이 떴음. 참,,
>
> 디버깅도 열심히 하고 삽질도 열심히 시간낭비도 열심히 했던 문제. 그래도 나에게 얻어진 건 있을 거야.



* 모범답안

  ```python
  60
  
  N, M = map(int, input().split())
  arr = [list(input().strip()) for _ in range(N)]
  check = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  
  dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
  
  
  queue = []
  
  def init():
      _rx, _ry, _bx, _by = [0] * 4
      for i in range(N):
          for j in range(M):
              if arr[i][j] == 'R':
                  _rx, _ry = i, j
              elif arr[i][j] == 'B':
                  _bx, _by = i, j
      queue.append((_rx, _ry, _bx, _by, 0))    
      check[_rx][_ry][_bx][_by] = True
  
  def move(_x, _y, _dx, _dy, _c):
      while arr[_x + _dx][_y + _dy] != '#' and arr[_x][_y] != 'O':
          _x += _dx
          _y += _dy
          _c += 1
      return _x, _y, _c
  
  def bfs():
      while queue:
          rx, ry, bx, by, d = queue.pop(0)
          if d >= 10:
              break
          for i in range(4):
              nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
              nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
              if arr[nbx][nby] == 'O':
                  continue
              if arr[nrx][nry] == 'O':
                  print(1)
                  return
              if nrx == nbx and nry == nby:
                  if rc > bc:
                      nrx, nry = nrx-dx[i], nry-dy[i]
                  else:
                      nbx, nby = nbx-dx[i], nby-dy[i]
              if not check[nrx][nry][nbx][nby]:
                  check[nrx][nry][nbx][nby] = True
                  queue.append((nrx, nry, nbx, nby, d+1))
      print(0)
  
  init()
  bfs()
  ```
  
  > 우선 4차원 배열을 통해 빨구 파구가 기울일 때마다 같은 위치에 있지 않도록 해줬음
  >
  > 현재 위치에서 상하좌우 움직이며 그 위치가 구멍인지 아닌지 판별해 줌. (이러면 리스트를 변환할 필요가 없으니, 내가 임시 리스트를 생성해 준 것이 필요 없음)
  >
  > 또한 둘이 만약 겹치는 위치에 있다면, 덜 움직인 애가 뒤에 있어야 하므로 그것도 if문으로 조정시켜 줌.
  >
  > 이렇게 풀면 되는군,, 신기하다. 내가 이런문제를 또 만나게 되면 이렇게 풀 수 있을까?

