# python

## baek 17135 캐슬 디펜스 골드4

https://www.acmicpc.net/problem/17135

> python3 436ms
>



* 문제

  > 캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.
  >
  > 성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. 
  >
  > 게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.
  >
  > 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
  
* 입력

  > 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.
  >
  > ```bash
  > 6 5 1
  > 1 0 1 0 1
  > 0 1 0 1 0
  > 1 1 0 0 0
  > 0 0 0 1 1
  > 1 1 0 1 1
  > 0 0 1 0 0
  > ```
  >
  
* 출력

  > 첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.
  >
  > ```bash
  > 9
  > ```



```python
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def sol():

    # bfs로 가장 가까운 적을 찾음
    def bfs(a):
        v = [[0] * m for _ in range(n + 1)]
        q = deque([a])
        v[a[0]][a[1]] = 1

        while q:
            r, c, dist = q.popleft()
            if tmparr[r][c] == 1:
                enemy.append([r, c])
                break
                
            # 방향은 왼 위 오
            for i in range(3):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n + 1 and 0 <= nc < m and \
                        not v[nr][nc] and dist + 1 <= d:
                    q.append([nr, nc, dist + 1])
                    v[nr][nc] = 1

    dr = (0, -1, 0)
    dc = (-1, 0, 1)
    n, m, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 궁수를 위치할 한 줄 추가
    arr.append([0 for _ in range(m)])
    archer = [i for i in range(0, m)]
    # 궁수 좌표는 combination으로
    archer = [c for c in combinations(archer, 3)]
    res = 0
    
    # combination으로 선정한 궁수 좌표를 돌면서
    for a in archer:

        # 매번 맵을 새로 만들어주고, 경우마다 죽인 적을 새로 새어줌
        tmparr, kill = [[0] * m for _ in range(n+1)], 0

        for i in range(n + 1):
            tmparr[i] = arr[i][:]

        # 적이 없을 때까지 반복하며
        while 1:

            enemy = []
            
            # 궁수마다 bfs 돌려줌
            a1, a2, a3 = [n, a[0], 0], [n, a[1], 0], [n, a[2], 0]
            bfs(a1)
            bfs(a2)
            bfs(a3)
            
            # 중복 적을 제거하며 죽인 적을 세어주고
            for i in range(len(enemy)):
                if tmparr[enemy[i][0]][enemy[i][1]]:
                    kill += 1
                    tmparr[enemy[i][0]][enemy[i][1]] = 0
            
            # 적들의 좌표를 아래로 하나 씩 땡겨줌.
            del(tmparr[n-1])
            tmparr.insert(0, [0] * m)
            flag = 0
            
            # 만약 적이 아직도 존재한다면 계속 while문 돌려줌
            for i in range(n+1):
                for j in range(m):
                    if tmparr[i][j] == 1:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                break
        
        # 최대로 적을 많이 죽인 횟수를 결과값에
        res = max(res, kill)

    print(res)


sol()
```

> 처음에 문제를 잘못이해하는 바람이 적이 한 칸 씩 이동할 때마다 계속 combi를 돌렸었다. 그런데 그렇게 짜다보니까 이러는데 어떻게 1초만에 가능할까,, 이생각을 하게 도ㅣ었다. 알고보니 궁수는 움직이지 않고 적만 움직이는 거였다. 그래서 코드를 줄일 수 있었다. (솔직히 그래도 시간초과 날까봐 염려했지만 15개에서 3개 뽑는 건 별루 시간 초과 안나는듯 다행)
>
>  문제는 append였다. tmparr에 arr를 append할 때마다 메모리가 새로 추가되어 다음 combi일 때 영향을 끼치지 않을 것이라고 생각했다. 하지만 전혀 그렇지 않았다. 그래서 빠르게 tmparr 배열 미리 생성해 놓고 arr[ i ] [ : ] 와 같이 바꿨음... ㅠ
>
> 근데 왜 시간이 다른 사람보다 오래나왔냐,,, 하면,,, 단순히 맵을 del이랑 append하였기 때문이었을까



* 모범답안

  ```python
  # 궁수자리 3개 뽑는거
  def location(idx=-1,num=3,position=[]):
      global M,ans
  
      if num==0:
          cnt = defence(position)
          ans= max(ans,cnt)
          return
  
      for i in range(idx+1,M-num+1):
          position.append(i)
          location(i,num-1,position)
          position.pop()
  
# 궁수 전진
  def defence(position):
      global N,M
      # 복제
      enemy_copy = [0] * N
      for i in range(N):
          enemy_copy[i] = enemy[i][:]
  
      cnt_attack=0
      arc1 ,arc2, arc3 = position
      for i in range(N-1,-1,-1):
          a = shoot(i, arc1 , enemy_copy)
          b = shoot(i, arc2 , enemy_copy)
          c = shoot(i, arc3 , enemy_copy)
          attack = set()
          if a: attack.add((a[0],a[1]))
          if b: attack.add((b[0], b[1]))
          if c: attack.add((c[0], c[1]))
          cnt_attack+=len(attack)
          for j,k in attack:
              enemy_copy[j][k]=0
      return cnt_attack
  
  # 발사
  # 같은 거리일 때 가장 왼쪽에 있는 적 공격
  # 화살 발사하고 삼각형을 그린다고 생각하면 된다.
  def shoot(a, b, enemy_copy):
      global N,M,D
      if enemy_copy[a][b]==1:
          return (a,b)
  
      arrow=[(a,b,1)]
      st=0
      while arrow:
          r,c,d=arrow[st]
          st+=1
          if d>D:
              return False
          for nr,nc in (r,c-1),(r-1,c),(r,c+1):
              if not(0<=nr<N and 0<=nc<M): continue
              if (nr,nc,d+1) in arrow: continue
              if enemy_copy[nr][nc]==1:
                  if d+1>D:
                      continue
                  return (nr,nc)
              else:
                  arrow.append((nr,nc,d+1))
          if st==len(arrow):      # st가 인덱스 초과한것
              return False
      # return False
  
  
  N,M,D=map(int,input().split())
  enemy=[list(map(int, input().split())) for _ in range(N)]
  
  ans=0
  location()
  print(ans)
  ```
  
  > 

