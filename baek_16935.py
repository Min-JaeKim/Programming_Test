# Python

## baek 16935 배열 돌리기 3 실버3

https://www.acmicpc.net/problem/16935



> pypy3 284ms
>
> python3 2020ms



* 문제

  > 크기가 N×M인 배열이 있을 때, 배열에 연산을 R번 적용하려고 한다. 연산은 총 6가지가 있다.
  >
  > 1번 연산은 배열을 상하 반전시키는 연산이다.
  >
  > ```
  > 1 6 2 9 8 4 → 4 2 9 3 1 8
  > 7 2 6 9 8 2 → 9 2 3 6 1 5
  > 1 8 3 4 2 9 → 7 4 6 2 3 1
  > 7 4 6 2 3 1 → 1 8 3 4 2 9
  > 9 2 3 6 1 5 → 7 2 6 9 8 2
  > 4 2 9 3 1 8 → 1 6 2 9 8 4
  >    <배열>       <연산 결과>
  > ```
  >
  > 2번 연산은 배열을 좌우 반전시키는 연산이다.
  >
  > ```
  > 1 6 2 9 8 4 → 4 8 9 2 6 1
  > 7 2 6 9 8 2 → 2 8 9 6 2 7
  > 1 8 3 4 2 9 → 9 2 4 3 8 1
  > 7 4 6 2 3 1 → 1 3 2 6 4 7
  > 9 2 3 6 1 5 → 5 1 6 3 2 9
  > 4 2 9 3 1 8 → 8 1 3 9 2 4
  >    <배열>       <연산 결과>
  > ```
  >
  > 3번 연산은 오른쪽으로 90도 회전시키는 연산이다.
  >
  > ```
  > 1 6 2 9 8 4 → 4 9 7 1 7 1
  > 7 2 6 9 8 2 → 2 2 4 8 2 6
  > 1 8 3 4 2 9 → 9 3 6 3 6 2
  > 7 4 6 2 3 1 → 3 6 2 4 9 9
  > 9 2 3 6 1 5 → 1 1 3 2 8 8
  > 4 2 9 3 1 8 → 8 5 1 9 2 4
  >    <배열>       <연산 결과>
  > ```
  >
  > 4번 연산은 왼쪽으로 90도 회전시키는 연산이다.
  >
  > ```
  > 1 6 2 9 8 4 → 4 2 9 1 5 8
  > 7 2 6 9 8 2 → 8 8 2 3 1 1
  > 1 8 3 4 2 9 → 9 9 4 2 6 3
  > 7 4 6 2 3 1 → 2 6 3 6 3 9
  > 9 2 3 6 1 5 → 6 2 8 4 2 2
  > 4 2 9 3 1 8 → 1 7 1 7 9 4
  >    <배열>       <연산 결과>
  > ```
  >
  > 5, 6번 연산을 수행하려면 배열을 크기가 N/2×M/2인 4개의 부분 배열로 나눠야 한다. 아래 그림은 크기가 6×8인 배열을 4개의 그룹으로 나눈 것이고, 1부터 4까지의 수로 나타냈다.
  >
  > ```
  > 1 1 1 1 2 2 2 2
  > 1 1 1 1 2 2 2 2
  > 1 1 1 1 2 2 2 2
  > 4 4 4 4 3 3 3 3
  > 4 4 4 4 3 3 3 3
  > 4 4 4 4 3 3 3 3
  > ```
  >
  > 5번 연산은 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산이다.
  >
  > ```
  > 3 2 6 3 1 2 9 7 → 2 1 3 8 3 2 6 3
  > 9 7 8 2 1 4 5 3 → 1 3 2 8 9 7 8 2
  > 5 9 2 1 9 6 1 8 → 4 5 1 9 5 9 2 1
  > 2 1 3 8 6 3 9 2 → 6 3 9 2 1 2 9 7
  > 1 3 2 8 7 9 2 1 → 7 9 2 1 1 4 5 3
  > 4 5 1 9 8 2 1 3 → 8 2 1 3 9 6 1 8
  >      <배열>            <연산 결과>
  > ```
  >
  > 6번 연산은 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산이다.
  >
  > ```
  > 3 2 6 3 1 2 9 7 → 1 2 9 7 6 3 9 2
  > 9 7 8 2 1 4 5 3 → 1 4 5 3 7 9 2 1
  > 5 9 2 1 9 6 1 8 → 9 6 1 8 8 2 1 3
  > 2 1 3 8 6 3 9 2 → 3 2 6 3 2 1 3 8
  > 1 3 2 8 7 9 2 1 → 9 7 8 2 1 3 2 8
  > 4 5 1 9 8 2 1 3 → 5 9 2 1 4 5 1 9
  >      <배열>            <연산 결과>
  > ```

* 입력

  > 첫째 줄에 배열의 크기 N, M과 수행해야 하는 연산의 수 R이 주어진다.
  >
  > 둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.
  >
  > 마지막 줄에는 수행해야 하는 연산이 주어진다. 연산은 공백으로 구분되어져 있고, 문제에서 설명한 연산 번호이며, 순서대로 적용시켜야 한다.
  >
  > - 2 ≤ N, M ≤ 100
  > - 1 ≤ R ≤ 1,000
  > - N, M은 짝수
  > - 1 ≤ Aij ≤ 108
  >
  > ```bash
  > 6 8 1
  > 3 2 6 3 1 2 9 7
  > 9 7 8 2 1 4 5 3
  > 5 9 2 1 9 6 1 8
  > 2 1 3 8 6 3 9 2
  > 1 3 2 8 7 9 2 1
  > 4 5 1 9 8 2 1 3
  > 1
  > ```

