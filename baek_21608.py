# python

## baek 21608 상어 초등학교 실버1

https://www.acmicpc.net/problem/21608

> python3 256ms
>
> pypy3 204ms



* 문제

  > 상어 초등학교에는 교실이 하나 있고, 교실은 N×N 크기의 격자로 나타낼 수 있다. 학교에 다니는 학생의 수는 N2명이다. 오늘은 모든 학생의 자리를 정하는 날이다. 학생은 1번부터 N2번까지 번호가 매겨져 있고, (r, c)는 r행 c열을 의미한다. 교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다.
  >
  > 선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다. 이제 다음과 같은 규칙을 이용해 정해진 순서대로 학생의 자리를 정하려고 한다. 한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.
  >
  > 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
  > 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
  > 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
  >
  > 예를 들어, N = 3이고, 학생 N2명의 순서와 각 학생이 좋아하는 학생이 다음과 같은 경우를 생각해보자.
  >
  > | 학생의 번호 | 좋아하는 학생의 번호 |
  > | :---------- | :------------------- |
  > | 4           | 2, 5, 1, 7           |
  > | 3           | 1, 9, 4, 5           |
  > | 9           | 8, 1, 2, 3           |
  > | 8           | 1, 9, 3, 4           |
  > | 7           | 2, 3, 4, 8           |
  > | 1           | 9, 2, 5, 7           |
  > | 6           | 5, 2, 3, 4           |
  > | 5           | 1, 9, 2, 8           |
  > | 2           | 9, 3, 1, 4           |
  >
  > 가장 먼저, 4번 학생의 자리를 정해야 한다. 현재 교실의 모든 칸은 빈 칸이다. 2번 조건에 의해 인접한 칸 중에서 비어있는 칸이 가장 많은 칸인 (2, 2)이 4번 학생의 자리가 된다.
  >
  > |      |      |      |
  > | ---- | ---- | ---- |
  > |      | 4    |      |
  > |      |      |      |
  >
  > 다음 학생은 3번이다. 1번 조건을 만족하는 칸은 (1, 2), (2, 1), (2, 3), (3, 2) 이다. 이 칸은 모두 비어있는 인접한 칸이 2개이다. 따라서, 3번 조건에 의해 (1, 2)가 3번 학생의 자리가 된다.
  >
  > |      | 3    |      |
  > | ---- | ---- | ---- |
  > |      | 4    |      |
  > |      |      |      |
  >
  > 다음은 9번 학생이다. 9번 학생이 좋아하는 학생의 번호는 8, 1, 2, 3이고, 이 중에 3은 자리에 앉아있다. 좋아하는 학생이 가장 많이 인접한 칸은 (1, 1), (1, 3)이다. 두 칸 모두 비어있는 인접한 칸이 1개이고, 행의 번호도 1이다. 따라서, 3번 조건에 의해 (1, 1)이 9번 학생의 자리가 된다.
  >
  > | 9    | 3    |      |
  > | ---- | ---- | ---- |
  > |      | 4    |      |
  > |      |      |      |
  >
  > 이번에 자리를 정할 학생은 8번 학생이다. (2, 1)이 8번 학생이 좋아하는 학생과 가장 많이 인접한 칸이기 때문에, 여기가 그 학생의 자리이다.
  >
  > | 9    | 3    |      |
  > | ---- | ---- | ---- |
  > | 8    | 4    |      |
  > |      |      |      |
  >
  > 7번 학생의 자리를 정해보자. 1번 조건을 만족하는 칸은 (1, 3), (2, 3), (3, 1), (3, 2)로 총 4개가 있고, 비어있는 칸과 가장 많이 인접한 칸은 (2, 3), (3, 2)이다. 행의 번호가 작은 (2, 3)이 7번 학생의 자리가 된다.
  >
  > | 9    | 3    |      |
  > | ---- | ---- | ---- |
  > | 8    | 4    | 7    |
  > |      |      |      |
  >
  > 이런식으로 학생의 자리를 모두 정하면 다음과 같다.
  >
  > | 9    | 3    | 2    |
  > | ---- | ---- | ---- |
  > | 8    | 4    | 7    |
  > | 5    | 6    | 1    |
  >
  > 이제 학생의 만족도를 구해야 한다. 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다. 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
  >
  > 학생의 만족도의 총 합을 구해보자.

* 입력

  > 첫째 줄에 N이 주어진다. 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.
  >
  > 학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수이다. 어떤 학생이 자기 자신을 좋아하는 경우는 없다.
  >
  > ```python
  > 3
  > 4 2 5 1 7
  > 3 1 9 4 5
  > 9 8 1 2 3
  > 8 1 9 3 4
  > 7 2 3 4 8
  > 1 9 2 5 7
  > 6 5 2 3 4
  > 5 1 9 2 8
  > 2 9 3 1 4
  > ```
  >
  > 

* 출력

  > 첫째 줄에 학생의 만족도의 총 합을 출력한다.
  >
  > ```python
  > 54
  > ```



