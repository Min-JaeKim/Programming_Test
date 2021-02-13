# Python

## baek 16918 봄버맨

https://www.acmicpc.net/problem/16918



> 300ms



* 문제

  > [봄버맨](https://en.wikipedia.org/wiki/Bomberman)은 크기가 R×C인 직사각형 격자판 위에서 살고 있다. 격자의 각 칸은 비어있거나 폭탄이 들어있다.
  >
  > 폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며, 인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도 함께 파괴된다. 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.
  >
  > 봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 모든 칸을 자유롭게 이동할 수 있다. 봄버맨은 다음과 같이 행동한다.
  >
  > - 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
  > - 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
  > - 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
  > - 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
  > - 3과 4를 반복한다.
  >
  > 폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다.
  >
  > 예를 들어, 초기 상태가 아래와 같은 경우를 보자.
  >
  > ```
  > ...
  > .O.
  > ...
  > ```
  >
  > 1초가 지난 후에는 아무 일도 벌어지지 않기 때문에, 위와 같다고 볼 수 있다. 1초가 더 흐른 후에 격자판의 상태는 아래와 같아진다.
  >
  > ```
  > OOO
  > OOO
  > OOO
  > ```
  >
  > 1초가 지난 후엔 가운데에 있는 폭탄이 폭발해 가운데 칸과 인접한 네 칸이 빈 칸이 된다.
  >
  > ```
  > O.O
  > ...
  > O.O
  > ```

* 입력

  > 첫째 줄에 R, C, N (1 ≤ R, C, N ≤ 200)이 주어진다. 둘째 줄부터 R개의 줄에 격자판의 초기 상태가 주어진다. 빈 칸은 '`.`'로, 폭탄은 '`O`'로 주어진다.
  >
  > ```bash
  > 6 7 3
  > .......
  > ...O...
  > ....O..
  > .......
  > OO.....
  > OO.....
  > ```

* 출력

  > 총 R개의 줄에 N초가 지난 후의 격자판 상태를 출력한다.
  >
  > ```bash
  > OOO.OOO
  > OO...OO
  > OOO...O
  > ..OO.OO
  > ...OOOO
  > ...OOOO
  > ```



```python
from collections import deque # deque 선언

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(): # bfs함수 미리 선언
    while(len(que) != 0): # que가 비어있지 않으면, (que에는 폭탄이 설치된 좌표만 넣는다)
        x,y = que.popleft() # que를 pop하면서,
        for k in range(4): # 상하좌우 돌며 주변을 '.'으로 찍는다.
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<r and 0<=ny<c): # 상하좌우가 좌표상에 존재하는 좌표라면
                arr[nx][ny] = '.' # 폭발된 상태로 만들어줌

r,c,n = map(int,input().split()) # 가로, 세로, 시간
arr = [list(input()) for _ in range(r)] # 좌표를 담아둘 배열
que = deque([]) # deque로 폭탄 좌표를 담아둠

if n % 2 == 0: # 짝수단위의 초라면,
    for i in range(r): 
        for j in range(c):
            print('O', end ="") # 좌표를 돌며 O로 바꿔줌
        print()

else : # 홀수 단위 초라면
    tmp = 1 # 1초라고 현재상황을 가정하고
    while(tmp != n): # 2초 단위 씩 더해가며 주어진 초에 맞춘다.
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O': # 만약폭탄이 설치된 곳이라면
                    que.append([i, j]) # QUEUE에 넣고,
                    arr[i][j] = '.' # 미리 폭탄 터진 땅으로 만들어줌.(BFS함수에서는 상하좌우만 바꿔줌)
                else : # 만약 폭탄이 설치된 곳이 아니라면
                    arr[i][j] = 'O' # O로 바꿔줌.
        bfs() # BFS함수를 돌려 QUEUE에 들어가 있는 좌표를 해결함
        tmp += 2 # 임시시간을 2초씩 늘려가며 홀수 초에 대해서 계산해줌.
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end ="") # 마지막으로 출력 이중포문
        print()


# 1초 -> 들어온대로
# 2초 -> 모든칸에 0
# 3초 -> 1의 반대
# 4초 -> 모든칸에 0
# 5초 -> 3의 반대
```

> 민재는 멍퉁이 그자체였는데,, 파이참으로 계속 이전에 작성했던 코드를 돌리며 ,, 또 틀렸네,, 또틀렸네 하고 있었다.. 파이참의 함정이었다. 꼭 지금 작성중인 코드를 빌드코드로 바꿔 주는 것을 잊지 말아야겠다.



* 모범답안

  ```python
  direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
  r, c, n = map(int, input().split())
  MAP = [list(input()) for _ in range(r)]
  time = [[-1]*c for _ in range(r)]
  cnt = 0
   
  # 초기화
  for i in range(r):
      for j in range(c):
          if MAP[i][j] == 'O':
              time[i][j] = 0
   
  while cnt != n:
      boom = []
      for i in range(r):
          for j in range(c):
              if MAP[i][j] == '.' and time[i][j] == -1 and cnt != 0: # 0초일땐 무시
                  MAP[i][j] = 'O'
                  time[i][j] = 0
              elif MAP[i][j] == 'O' and time[i][j] < 3:
                  time[i][j] += 1
                  if time[i][j] == 3:
                      boom.append((i,j)) # 폭발 리스트를 만들어서 터지는 폭탄 삽입
   
      for i,j in boom:
          MAP[i][j] = '.'
          time[i][j] = -1
          for d in direction:
              ny = i + d[0]
              nx = j + d[1]
              if 0 <= ny < r and 0 <= nx < c:
                  MAP[ny][nx] = '.'
                  time[ny][nx] = -1
   
      cnt += 1
   
  for m in MAP:
      print(''.join(m))
  
  ```

  > * 방향을 튜플로 정해두셨네
  > * 비슷한 것 같지만 이차원 배열을 하나 더 사용함으로써 나보다 시간이 더 나오신 것 같다.