# python

## baek 1939 중량제한 골드4

https://www.acmicpc.net/problem/1939

> pypy3 688ms

* 문제

  > N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.
  >
  > 영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.
  >
  > 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 N, M(1 ≤ M ≤ 100,000)이 주어진다. 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)가 주어진다. 이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다. 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.
  >
  > ```bash
  > 3 3
  > 1 2 2
  > 3 1 3
  > 2 3 2
  > 1 3
  > ```
  >
  
* 출력

  > 첫째 줄에 답을 출력한다.
  >
  > ```bash
  > 3
  > ```



- 

```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        arr[a].append([b, c])
        arr[b].append([a, c])

    s1, s2 = map(int, input().split())
    left, right, res = 1, 1000000001, 0

    while left < right:
        mid = (left + right) // 2
        v = [0] * (n+1)
        q, flag = deque([]), False
        q.append(s1)
        v[s1] = 1

        while q:
            node = q.popleft()

            if node == s2:
                flag = True
                break

            for node2, wt in arr[node]:
                if mid < wt and not v[node2]:
                    q.append(node2)
                    v[node2] = 1

        if flag:
            left = mid + 1
        else:
            right = mid

    print(right)


sol()
```

> 아직도 이분탐색 헷갈리는 게 뭐냐면..
>
> left와 right 를 계산할 때 1을 증가 시킬지 냅둘지, 1을 감소시킬지 냅둘지에 대한 것이다.. 더많이 풀어봐야지
>
> 이번 코드의 키포인트는
>
> `mid < wt`
>
> 이거임. 어쨌든 중량제한을 넘는 게 있을 때만 flag를 True로 줬고, 그로 인해 left에 1을 추가해 주며 답 찾는 범위를 좁혀 나갔다. 만약 딱 맞는 게 있다면 flag 함수에서 false를 받았을 것이므로 right 를 mid에 맞출 수 있었음.



* 모범답안

  ```python
  264
  
  import sys
  
  input = sys.stdin.readline
  sys.setrecursionlimit(10**6)
  
  
  def find_parent(parent, x):
      if parent[x] != x:
          parent[x] = find_parent(parent, parent[x])
      return parent[x]
  
  
  def union_parent(parent, a, b):
      a = find_parent(parent, a)
      b = find_parent(parent, b)
      if a < b:
          parent[b] = a
      else:
          parent[a] = b
  
  
  N, M = map(int, input().split())
  parent = [i for i in range(N+1)]
  graph = []
  
  for _ in range(M):
      A, B, C = map(int, input().split())
      graph.append((C, A, B))
  
  # 공장 입력 받기
  x, y = map(int, input().split())
  
  # 다리가 들 수 있는 중량이 큰 것부터 내림차순으로 정렬
  graph.sort(key=lambda i: i[0], reverse=True)
  
  for cost, a, b in graph:
      # 다리 연결
      union_parent(parent, a, b)
      # 두 공장이 연결 되었을 때
      if find_parent(parent, x) == find_parent(parent, y):
          # 현재 중량 출력
          print(cost)
          break
  ```

  > 엥 이거 유니온파인드를 쓸 수 있는 거였나..
  >
  > 그렇군,, 무거운 것부터 세어가면서 ,, 하나씩 이을 때마다 섬 두 개가 연결되어 있는 지 확인하면 됨.

