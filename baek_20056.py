# python

## baek 20056 마법사 상어와 파이어볼 골드5

https://www.acmicpc.net/problem/20056

> python3 1524ms
>
> pypy3 564ms



* 문제

  > [어른 상어](https://www.acmicpc.net/problem/19237)가 마법사가 되었고, 파이어볼을 배웠다.
  >
  > 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.
  >
  > 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
  >
  > 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.
  >
  > | 7    | 0    | 1    |
  > | ---- | ---- | ---- |
  > | 6    |      | 2    |
  > | 5    | 4    | 3    |
  >
  > 마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.
  >
  > 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
  >    - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
  > 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
  >    1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
  >    2. 파이어볼은 4개의 파이어볼로 나누어진다.
  >    3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
  >       1. 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
  >       2. 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
  >       3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
  >    4. 질량이 0인 파이어볼은 소멸되어 없어진다.
  >
  > 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

* 입력

  > 첫째 줄에 N, M, K가 주어진다.
  >
  > 둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
  > 
  > 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.
  > 
  > ```python
  > 4 2 1
  > 1 1 5 2 2
  > 1 4 7 1 6
  > ```
  > 
  
* 출력

  > 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.
  >
  > ```python
  > 8
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    n, m, count = map(int, input().split())
    arr = [[[] for _ in range(n)] for _ in range(n)]
    dd = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    def dir(r, c, speed, direction):
        if dd[direction][0] * speed > 0:
            r = (r + dd[direction][0] * speed) % n
        elif dd[direction][0] * speed < 0:
            r = (n + r - (abs(dd[direction][0] * speed) % n)) % n
        if dd[direction][1] * speed > 0:
            c = (c + dd[direction][1] * speed) % n
        elif dd[direction][1] * speed < 0:
            c = (n + c - (abs(dd[direction][1] * speed) % n)) % n
        return r, c

    for _ in range(m):
        r, c, m, s, d = map(int, input().split())
        arr[r-1][c-1].append([r-1, c-1, m, s, d])

    cnt = 0
    while cnt < count:
        arr2 = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j]:
                    for k in range(len(arr[i][j])):
                        arr[i][j][k][0], arr[i][j][k][1] = dir(arr[i][j][k][0], arr[i][j][k][1], arr[i][j][k][3], arr[i][j][k][4])

        for i in range(n):
            for j in range(n):
                if arr[i][j]:
                    for k in range(len(arr[i][j])):
                        arr2[arr[i][j][k][0]][arr[i][j][k][1]].append(arr[i][j][k])

        for i in range(n):
            for j in range(n):
                if len(arr2[i][j]) > 1:
                    mass, speed, oddflag, evenflag = 0, 0, True, True
                    for k in range(len(arr2[i][j])):
                        mass += arr2[i][j][k][2]
                        speed += arr2[i][j][k][3]
                        if arr2[i][j][k][4] % 2 == 0:
                            oddflag = False
                        else:
                            evenflag = False
                    mass //= 5
                    speed //= len(arr2[i][j])

                    for k in range(len(arr2[i][j])):
                        arr2[i][j].remove(arr2[i][j][0])

                    if mass != 0:
                        if oddflag or evenflag:
                            arr2[i][j].append([i, j, mass, speed, 0])
                            arr2[i][j].append([i, j, mass, speed, 2])
                            arr2[i][j].append([i, j, mass, speed, 4])
                            arr2[i][j].append([i, j, mass, speed, 6])
                        else:
                            arr2[i][j].append([i, j, mass, speed, 1])
                            arr2[i][j].append([i, j, mass, speed, 3])
                            arr2[i][j].append([i, j, mass, speed, 5])
                            arr2[i][j].append([i, j, mass, speed, 7])

        cnt += 1
        arr = arr2[:]


    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(len(arr[i][j])):
                result += arr[i][j][k][2]

    print(result)


sol()
```

> 하,, 진짜 오래 걸렸다.. 파이어볼의 개수만 순회할 지, 맵을 전체 순회할 지 고민하다가 맵을 전체 순회하는 걸 골랐는데 걍 구현 뿐인 문제라 엄청 오래 걸렸다.
>
> 그리고 좌표 구하는 것도 저렇게 고심해서 안해도 되나보다;; 모범답안 보면            
>
>  nx, ny = (x + s * dx) % N, (y + s * dy) % N
>
> 걍 이렇게 했네 ;; 신기

* 모범답안

  ```python
  from sys import stdin
  from math import floor
  
  
  def solution(N, M, K, balls):
      DELTA = (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
      balls = list(map(lambda x: (x[0] - 1, x[1] - 1, *x[2:]), balls))
      for _ in range(K):
  
          poses = {}
          for x, y, m, s, d in balls:
              dx, dy = DELTA[d]
              nx, ny = (x + s * dx) % N, (y + s * dy) % N
              poses.setdefault((nx, ny), []).append((m, s, d))
  
          new_balls = []
          for (x, y), vals in poses.items():
              if len(vals) == 1:
                  new_balls.append((x, y, *vals[0]))
                  continue
  
              nm, ns, nd = 0, 0, []
              for m, s, d in vals:
                  nm += m
                  ns += s
                  nd.append(d % 2)
              nm = floor(nm / 5)
              ns = floor(ns / len(vals))
              nd = (0, 2, 4, 6) if all(d == nd[0] for d in nd) else (1, 3, 5, 7)
              if nm != 0:
                  for d in nd:
                      new_balls.append((x, y, nm, ns, d))
  
          balls = new_balls
  
      return sum(map(lambda x: x[2], balls))
  
  
  lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
  N, M, K = lexer()
  balls = [lexer() for _ in range(M)]
  
  print(solution(N, M, K, balls))
  ```

  > - `poses.setdefault((nx, ny), []).append((m, s, d))`
  >
  >   > {(0, 2): [(5, 2, 2), (7, 1, 6)]}
  >
  > 와 근데 진짜 빠르다... 나는 n*n을 다 순회하는데 이사람은 파이어볼의 개수만큼만 순회한다.. 나도 처음엔 이방법을 생각했었는데.. 밀고 나갈 걸 그랬다. 한층 성장할 수 있었던 문제였다고 생각한다..

