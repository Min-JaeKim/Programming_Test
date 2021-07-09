# python

## baek 18428 감시 피하기 실버1

https://www.acmicpc.net/problem/18428

> python3 72ms
>



* 문제

  > *N*x*N* 크기의 복도가 있다. 복도는 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다. 현재 몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.
  >
  > 각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다. 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.
  >
  > 다음과 같이 3x3 크기의 복도의 정보가 주어진 상황을 확인해보자. 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다. 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시하였다. 아래 그림과 같이 (3,1)의 위치에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다. 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다. 
  >
  > ![img](md-images/preview)
  >
  > 이 때 (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어 있기 때문에 감시를 피할 수 있다. 하지만 (1,1)과 (2,1)의 위치에 존재하는 학생은 선생님에게 들키게 된다.
  >
  > 학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다. 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산하고자 한다. *N*x*N* 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.
  >
  > 예를 들어 *N*=5일 때, 다음과 같이 선생님 및 학생의 위치 정보가 주어졌다고 가정하자.
  >
  > ![img](md-images/preview)
  >
  > 이 때 다음과 같이 3개의 장애물을 설치하면, 모든 학생들을 선생님의 감시로부터 피하도록 만들 수 있다.
  >
  > ![img](md-images/preview)

* 입력

  > 첫째 줄에 자연수 *N*이 주어진다. (3 ≤ *N* ≤ 6) 둘째 줄에 *N*개의 줄에 걸쳐서 복도의 정보가 주어진다. 각 행에서는 *N*개의 원소가 공백을 기준으로 구분되어 주어진다. 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
  >
  > 단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.
  >
  > ```bash
  >5
  > X S X X T
  > T X S X X
  > X X X X X
  > X T X X X
  > X X T X X
  > ```
  > 
  
* 출력

  > 첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다. 모든 학생들을 감시로부터 피하도록 할 수 있다면 "`YES`", 그렇지 않다면 "`NO`"를 출력한다.
  >
  > ```bash
  > YES
  > ```



```python
import sys
input = sys.stdin.readline
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    ob = 3 # 장애물 개수

    for i in range(n):
        for j in range(n):

            if arr[i][j] == 'T':
                # 선생을 만나면
                for k in range(4):
                    # 네 방향 돌면서
                    nr, nc, flag, obx = i, j, 0, 0

                    while 0 <= nr < n and 0 <= nc < n:
                        # S를 찾으면 돌고 있던 이전 좌표가
                        # 자기 자신이었는지 확인하고,
                        # 자기 자신이 아니었다면,
                        # 장애물이 남아 있는지 확인하고
                        # 장애물 설치.
                        # 그 외에는 NO 출력 후 종료.
                        if arr[nr][nc] == 'S':
                            flag = 1
                            nr, nc = nr - dr[k], nc - dc[k]
                            if arr[nr][nc] == 'T':
                                obx = 1
                            break
                        if arr[nr][nc] == 'O':
                            break
                        nr, nc = nr + dr[k], nc + dc[k]

                    if flag:
                        if ob and not obx:
                            arr[nr][nc] = 'O'
                            ob -= 1
                        else:
                            print('NO')
                            exit()

    print('YES')


sol()
```

> 



* 모범답안

  ```python
  64
  
  import itertools
  
  
  def bfs():
      for x, y in t:
          for i in range(x+1, N):
              if cls[i][y] == 'O':
                  break
              if cls[i][y] == 'S':
                  return False
          for j in range(y+1, N):
              if cls[x][j] == 'O':
                  break
              if cls[x][j] == 'S':
                  return False
          for i in range(x-1, -1, -1):
              if cls[i][y] == 'O':
                  break
              if cls[i][y] == 'S':
                  return False
          for j in range(y-1, -1, -1):
              if cls[x][j] == 'O':
                  break
              if cls[x][j] == 'S':
                  return False
      return True
  
  
  N = int(input())
  teacher = [set() for i in range(N)]
  cls = [list(input().split()) for _ in range(N)]
  t = []
  for i in range(N):
      for j in range(N):
          if cls[i][j] == 'T':
              t.append((i, j))
              if i > 0 and cls[i-1][j] == 'X':
                teacher[i-1].add(j)
              if j > 0 and cls[i][j-1] == 'X':
                  teacher[i].add(j-1)
              if i < N-1 and cls[i+1][j] == 'X':
                  teacher[i+1].add(j)
              if j < N-1 and cls[i][j+1] == 'X':
                  teacher[i].add(j+1)
  
  candi = []
  for i in range(N):
      for j in teacher[i]:
          candi.append((i, j))
  #print(candi)
  for combi in itertools.combinations(candi, 3):
      for x, y in combi:
          cls[x][y] = 'O'
      if bfs():
          print("YES")
          exit()
      for x, y in combi:
          cls[x][y] = 'X'
  print("NO")
  ```
  
  > 가능한 조건을 따져 조합을 썼다. 심지어 예시랑 장애물 설치 위치도 다르다. 이게 어떻게 통과가 되었지 싶지만 로직상 틀린 게 없다. 그런데 조합을 썼는데 어떻게 나보다 빠를까? 대단..

