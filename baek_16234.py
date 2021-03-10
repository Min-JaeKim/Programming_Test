# python

## 백준 16234 인구 이동 골드 5

https://www.acmicpc.net/problem/16234



> python3 시간초과
>
> pypy3 816ms



* 문제

  > N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
  >
  > 오늘부터 인구 이동이 시작되는 날이다.
  >
  > 인구 이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
  >
  > - 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
  > - 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
  > - 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
  > - 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
  > - 연합을 해체하고, 모든 국경선을 닫는다.
  >
  > 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
  >
  > 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
  >
  > 인구 이동이 발생하는 횟수가 2,000번 보다 작거나 같은 입력만 주어진다.
  >
  > ```bash
  > 2 20 50
  > 50 30
  > 20 40
  > ```

* 출력

  > 인구 이동이 몇 번 발생하는지 첫째 줄에 출력한다.
  >
  > ```bash
  > 1
  > ```



```python
'''
로직 설명
1. deque를 두 개 할당.
2. 일단 모든 좌표를 돌면서 q1에 push
3. 그리고 그 좌표를 사방면으로 돌면서 범위에 해당하는지 체크.
4. 범위
4-1. 범위에 해당하는 값이 없다면 q1을 pop하고 다음 좌표 탐색
4-2. 범위에 해당한다면 해당한 좌표를 q1에 push하고 q2에 q1값을 복사.
4-2-1. q2 : 범위 해당 좌표를 push하고 pop하는 deque
4-2-2. q1 : 범위 해당 좌표를 push만 함. 모아뒀다가 나중에 인구수 변경하는 deque.
5. q2가 존재할 때까지, q2에 있는 좌표를 pop하며 4방면으로 탐색.
5-1. 범위에 해당하는 좌표가 있을 시, q1과 q2에 둘 다 push.
5-2. 없을 시, q2는 pop
6. 3~5까지 반복하며 해당되는 좌표의 인구를 더함.
7. q2가 없으면 반복문이 끝나고 이제 while문을 통해 q1이 존재할 때까지 인구수 변경.
8. flag를 통해 한 번이라도 인구 이동을 하지 않았을 때는 반복문 탈출!

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = (-1,1,0,0)
dc = (0,0,-1,1)

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q, q2, result = deque([]), deque([]), 0
while True:
    progress = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] : continue
            q.append([i, j, arr[i][j]])
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if l <= abs(arr[i][j]-arr[nr][nc]) <= r:
                        q.append([nr, nc, arr[nr][nc]])
                        visited[i][j], visited[nr][nc], progress = True, True, True
                        q2 = q.copy()
            if len(q) == 1 : q.pop()
            popul = 0
            while q2:
                row, col, tmp = q2.popleft()
                popul += tmp
                for m in range(4):
                    nnr = row + dr[m]
                    nnc = col + dc[m]
                    if 0 <= nnr < n and 0 <= nnc < n and not visited[nnr][nnc] and \
                        l <= abs(tmp - arr[nnr][nnc]) <= r:
                        visited[nnr][nnc] = True
                        q.append([nnr, nnc, arr[nnr][nnc]])
                        q2.append([nnr, nnc, arr[nnr][nnc]])
            if popul != 0:
                popul //= len(q)
            while q:
                row, col, garbage = q.pop()
                arr[row][col] = popul
    if not progress:
        break
    result += 1

print(result)
```

> 처음에는 함수를 써서 인구이동할 수 있는 국가가 있을 때마다 재귀로 넣고 넣어서 사방면을 돌았다. 하지만 이렇게 하면 리커션에러라고 무수히 많은 재귀에 들어갔다고 에러가 뜬다.  그래서 시간초과 뜰 걸 알면서도 조작했다. 결과는 역시 시간초과.
>
> 그래서 재귀를 버리고 while문을 택해서 했다. 하지만 이 역시도 python3는 시간 초과 뜬다 후우,,
>
> 추가로 풀기 굉장히 혼란스러운 문제였다. 여타 다른 문제와 다르게 정말 오래 걸렸고 디버깅도 수도 없이 해야했다. 앞으로 디버깅에 의존하지 않는 사람이 되었음 좋겠다.



### 모범답안

```python
444ms

import sys
from collections import deque
input = sys.stdin.readline


dy = [1, -1, 0, 0] 
dx = [0, 0, 1, -1]


def bfs(y, x):
    global visisted, m
    queue = deque()
    queue.append((y, x))
    sum_val = m[y][x]
    visisted[y][x] = 1
    pos = [(y, x)]

    while queue:
        y, x = queue.popleft()

        for my, mx in zip(dy, dx):
            ny = y + my
            nx = x + mx
            if 0 <= ny < N and 0 <= nx < N and not visisted[ny][nx]:
                if L <= abs(m[ny][nx] - m[y][x]) <= R:
                    visisted[ny][nx] = 1
                    sum_val += m[ny][nx]
                    queue.append((ny, nx))
                    pos.append((ny, nx))
        
    if len(pos) > 1:  # exist group
        cnt = len(pos)
        mean = sum_val // cnt
        for i in range(cnt):
            y, x = pos[i] 
            m[y][x] = mean
            q.append((y, x))
        return 0
    else:
        return 1


def check(y, x):
    for my, mx in zip(dy, dx):
        ny = y + my
        nx = x + mx
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(m[ny][nx] - m[y][x]) <= R:
                return 0
    return 1


N, L, R = map(int, input().split())
m = [[] for _ in range(N)]
q = deque()
for i in range(N):
    m[i] = list(map(int, input().split()))
    for j in range(N):
        q.append((i, j))

cnt = 0
flag = False 

while not flag:
    visisted = [[0] * N for _ in range(N)]
    flag = True
    size = len(q)
    for _ in range(size):
        y, x = q.popleft()
        if visisted[y][x] or check(y, x):
            continue
        if not bfs(y, x):
            flag = False 
    if not flag:
        cnt += 1
print(cnt)
```

> 어떻게 444ms가 나오는거지? ;; 함수를 쓰면 이렇게 시간이 단축이 되나? 원인이 뭘까..