```python
'''
3
1 1 1 1 1
2 1 1 1 1
3 1 1 1 1
4 1 1 1 1
5 1 1 1 1
6 1 1 1 1
7 2 3 2 3
8 2 3 2 3
9 2 3 2 3

6
'''

import sys
input = sys.stdin.readline


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    n = int(input())
    arr = []
    classroom = [[0] * n for _ in range(n)]
    sat = [[] for _ in range(n*n+1)]
    res = 0

    for _ in range(n*n):
        arr.append(list(map(int, input().split()))) # 순서

    for i in range(len(arr)):
        likeloc, likeflag = [0, 0], 0
        # [좋아하는 사람 명수, 공백 개수], 상하좌우 모두 좋아하는 사람일 경우의 flag
        for j in range(n):
            for k in range(n):
                if len(likeloc) == 2 and classroom[j][k] == 0:
                    # 현재 자리가 정해지지 않았고, 비어있는 자리라면
                    likeloc.append(j)
                    likeloc.append(k)
                    # 자리 초기화
                like, blank = 0, 0
                if classroom[j][k] == 0:
                    # 비어있는 자리라면
                    for dir in range(4):
                        nr, nc = j + dr[dir], k + dc[dir]
                        if 0 <= nr < n and 0 <= nc < n:
                            if classroom[nr][nc] in arr[i]:
                                like += 1
                            elif classroom[nr][nc] == 0:
                                blank += 1
                            # 사방을 돌면서 좋아하는 사람과 공백의 개수를 세어줌
                    if like == 4:
                        # 상하좌우 모두 좋아하는 사람이라면
                        likeflag = 1
                        classroom[j][k] = arr[0]
                        sat[arr[i][0]] = [arr[i][1], arr[i][2], arr[i][3], arr[i][4]]
                        # 자리를 정하고 다음 자리들 탐색할 필요 없으니 break
                        break
                    if like >= likeloc[0]:
                        if like > likeloc[0]:
                            likeloc = [like, blank, j, k]
                        else:
                            if blank >= likeloc[1]:
                                if blank > likeloc[1]:
                                    likeloc = [like, blank, j, k]
                                else:
                                    if j <= likeloc[2]:
                                        if j < likeloc[2]:
                                            likeloc = [like, blank, j, k]
                                        else:
                                            if k < likeloc[3]:
                                                likeloc = [like, blank, j, k]
                        # 문제에 주어진 세 개의 조건에 걸맞는 난잡한 if문
            if likeflag:
                break
        if likeflag:
            continue
            # 좋아하는 사람이 상하좌우에 있을 때 빠져나가기
        classroom[likeloc[2]][likeloc[3]] = arr[i][0]
        sat[arr[i][0]] = [arr[i][1], arr[i][2], arr[i][3], arr[i][4]]
        # 만족도를 계산할 배열에 넣기

    for i in range(n):
        for j in range(n):
            likep = 0
            for dir in range(4):
                nr, nc = i + dr[dir], j + dc[dir]
                if 0 <= nr < n and 0 <= nc < n:
                    if classroom[nr][nc] in sat[classroom[i][j]]:
                        likep += 1
            if likep:
                res += 10 ** (likep-1)

    print(res)


sol()


```

> 하,, 코드 진짜 지저분하다.. 그래도 이게 파이썬 코드 중에서 제일 빠른데 그 이유는 네 개의 방면에 좋아하는 사람이 있을 경우 다음 좌표들을 따져보지 않고 빠져나와서 그런듯.
>
> 고민했던 건 현재 좌표 초기화였는데 이부분은 교실을 돌면서 현재 0인 좌표로 초기화해줬어야 하는 게 중요한듯,,

* 모범답안

  ```python
  pypy3 208
  N=int(input())
  ans = [[-1 for _ in range(N+2)] for _ in range(N+2)]
  for i in range(1,N+1):
      for j in range(1,N+1):
          ans[i][j] = 0
  inp = [None for i in range(N*N+1)]
  
  def get_rank(x, y, a):
      ret = 0
      for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
          if ans[x+dx][y+dy] == 0:
              ret += 1
          elif ans[x+dx][y+dy] in inp[a]:
              ret += 10
      return ret
  
  def set_pos(a):
      m = (10, (-1,-1))
      for x in range(1,N+1):
          for y in range(1,N+1):
              if ans[x][y] == 0:
                  m = min(m, (-get_rank(x,y,a), (x,y)))
      x,y = m[1]
      ans[x][y] = a
  
  for i in range(N*N):
      tmp = list(map(int, input().split()))
      inp[tmp[0]] = tmp[1:]
      set_pos(tmp[0])
  
  tot = 0
  for i in range(1,N+1):
      for j in range(1,N+1):
          tot += [0, 1, 10, 100, 1000][get_rank(i,j,ans[i][j])//10]
  print(tot)
  ```

  > 함수를 쓰셔서 코드 길이에 최적화를 하셨군,,

