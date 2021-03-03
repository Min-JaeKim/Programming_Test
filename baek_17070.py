# Python

## baek 17070 파이프 옮기기 1 골드5

https://www.acmicpc.net/problem/17070



> pypy3 944ms



* 문제

  > 유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.
  >
  > 오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.
  >
  > ![img](md-images/preview)
  > 
  > 파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.
  > 
  > ![img](md-images/preview)
  > 
  > 파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.
  >    
  > 파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.
  >
  > 파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.
  >
  > 아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.
  > 
  > ![img](md-images/preview)
  > 
  > 가로
  > 
  > ![img](md-images/preview)
  >    
  > 세로
  >
  > ![img](md-images/preview)
  >
  > 대각선
  > 
  > 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.
  
* 입력

  > 첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.
  >
  > ```bash
  > 6
  > 0 0 0 0 0 0
  > 0 1 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > ```

* 출력

  > 첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.
  >
  > ```bash
  > 13
  > ```

* 제한

  >- 3 ≤ N, M ≤ 50
  >- 1 ≤ K ≤ 6
  >- 1 ≤ A[i][j] ≤ 100
  >- 1 ≤ s
  >- 1 ≤ r-s < r < r+s ≤ N
  >- 1 ≤ c-s < c < c+s ≤ M

```python
from datetime import datetime
import sys
input = sys.stdin.readline
dr = [0, 1, 1] # → ↘ ↓
dc = [1, 1, 0]

def move(r, c, flag):
    global result
    if r == n-1 and c == n-1:
        result += 1
        return
    if flag == 0:
        nr = r + dr[0]
        nc = c + dc[0]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            move(nr, nc, 0)
        else :
            return
        if 0 <= r+1 < n and 0 <= c+1 < n:
            if arr[r+1][c] == 0 and arr[r+1][c+1] == 0:
                move(r+1, c+1, 1)
        else:
            return

    elif flag == 1:
        diag = True
        nr = r + dr[0] # 가로
        nc = c + dc[0]
        if 0 <= nr < n and 0 <= nc < n:
            if arr[nr][nc] == 0:
                move(nr, nc, 0)
            else :
                diag = False
        nr, nc = r + dr[2], c + dc[2]
        if 0 <= nr < n and 0 <= nc < n :
            if arr[nr][nc] == 0:
                move(nr, nc, 2)
            else:
                diag = False
        if diag:
            nr, nc = r + dr[1], c + dc[1]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 0:
                    move(nr, nc, 1)
                else:
                    return
        else: return

    else:
        nr = r + dr[2]
        nc = c + dc[2]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            move(nr, nc, 2)
        else :
            return
        if 0 <= r+1 < n and 0 <= c+1 < n:
            if arr[r][c+1] == 0 and arr[r+1][c+1] == 0:
                move(r+1, c+1, 1)
        else:
            return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
start = datetime.now()
flag = 0 # 0 가로 1 대각선 2 세로
result =0
move(0,1,0)
print(result)
print(datetime.now() - start)
```

> 정말 정말 또 불태웠다. 나는 진짜 코테 풀 때 불태우기만 하는듯 ㅋ ㅋ
>
> 우선 시간초과가 계속 떴다. 내가 빠뜨리고 있던 함정은 
>
> 1. 대각선을 생각할 때, 가로 세로 대각선 모두 갈 수 있는 범위 내에 있고, 벽이 아닌지 따지면서 for문을 썼다. 즉, 재귀로 진입을 해서 for문을 쓰는 것 때문에 시간 초과가 걸린 것으로 보인다.
> 2. 그리고 visited를 안써줘도 된다. 어차피 재귀로 도는데 방문 표시가 쓸모 없다. 방문 표시했다가 재귀를 return하면 방문을 풀어 주는 것 자체가 무의미하다. 시간에는 큰 영향이 없긴 하다.
>
> 나름 로직은 다른 dfs 사람들과 비슷했지만서도 내가 아직까지 복잡하게 짜는 것 같다. 그런 습관을 버려야겠다.



* 모범답안

  ```python
  python3 80
  
  n = int(input())
  graph = [[] for _ in range(n)]
  
  # 0은 가로, 1은 세로, 2는 대각선
  dp = [[[0] * n for _ in range(n)] for _ in range(3)]
  
  # 그래프 정보 입력
  for i in range(n):
      graph[i] = list(map(int, input().split()))
  
  dp[0][0][1] = 1  # 첫 시작 위치
  
  # dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
  for i in range(2, n):
      if graph[0][i] == 0:
          dp[0][0][i] = dp[0][0][i - 1]
  
  for r in range(1, n):
      for c in range(1, n):
          # 현재위치가 대각선인 경우
          if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
              dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
  
          if graph[r][c] == 0:
              # 가로인 경우
              dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
              # 세로인경우
              dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]
  
  print(sum(dp[i][n - 1][n - 1] for i in range(3)))
  ```

  > 대체 어떻게 이렇게 푸는 거냐,, dp는 진짜,, 어떻게 이렇게 풀지,,? 라는 생각밖에 안나오는 알고리즘,, 내가 코테 직전까지 dp를 익힐 수 있을까,,
  >
  > 아무튼 이분은 가로 dp 세로 dp 대각선 dp를 따로 따로 만들어서 구현하셨다. 
  >
  > 대각선일 경우, 현재 위치가 벽이 아니라면,  위, 위 대각선, 왼쪽의 진행 숫자들을 더해준다.
  >
  > 가로일 경우, 현재가 벽이 아닌지만 따지고, 왼쪽, 위 대각선 진행 수를 더해줌
  >
  > 세로일 경우 현재가 벽이 아닌지 따지고, 위, 위 대각선이 아닌지 따져서
  >
  > 나중에 결과를 낼 때, 세 가지의 dp 리스트의 총합을 더하면 경우의 수가 나온다.
  >
  > 어찌어찌 이해는 했는데 내가 구현할 수 있을까? 라는 생각이 드는 문제,, dp 차근차근 시작해 보아야 겠다.
  >
  > 

