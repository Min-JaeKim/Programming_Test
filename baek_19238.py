# python

## baek 19238 스타트 택시 골드4

https://www.acmicpc.net/problem/19238

> python3 184ms
>
> pypy3 260ms



* 문제

  > 스타트링크가 "스타트 택시"라는 이름의 택시 사업을 시작했다. 스타트 택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.
  >
  > 택시 기사 최백준은 오늘 M명의 승객을 태우는 것이 목표이다. 백준이 활동할 영역은 N×N 크기의 격자로 나타낼 수 있고, 각 칸은 비어 있거나 벽이 놓여 있다. 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다. 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동한다.
  >
  > M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다. 각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.
  >
  > 백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 연료는 한 칸 이동할 때마다 1만큼 소모된다. 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
  >
  > ![img](md-images/preview)
  >
  > <그림 1>
  >
  > <그림 1>은 택시가 활동할 영역의 지도를 나타내며, 택시와 세 명의 승객의 출발지와 목적지가 표시되어 있다. 택시의 현재 연료 양은 15이다. 현재 택시에서 각 손님까지의 최단거리는 각각 9, 6, 7이므로, 택시는 2번 승객의 출발지로 이동한다.
  >
  > | ![img](md-images/preview)<그림 2> | ![img](md-images/preview)<그림 3> |
  > | --------------------------------- | --------------------------------- |
  > |                                   |                                   |
  >
  > <그림 2>는 택시가 2번 승객의 출발지로 가는 경로를, <그림 3>은 2번 승객의 출발지에서 목적지로 가는 경로를 나타낸다. 목적지로 이동할 때까지 소비한 연료는 6이고, 이동하고 나서 12가 충전되므로 남은 연료의 양은 15이다. 이제 택시에서 각 손님까지의 최단거리는 둘 다 7이므로, 택시는 둘 중 행 번호가 더 작은 1번 승객의 출발지로 이동한다.
  >
  > | ![img](md-images/preview)<그림 4> | ![img](md-images/preview)<그림 5> |
  > | --------------------------------- | --------------------------------- |
  > |                                   |                                   |
  >
  > <그림 4>와 <그림 5>는 택시가 1번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 남은 연료의 양은 15 - 7 - 7 + 7×2 = 15이다.
  >
  > | ![img](md-images/preview)<그림 6> | ![img](md-images/preview)<그림 7> |
  > | --------------------------------- | --------------------------------- |
  > |                                   |                                   |
  >
  > <그림 6>과 <그림 7>은 택시가 3번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 최종적으로 남은 연료의 양은 15 - 5 - 4 + 4×2 = 14이다.
  >
  > 모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.

* 입력

  > 첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.
  >
  > 다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.
  >
  > 다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.
  >
  > 그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.
  >
  > ```python
  > 6 3 15
  > 0 0 1 0 0 0
  > 0 0 1 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 1 0
  > 0 0 0 1 0 0
  > 6 5
  > 2 2 5 6
  > 5 4 1 6
  > 4 2 3 5
  > ```
  >
  > 

* 출력

  > 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다. 단, 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다. 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
  >
  > ```python
  > 14
  > ```



