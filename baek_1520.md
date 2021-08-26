# python

## baek 1520 내리막 길 골드4

https://www.acmicpc.net/problem/1520

> python3 180ms

* 문제

  > 여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview) ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview) ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.
  >
  > ```bash
  > 4 5
  > 50 45 37 32 30
  > 35 50 40 20 25
  > 30 30 25 17 28
  > 27 24 22 15 10
  > ```
  >
  
* 출력

  > 첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.
  >
  > ```bash
  > 3
  > ```



```python
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():

    def dfs(r, c):
        if r == m-1 and c == n-1:
            return 1

        if v[r][c] != -1:
            return v[r][c]

        v[r][c] = 0

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] < arr[r][c]:
                v[r][c] += dfs(nr, nc)

        return v[r][c]

    m, n = map(int, input().split())
    arr, v = [list(map(int, input().split())) for _ in range(m)], [[-1] * n for _ in range(m)]
    print(dfs(0, 0))


sol()
```

> 하,, 힘든 풀이였다. 방문표시 초기화를 -1이 아닌 0으로 해놔서 무한루프 걸렸다.
>
> if문을 또 if v[ r ] [ c ] 일 때만 작동하라고 해놔서 좌표가 0인거는 계속 돌고 돌고 돌았던 거임. 아예 갈 수 없을 수도 있을 텐데



* 모범답안

  ```python
  136
  
  import sys
  sys.setrecursionlimit(100000000)
  
  
  def solution():
      m, n = map(int, sys.stdin.readline().strip().split())
      square = [list(map(int, sys.stdin.readline().strip().split()))
                for _ in range(m)]
      memo = [[-1] * n for _ in range(m)]
      answer = memoization(square, 0, 0, m, n, memo)
      print(answer)
  
  
  def memoization(square, i, j, m, n, memo):
      if memo[i][j] != -1:
          return memo[i][j]
      if i == m - 1 and j == n - 1:
          memo[i][j] = 1
          return 1
      ways_to_go = 0
  
      if i > 0 and square[i][j] > square[i - 1][j]:
          ways_to_go += memoization(square, i - 1, j, m, n, memo)  # up
      if i < m - 1 and square[i][j] > square[i + 1][j]:
          ways_to_go += memoization(square, i + 1, j, m, n, memo)  # down
      if j > 0 and square[i][j] > square[i][j - 1]:
          ways_to_go += memoization(square, i, j - 1, m, n, memo)  # left
      if j < n - 1 and square[i][j] > square[i][j + 1]:
          ways_to_go += memoization(square, i, j + 1, m, n, memo)  # right
      memo[i][j] = ways_to_go
      return memo[i][j]
  
  
  solution()
  ```

  > 역시 for문보다 if문 4개 쓰는 게 더 빠르다.

