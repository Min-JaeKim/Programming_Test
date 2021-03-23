# Python

## baek 14500 테트로미노

https://www.acmicpc.net/problem/14500



> python3 2228ms
>
> pypy3 276ms



* 문제

  > 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
  >
  > - 정사각형은 서로 겹치면 안 된다.
  > - 도형은 모두 연결되어 있어야 한다.
  > - 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
  >
  > 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
  >
  > [![img](md-images/1.png)](https://commons.wikimedia.org/wiki/File:All_5_free_tetrominoes.svg)
  >
  > 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
  >
  > 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
  >
  > 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

* 입력

  > 첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
  >
  > 둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.
  >
  > ```bash
  > 5 5
  > 1 2 3 4 5
  > 5 4 3 2 1
  > 2 3 4 5 6
  > 6 5 4 3 2
  > 1 2 1 2 1
  > ```

* 출력

  > 첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
  >
  > ```bash
  > 19
  > ```



```python
import sys
input = sys.stdin.readline


def stick(m,n):
    global result
    for i in range(m):
        tmp = 0
        for j in range(n):
            tmp += arr[i][j]
            if j >= 3:
                result = max(tmp, result)
                tmp -= arr[i][j - 3]


def square(m,n):
    global result
    for i in range(m-1):
        for j in range(n-1):
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
            result = max(tmp, result)


def l(m,n):
    global result
    for i in range(m-2):
        for j in range(n-1):
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
            result = max(tmp, result)


def l2(m,n): # -┘
    global result
    for i in range(1, m):
        for j in range(n-2):
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+2]
            result = max(tmp, result)


def l3(m,n): #
    global result
    for i in range(m-2):
        for j in range(n-1):
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
            result = max(tmp, result)


def l4(m,n): #
    global result
    for i in range(m-1):
        for j in range(n-2):
            tmp = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i][j+2]
            result = max(tmp, result)


def chair(m,n): #
    global result
    for i in range(m-2):
        for j in range(n-1):
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
            result = max(tmp, result)


def chair2(m,n): #
    global result
    for i in range(m-1):
        for j in range(n-2):
            tmp = arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2]
            result = max(tmp, result)


def cry(m,n):
    global result
    for i in range(m - 1):
        for j in range(n - 2):
            tmp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i+1][j + 1]
            result = max(tmp, result)


def cry2(m,n):
    global result
    for i in range(m - 2):
        for j in range(n - 1):
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j + 1] + arr[i+2][j]
            result = max(tmp, result)


def cry3(m,n):
    global result
    for i in range(m-1):
        for j in range(n-2):
            tmp = arr[i][j+1] + arr[i+1][j] + arr[i+1][j + 1] + arr[i+1][j+2]
            result = max(tmp, result)


def cry4(m,n):
    global result
    for i in range(m-2):
        for j in range(n-1):
            tmp = arr[i][j+1] + arr[i+1][j] + arr[i+1][j + 1] + arr[i+2][j+1]
            result = max(tmp, result)


row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
result = 0

stick(row,col) # 가로 막대기
square(row,col)
l(row,col)
l2(row,col)
l3(row,col)
l4(row,col)
chair(row,col)
chair2(row,col)
cry(row,col)
cry2(row,col)
cry3(row,col)
cry4(row,col)

arr = list(zip(*arr))

stick(col,row)
l(col,row)
l2(col,row)
l3(col,row)
l4(col,row)
chair(col,row)
chair2(col,row)

print(result)
```

> 그냥 노가다성 구현문제.
>
> 단지 머리를 잘 굴려야 할 부분은 함수를 모두 돌리지 말고, 배열을 대각선을 기준으로 대칭해서 돌리면 된다.



* 모범답안

  ```python
  272
  
import sys
  input = sys.stdin.readline
  
  n, m = map(int, input().split())
  paper = [list(map(int, input().split())) for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range(n)]
  direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  max_val = max(max(paper))
  
  answer = 0
  def solution(length, total, r, c):
      global answer
      # 더이상 진행해도 최댓값보다 커질 수 없는 경우
      if(total+max_val*(4-length)<=answer):
          return
      
      # 네칸째 방문일 경우
      if(length==4):
          answer = max(answer, total)
          return
      
      # 각 방향으로 탐색
      for d in direction:
          nr = r+d[0]
          nc = c+d[1]
          # 다음 방문할 칸이 존재하고 아직 방문한적이 없을 경우
          if ((0<=nr<n and 0<=nc<m) and not visited[nr][nc]):
              # 요철형태 처리
              if(length==2):
                  visited[nr][nc] = True
                  solution(length+1, total+paper[nr][nc], r, c)
                  visited[nr][nc] = False
              visited[nr][nc] = True
              solution(length+1, total+paper[nr][nc], nr, nc)
              visited[nr][nc] = False
              
  for r in range(n):
      for c in range(m):
          visited[r][c] = True
          solution(1, paper[r][c], r, c)
          visited[r][c] = False
  print(answer)
  ```
  
  > 미쳤다 이런 생각을 할 수 있는 게 신기하다.