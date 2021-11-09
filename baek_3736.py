# python

## baek 2206 벽 부수고 이동하기 골드4

https://www.acmicpc.net/problem/2206

> python3 3736ms



* 문제

  > N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
  >
  > 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
  >
  > 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
  >
  > 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
  >
  > ```bash
  > 6 4
  > 0100
  > 1110
  > 1000
  > 0000
  > 0111
  > 0000
  > ```
  >
  
* 출력

  > 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
  >
  > ```bash
  > 15
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    n, m = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    v = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q, res = deque([]), 0
    q.append([0, 0, 0, 1])

    while q:
        r, c, flag, cnt = q.popleft()

        if r == n-1 and c == m-1:
            res = cnt
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if flag:
                if 0 <= nr < n and 0 <= nc < m and not v[nr][nc][1] and not arr[nr][nc]:
                    v[nr][nc][1] = 1
                    q.append([nr, nc, flag, cnt+1])
            else:
                if 0 <= nr < n and 0 <= nc < m and not v[nr][nc][0]:
                    if arr[nr][nc]:
                        q.append([nr, nc, 1, cnt+1])
                    else:
                        q.append([nr, nc, flag, cnt+1])
                    v[nr][nc][0] = 1

    print(res if res != 0 else -1)


sol()
```

> 아 열받아 진자
>
> - `[[[0] * 2 for _ in range(m)] for _ in range(n)]`
>
>   - 이런식으로 for문을 두 개 써야 내가 원하는 방식으로 다차원 배열이 생성됨
>
> - 벽을 부쉈을 때와 안부쉈을 때를 나누면 되는데 여기서 한참을 삽질했다.
>
>   - 벽을 부수며 지나갔을 때와 벽을 안부수며 지나갔을 때를 덧셈으로 계산해보았다. 벽을 안부순 상태에서 현재 길을 지나가는 거라면 1을 더해 줬고, 벽을 부순 상태에서 현재 길을 지나가는 거라면 2를 더해 줬다.
>     - 이 논리에는 오류가 있었다. 길의 상태는 총 3가지 1 2 3이 존재하였는데 만약 상태가 2라면 두 가지 경우의 수가 존재하는 것이었다. 안부순 상태에서 2번 지나가는 것, 그리고 부순 상태에서  한 번 지나가는 것. 그래서 이건 실패.. (여기서 3차원 배열을 생각했어야 했다)
>
>   - 하, 이다음은 왜 이렇게 생각했는지 모르겠는데 벽을 부순상태에서 상하좌우 방문표시 저장. 벽을 안 부순 상태에서 상하좌우 방문 표시 저장. 왜 이렇게 다각도로 저장했는지 모를일.. 왜 이랬지? 당연히 답은 맞을 수 있겠지만 시간초과 메모리 초과
>   - 마지막으로 생각한 게 현재 답이다. 사실 다른 답을 보고 아이디어를 떠올렸다. 휴 짱나



* 모범답안

  ```python
  2176
  
  import sys
  
  input = sys.stdin.readline
  
  
  def sol2206():
      n, m = map(int, input().split())
      board = [list(input().rstrip()) for _ in range(n)]
      nw = {'0', '2'}
      q = [(0, 0, 2)]
      answer = 1
      while q:
          nq = []
          for r, c, w in q:
              if r == n - 1 and c == m - 1:
                  return answer
              
              for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                  if 0 <= nr < n and 0 <= nc < m and board[nr][nc]!='3':
                      if w == 1:
                          if board[nr][nc] == '0':
                              board[nr][nc] = '2'
                              nq.append((nr, nc, 1))
                      else:
                          if board[nr][nc] == '1':
                              nq.append((nr, nc, 1))
                          elif board[nr][nc] in nw:
                              nq.append((nr, nc, 2))
                          board[nr][nc] = '3'
          answer += 1
          q = nq
      return -1
  
  
  if __name__ == '__main__':
      print(sol2206())
  ```
  
  > 아 ㅋㅋㅋㅋ 이사람은 나의 첫번재 방법처럼 푼건데 ,, 덧셈이 아니라 문자열로 표시해줬다.. 현명하다 현명해...

