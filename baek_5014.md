# python

## baek 5014 스타트링크 골드5

https://www.acmicpc.net/problem/5014

> python3 676ms
>



* 문제

  > 강호는 코딩 교육을 하는 스타트업 [스타트링크](https://startlink.io/)에 지원했다. 오늘은 강호의 면접날이다. 하지만, 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.
  >
  > 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
  >
  > 보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
  >
  > 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오. 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.
  
* 입력

  > 첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.
  >
  > ```bash
  >10 1 10 2 1
  > ```
  >
  
* 출력

  > 첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.
  >
  > ```bash
  > 6
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    f, s, g, u, d = map(int, input().split())
    v = set()
    q = deque([])
    v.add(s)
    q.append([s, 0])

    while q:
        kh, cnt = q.popleft()

        if kh == g:
            print(cnt)
            exit()

        if kh + u <= f and kh + u not in v:
            v.add(kh+u)
            q.append([kh+u, cnt+1])
        if kh - d > 0 and kh - d not in v:
            v.add(kh-d)
            q.append([kh-d, cnt+1])

    print('use the stairs')


sol()
```

> 



* 모범답안

  ```python
  324
  
  import sys
  
  def dfs1(cr, vi, f, g, u, d, n):
      vi[cr] = 1
      if (cr == g):
          return n
      for i in range(f):
          if (cr == g):
              return n
          elif (cr < g):
              if (cr + u <= f):
                  cr += u
                  n += 1
                  if vi[cr] == 1:
                      return -1
                  else:
                      vi[cr] = 1
              elif (cr - d > 0):
                  cr -= d
                  n += 1
                  if vi[cr] == 1:
                      return -1
                  else:
                      vi[cr] = 1
              else:
                  return -1
          else:
              if (cr - d > 0):
                  cr -= d
                  n += 1
                  if vi[cr] == 1:
                      return -1
                  else:
                      vi[cr] = 1
              elif (cr + u <= f):
                  cr += u
                  n += 1
                  if vi[cr] == 1:
                      return -1
                  else:
                      vi[cr] = 1
              else:
                  return -1
  
      return -1
  
  input = sys.stdin.readline
  
  F, S, G, U, D = list(map(int, input().split()))
  
  visited = [0]*(F+1)
  
  num = 0
  result = dfs1(S, visited, F, G, U, D, num)
  
  if result != -1:
      print(result) 
  else:
      print("use the stairs")
  ```
  
  > 아 set에다 추가하는 게 아니라 그 건물 층수만큼 visit 배열을 만들어 줬구나.
  >
  > 