* 출력

  > 입력으로 주어진 배열에 R개의 연산을 순서대로 수행한 결과를 출력한다.
  >
  > ```bash
  > 4 5 1 9 8 2 1 3
  > 1 3 2 8 7 9 2 1
  > 2 1 3 8 6 3 9 2
  > 5 9 2 1 9 6 1 8
  > 9 7 8 2 1 4 5 3
  > 3 2 6 3 1 2 9 7
  > ```



```python
n,m,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
que = list(map(int, input().split()))
while r > 0:
    if len(que) > 0:
        count = que.pop(0)
    if count == 1:
        for i in range(n//2):
            arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    elif count == 2:
        for i in range(n):
            for j in range(m//2):
                arr[i][j],arr[i][m-j-1] = arr[i][m-j-1],arr[i][j]
    elif count == 3:
        n,m = m,n # 8 6
        copy = [[0] * m for _ in range(n)]
        for i in range(n): # 8
            for j in range(m): # 6
                copy[i][j] = arr[m-j-1][i]
        arr = copy[:]
    elif count == 4:
        n, m = m, n  # 8 6
        copy = [[0] * m for _ in range(n)]
        for i in range(n):  # 8
            for j in range(m):  # 6
                copy[i][j] = arr[j][n-1-i]
        arr = copy[:]
    elif count == 5:
        copy = [[0] * m for _ in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                copy[i][j+m//2] = arr[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                copy[i+n//2][j] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                copy[i][j-m//2] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                copy[i-n//2][j] = arr[i][j]
        arr = copy[:]
    elif count == 6:
        copy = [[0] * m for _ in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                copy[i+n//2][j] = arr[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                copy[i][j-m//2] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                copy[i-n//2][j] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                copy[i][j+m//2] = arr[i][j]
        arr = copy[:]
    r -= 1

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()

# 00 01 02 03 n = 3 m = 4
# 10 11 12 13
# 20 21 22 23
#
# 20 10 00 n = 4 m = 3
# 21 11 01
# 22 12 02
# 23 13 03

# 03 13 23
# 02 12 22
# 01 11 21
# 00 10 20
```

> 어떻게,, 파이썬3과 파이파이3이 10배 가까이 차이나지..?
>
> 별 문제 아닌데 머릿속으로 시뮬레이션 안돌려 보고 대충대충 처리하려고 해서 3시간이나 푼듯,, 
>
> 처음부터 문제를 꼼꼼히 보는 습관을 들이자



* 모범답안

  ```python
  1000ms 정도
  import sys
  from collections import deque
  
  input = sys.stdin.readline
  N, M, K = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  
  
  def operation(op_num):
      global board, N, M
      tmp_board = deque()
      if op_num == 1:
          for row in board:
              tmp_board.appendleft(row)
      elif op_num == 2:
          for row in board:
              tmp_board.append(row[::-1])
      elif op_num == 3:
          tmp_board = [[] for _ in range(M)]
          for r in range(N - 1, -1, -1):
              for c in range(M):
                  tmp_board[c].append(board[r][c])
          N, M = M, N
      elif op_num == 4:
          tmp_board = [[] for _ in range(M)]
          for r in range(N):
              for c in range(M - 1, -1, -1):
                  tmp_board[M - c - 1].append(board[r][c])
          N, M = M, N
      elif op_num == 5:
          tmp_board = [[] for _ in range(N)]
          for r in range(N // 2, N):
              for c in range(0, M // 2):
                  tmp_board[r - N // 2].append(board[r][c])
          for r in range(0, N // 2):
              for c in range(0, M // 2):
                  tmp_board[r].append(board[r][c])
          for r in range(N // 2, N):
              for c in range(M // 2, M):
                  tmp_board[r].append(board[r][c])
          for r in range(0, N // 2):
              for c in range(M // 2, M):
                  tmp_board[r + N // 2].append(board[r][c])
      elif op_num == 6:
          tmp_board = [[] for _ in range(N)]
          for r in range(0, N // 2):
              for c in range(M // 2, M):
                  tmp_board[r].append(board[r][c])
          for r in range(N // 2, N):
              for c in range(M // 2, M):
                  tmp_board[r - N // 2].append(board[r][c])
          for r in range(0, N // 2):
              for c in range(0, M // 2):
                  tmp_board[r + N // 2].append(board[r][c])
          for r in range(N // 2, N):
              for c in range(0, M // 2):
                  tmp_board[r].append(board[r][c])
      board = tmp_board
  
  
  op_list = list(map(int, input().split()))
  for op in op_list:
      operation(op)
  for row in board:
      for item in row:
          print(item, end=' ')
      print()
  ```

  > 함수로 짜셨는데 대박이다. 내장함수 활용을 엄청 잘하셨다.
  >
  > * __appendleft__ : 왼쪽에다 넣기
  > * __tmp_board.append(row[::-1])__ : 한 행 씩 뒤집어서 출력한다음 배열에 넣었음