```python
'''
6 1 15
0 0 1 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
5 4 1 1
-1

5 5 4
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
3 3
2 2 4 2
4 2 4 4
4 4 2 4
2 4 2 2
2 5 3 3
10

5 1 4
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
3 3
2 2 4 2
4

6 4 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
1 6 5 4
20

3 1 100
0 1 0
0 1 0
0 1 0
1 1
1 3 3 3
-1
'''

'''
로직설명
1. 벽은 편의상 -1로 대체
2. 맵에서 사람이 존재하는 곳을 순번으로 표시함
3. 그리고 사람의 도착지점을 customers 리스트에 저장. 
(저장 인덱스는 사람의 순번보다 1작음)
4. 무한반복을 하면서
5. 매번 제한 거리를 최댓값으로 설정함
6. taxitocustomers 함수를 돈다.
(택시에서 고객까지 가는 함수)
7. 돌면서 택시에서 최솟값인 사람을 mindist 리스트에 저장.
8. 만약 저장된 사람이 없으면 택시가 사람을 못태웠다는 뜻이므로
-1을 출력하고 종료
9. 만약 저장된 최솟값 사람들이 다수라면
10. 행과 열을 기준으로 정렬하고 맨 앞 사람 태우고 bfs시작.
11. 택시가 이동한 거리보다 연료가 작다면 -1 출력후 종료
12. 도착지점에 다다랐다면 연료 계산후 다음 반복문
13. depart flag를 두어 도착지에 방문 했을 경우는 
True로 하고 , 방문하지 못한 채로 queue가 끝났을 경우
False가 되어 -1출력하고 종료.
14. 목적지까지 도착한 사람은 맵에서 0으로 바꿔줌.
15. 마지막으로 맵을 돌면서 사람의 순번이 존재한다면
반복문 계속 진행. 없으면 모두 태웠으므로 종료.
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def taxitocustomers(taxistartR, taxistartC):        # 고객들과 택시 거리 측정.
    global limitdist
    q = deque([[0, taxistartR, taxistartC]])
    visited = [[False] * n for _ in range(n)]
    visited[taxistartR][taxistartC] = True
    while q:
        dist, r, c = q.popleft()
        if limitdist < dist:
            break
        if arr[r][c] != 0:              # 7
            limitdist = dist
            mindist.append([dist, r, c, arr[r][c]])
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0 <= nr < n and \
                0 <= nc < n and \
                not visited[nr][nc] and\
                arr[nr][nc] != -1:
                q.append([dist + 1, nr, nc])
                visited[nr][nc] = True


n, m, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr[i][j] = -1              # 1
taxir, taxic = map(int, input().split())
taxir, taxic = taxir-1, taxic-1
customers, mindist= [], []
for i in range(1, m+1):      # 사람들을 돌면서
    star, stac, endr, endc = map(int, input().split())  # 시작 행, 렬, 도착 행, 렬
    arr[star-1][stac-1] = i
    customers.append([endr-1, endc-1])      # customers인덱스는 순번보다 1작다.

cnt = 0
while True:
    limitdist = float('inf')
    taxitocustomers(taxir, taxic)
    if not mindist:                     # 8
        print(-1)
        exit()
    if len(mindist) > 1:                # 9
        mindist.sort(key = lambda x : (x[1], x[2]))
    q, rr, cc = deque([mindist[0] + [0]]), customers[mindist[0][3]-1][0], customers[mindist[0][3]-1][1]
    taxir, taxic = mindist[0][1], mindist[0][2]
    visited = [[False] * n for _ in range(n)]
    depart = False
    while q:                            # 10
        dist, r, c, gbg, ddist = q.popleft()
        if dist + ddist > fuel:         # 11
            print(-1)
            exit()
        if r == rr and c == cc:         # 12
            fuel = fuel - (dist + ddist) + ddist * 2
            depart = True
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and\
                0 <= nc < n and\
                not visited[nr][nc] and\
                arr[nr][nc] != -1:
                q.append([dist, nr, nc, gbg, ddist+1])
                visited[nr][nc] = True
    if not depart:                      # 13
        print(-1)
        exit()
    arr[taxir][taxic] = 0               # 14
    taxir, taxic, mindist, flag = rr, cc, [], True
    for i in range(n):                  # 15
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:
                flag = False
    if flag:
        break

print(fuel)
```

> 뭔,, 이문제 풀려고 거진,, 여섯시간은 쓴 것 같은데,,아닌가,, 암튼 엄청 맘고생 많이 했던 문제,,
>
> 풀면서 계속 놓쳤던 부분은
>
> 1. `시간 초과` : 이부분은 맵에 사람들의 출발 지점에 순번을 넣는 거였음.. 애초에 택시에서 계속 bfs 돌려서 거리 측정하면 안됨.. 그렇게 되면 시간 초과 날 수 밖에 없다.
> 2. `taxir, taxic, mindist, flag = rr, cc, [], True` : 택시 출발 지점 초기화. 현재 고객의 도착지점에서 다시 출발할 예정이므로,, 그 값을 넣어 줘야 함.
> 3. `limitdist = float('inf')` : 제한 값 초기화,, 이것 때문에 애를 먹었다.. 디버깅을 몇 번 돌린 건지.. 이전 리밋거리 값이 다음 거리에 영향을 끼치지 않기 위해 매 반복문 시작 전에 최댓값으로 초기화해줘야 함.



* 모범답안

  ```python
  from sys import*
  from collections import*
  from heapq import*
  input=stdin.readline
  def solve():
      global k
      q=deque()
      q.append((0, sx-1, sy-1))
      cnt = 0
      status = 0      #0 시작 찾음, 1 도착점 찾음, 2도착점 찾은 상태
      ex, ey = -1, -1
      while 1:
          if cnt == m: return k
          if not q: break
          visit = [[0]*n for _ in range(n)]
          while 1:
              lq = len(q)
              if not q: break
              pq = []
              for i in range(lq):
                  c, x, y = q.popleft()
                  if c > k: return -1
                  if status==0 and a[x][y]:
                      heappush(pq, (c, x, y))
                      continue
                  if status and x==ex and y==ey:
                      cnt+=1
                      k += c
                      status = 2
                      q=deque()
                      q.append((0, x, y))
                      break
                  for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                      nx, ny = x+dx, y+dy
                      if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or a[nx][ny]==1: continue
                      visit[nx][ny]=1
                      q.append((c+1, nx, ny))
              if status==0 and pq:
                  c, x, y = heappop(pq)
                  ex, ey = a[x][y]
                  a[x][y]=0
                  q=deque()
                  k -= c
                  q.append((0, x, y))
                  status=1
                  break
              if status==2:
                  status=0
                  break
      return -1
  
  n, m, k= map(int,input().split())
  a=[list(map(int,input().split())) for _ in range(n)]
  sx, sy = map(int,input().split())
  for i in range(m):
      x, y, ex, ey = map(int,input().split())
      a[x-1][y-1] = [ex-1, ey-1]
  print(solve())
  ```

  > 웁스 깔쌈하구만,,, 나는 배열에 ㅅㅏ람 순번을 적었는데,, 여기는 목적지를 아예 리스트로 묶어서 넣었음.
  >
  > - `heapq` : 우선순위큐,,