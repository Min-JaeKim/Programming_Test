# python

## baek 2660 회장뽑기 골드5

https://www.acmicpc.net/problem/2660

> python3 72ms
>



* 문제

  > 월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.
  >
  > 예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.
  >
  > 4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.
  >
  > 회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.
  
* 입력

  > 입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.
  >
  > ```bash
  > 5
  > 1 2
  > 2 3
  > 3 4
  > 4 5
  > 2 4
  > 5 3
  > -1 -1
  > ```
  >
  
* 출력

  > 첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.
  >
  > ```bash
  > 2 3
  > 2 3 4
  > ```



```python
import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    arr = [[float('inf')] * (n+1) for _ in range(n+1)]
    arrsum = [float('inf')]

    while 1:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        arr[a][b] = 1
        arr[b][a] = 1
        arr[a][a] = 0
        arr[b][b] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if arr[i][k] + arr[k][j] < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]

    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            if tmp < arr[i][j]:
                tmp = arr[i][j]
        arrsum.append(tmp)

    candicnt = min(arrsum)
    candi = []

    for i in range(1, n+1):
        if arrsum[i] == candicnt:
            candi.append(i)

    print(candicnt, len(candi))
    print(*(sorted(candi)))

sol()
```

> 플로이드,, 내가 간과하고 있던 부분은 자기 자신은 항상 0으로 초기화해 줘야 한다는 것이다. 



* 모범답안

  ```python
  60
  
  def getpt(i):
      visited = [False for _ in range(n+1)]
      q = [i]
      visited[i] = True
      point = -1
      while len(q) > 0:
          qsize = len(q)
          for _ in range(qsize):
              h = q.pop()
              for j in g[h]:
                  if visited[j]:
                      continue
                  visited[j] = True
                  q.insert(0, j)
          point += 1
      return point
  
  
  n = int(input())
  g = [[] for _ in range(n+1)]
  while True:
      a, b = map(int, input().split())
      if a == -1:
          break
      if b not in g[a]:
          g[a].append(b)
      if a not in g[b]:
          g[b].append(a)
  
  
  p = [0 for _ in range(n+1)]
  for i in range(1, n+1):
      p[i] = getpt(i)
  
  m = min(p[1:])
  candidates = []
  for i, x in enumerate(p):
      if i == 0:
          continue
      if x == m:
          candidates.append(str(i))
  
  print(m, len(candidates))
  print(' '.join(candidates))
  ```

  > 이렇게 풀 수도 있구나
  >
  > 모든 사람에게 각각의 배열이 주어지고 거기에 자신과 친구인 모든 사람을 넣는다. 그리고 다익스트라로 다니면서 최대 친구의 거리를 구함. 그리고 그거를 enumerate로 지나다니며 값을 구한다.

