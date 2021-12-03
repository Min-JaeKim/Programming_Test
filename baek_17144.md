# python

## baek 17144 미세먼지 안녕! 골드4

https://www.acmicpc.net/problem/17144

> pypy3 424ms



* 문제

  > 미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.
  >
  > ![img](md-images/preview)
  >
  > 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.
  >
  > 1초 동안 아래 적힌 일이 순서대로 일어난다.
  >
  > 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
  >    - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
  >    - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
  >    - 확산되는 양은 Ar,c/5이고 소수점은 버린다.
  >    - (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
  > 2. 공기청정기가 작동한다.
  >    - 공기청정기에서는 바람이 나온다.
  >    - 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
  >    - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
  >    - 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
  >
  > 다음은 확산의 예시이다.
  >
  > ![img](md-images/preview)
  >
  > 왼쪽과 오른쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.
  >
  > ![img](md-images/preview)
  >
  > 인접한 네 방향으로 모두 확산이 일어난다.
  >
  > ![img](md-images/preview)
  >
  > 공기청정기가 있는 칸으로는 확산이 일어나지 않는다.
  >
  > 공기청정기의 바람은 다음과 같은 방향으로 순환한다.
  >
  > ![img](md-images/preview)
  >
  > 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.
  
* 입력

  > 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
  >
  > 둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
  >
  > ```bash
  > 7 8 4
  > 0 0 0 0 0 0 0 9
  > 0 0 0 0 3 0 0 8
  > -1 0 5 0 0 0 22 0
  > -1 8 0 0 0 0 0 0
  > 0 0 0 0 0 10 43 0
  > 0 0 5 0 15 0 0 0
  > 0 0 40 0 0 0 20 0
  > ```
  >
  
* 출력

  > 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
  >
  > ```bash
  > 178
  > ```



```python
import sys
input = sys.stdin.readline


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    r, c, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]
    air = []

    for _ in range(t):
        arr_tmp = [[0] * c for _ in range(r)]
 
        for i in range(r):
            for j in range(c):
                if arr[i][j] > 0:
                    cnt = 0
                    for d in range(4):
                        nr, nc = i + dr[d], j + dc[d]
                        if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] != -1:
                            arr_tmp[nr][nc] += arr[i][j] // 5
                            cnt += 1
                    arr_tmp[i][j] += arr[i][j] - (arr[i][j] // 5) * cnt

                elif len(air) < 2 and arr[i][j] == -1:
                    air.append(i)

        arr_tmp[air[0]-1][0], arr_tmp[air[1]+1][0] = 0, 0

        for i in range(air[0]-1, -1, -1):
            arr_tmp[i+1][0] = arr_tmp[i][0]
        for i in range(1, c):
            arr_tmp[0][i-1] = arr_tmp[0][i]
        for i in range(1, air[0]+1):
            arr_tmp[i-1][c-1] = arr_tmp[i][c-1]
        for i in range(c-2, -1, -1):
            arr_tmp[air[0]][i+1] = arr_tmp[air[0]][i]

        for i in range(air[1]+1, r):
            arr_tmp[i-1][0] = arr_tmp[i][0]
        for i in range(1, c):
            arr_tmp[r-1][i-1] = arr_tmp[r-1][i]
        for i in range(r-2, air[1]-1, -1):
            arr_tmp[i+1][c-1] = arr_tmp[i][c-1]
        for i in range(c-2, -1, -1):
            arr_tmp[air[1]][i+1] = arr_tmp[air[1]][i]

        arr_tmp[air[0]][0], arr_tmp[air[1]][0] = -1, -1
        for i in range(r):
            arr[i] = arr_tmp[i][:]

    res = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                res += arr[i][j]

    print(res)


sol()
```

> 하 짜증나
>
> 나 요즘 집중력이 좀 떨어졌나,,? 아 진자 이문제를 이렇게 오래 풀고 있으면 안되는데 말이지,, 값들을 회전시킬 때, 공기청정기에 들어가는 내용물들은 미리 0으로 바꾸고 회전을 시켰어야 했다. 하지만 0으로 변환하지 않고 돌린 덕분에 시간이 지나도 계속 같은 값이 나왔던 것,,(먼지는 질량이 보존되기 때문에 공기청정기에 들어가지 않는 한 같은 값이 나오는 게 맞다... 즉, 나는 공기청정기에 들어가는 값을 계산 안해줬다는 것.)



* 모범답안

  ```python
  1924
  
  r, c, t = map(int, input().split())
  
  room_given=[]
  g=[]
  for i in range(r):
      arr = list(map(int, input().split()))
      if arr[0]==-1:
         g.append(i) 
      room_given.append(arr)
      
  def diff_center(pos_x, pos_y,room):
      return room[pos_x-1][pos_y]//5+room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*4
  
  def diff_x1(pos_x,pos_y,room):
      return room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*3    
      
  def diff_xr(pos_x,pos_y,room):    
      return room[pos_x-1][pos_y]//5+room[pos_x][pos_y-1]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*3
  
  def diff_y1(pos_x,pos_y,room):
      return room[pos_x-1][pos_y]//5+room[pos_x+1][pos_y]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*3
  
  def diff_yc(pos_x,pos_y,room):
      return room[pos_x-1][pos_y]//5+room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5-(room[pos_x][pos_y]//5)*3
  
  def diff_x1y1(pos_x,pos_y,room):
      return room[pos_x+1][pos_y]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*2
  
  def diff_x1yc(pos_x,pos_y,room):
      return room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5-(room[pos_x][pos_y]//5)*2
  
  def diff_xry1(pos_x,pos_y,room):
      return room[pos_x-1][pos_y]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*2
  
  def diff_xryc(pos_x,pos_y,room):
      return room[pos_x-1][pos_y]//5+room[pos_x][pos_y-1]//5-(room[pos_x][pos_y]//5)*2
  
  
  def diff(room,r,c):
      room_ins=[[0]*c for _ in range(r)]
      for ix in range(1,r-1):
          for iy in range(1,c-1):
              room_ins[ix][iy]=diff_center(ix,iy,room)
      for ix in range(1,r-1):
          room_ins[ix][0]=diff_y1(ix,0,room)
          room_ins[ix][c-1]=diff_yc(ix,c-1,room)
      for iy in range(1,c-1):
          room_ins[0][iy]=diff_x1(0,iy,room)
          room_ins[r-1][iy]=diff_xr(r-1,iy,room)
      room_ins[0][0]=diff_x1y1(0,0,room)
      room_ins[0][c-1]=diff_x1yc(0,c-1,room)
      room_ins[r-1][0]=diff_xry1(r-1,0,room)
      room_ins[r-1][c-1]=diff_xryc(r-1,c-1,room)
      
      room_ins[g[0]][0]=0
      room_ins[g[1]][0]=0
      
      room_ins[g[0]-1][0]=room[g[0]-2][0]//5+room[g[0]-1][1]//5-(room[g[0]-1][0]//5)*2
      room_ins[g[1]+1][0]=room[g[1]+2][0]//5+room[g[1]+1][1]//5-(room[g[1]+1][0]//5)*2
      room_ins[g[0]][1]=room[g[0]+1][1]//5+room[g[0]-1][1]//5+room[g[0]][2]//5-(room[g[0]][1]//5)*3
      room_ins[g[1]][1]=room[g[1]+1][1]//5+room[g[1]-1][1]//5+room[g[1]][2]//5-(room[g[1]][1]//5)*3
      
      for ix in range(r):
          for iy in range(c):
              room[ix][iy]+=room_ins[ix][iy]
      
      
      return room
  
  def cir(room,r,c):
      for ix in range(g[0]-1,0,-1):
          room[ix][0]=room[ix-1][0]
      for iy in range(c-1):
          room[0][iy]=room[0][iy+1]
      for ix in range(g[0]):
          room[ix][c-1]=room[ix+1][c-1]
      for iy in range(c-1,1,-1):
          room[g[0]][iy]=room[g[0]][iy-1]
      room[g[0]][1]=0
      
      for ix in range(g[1]+1,r-1):
          room[ix][0]=room[ix+1][0]
      for iy in range(c-1):
          room[r-1][iy]=room[r-1][iy+1]
      for ix in range(r-1,g[1],-1):
          room[ix][c-1]=room[ix-1][c-1]
      for iy in range(c-1,1,-1):
          room[g[1]][iy]=room[g[1]][iy-1]
      room[g[1]][1]=0
      return room    
      
  
  for _  in range(t):
      room_given=diff(room_given,r,c)
      room_given=cir(room_given,r,c)
  
  summ=2
  for ix in range(r):
      for iy in range(c):
          summ=summ+room_given[ix][iy]
      
  print(summ)
  ```
  
  > 

