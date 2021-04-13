# python

## baek 2458 키 순서 골드4

https://www.acmicpc.net/problem/2458

> python3 828ms
>
> pypy3 204ms



* 문제

  > 1번부터 N번까지 번호가 붙여져 있는 학생들에 대하여 두 학생끼리 키를 비교한 결과의 일부가 주어져 있다. 단, N명의 학생들의 키는 모두 다르다고 가정한다. 예를 들어, 6명의 학생들에 대하여 6번만 키를 비교하였고, 그 결과가 다음과 같다고 하자. 
  >
  > - 1번 학생의 키 < 5번 학생의 키
  > - 3번 학생의 키 < 4번 학생의 키
  > - 5번 학생의 키 < 4번 학생의 키
  > - 4번 학생의 키 < 2번 학생의 키
  > - 4번 학생의 키 < 6번 학생의 키
  > - 5번 학생의 키 < 2번 학생의 키
  >
  > 이 비교 결과로부터 모든 학생 중에서 키가 가장 작은 학생부터 자신이 몇 번째인지 알 수 있는 학생들도 있고 그렇지 못한 학생들도 있다는 사실을 아래처럼 그림을 그려 쉽게 확인할 수 있다. a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다. 
  >
  > ![img](md-images/ccc.png)
  >
  > 1번은 5번보다 키가 작고, 5번은 4번보다 작기 때문에, 1번은 4번보다 작게 된다. 그러면 1번, 3번, 5번은 모두 4번보다 작게 된다. 또한 4번은 2번과 6번보다 작기 때문에, 4번 학생은 자기보다 작은 학생이 3명이 있고, 자기보다 큰 학생이 2명이 있게 되어 자신의 키가 몇 번째인지 정확히 알 수 있다. 그러나 4번을 제외한 학생들은 자신의 키가 몇 번째인지 알 수 없다. 
  >
  > 학생들의 키를 비교한 결과가 주어질 때, 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 학생들의 수 N (2<=N<=500)과 두 학생 키를 비교한 횟수 M (0<=M<=N(N-1)/2)이 주어진다. 다음 M개의 각 줄에는 두 학생의 키를 비교한 결과를 나타내는 두 양의 정수 a와 b가 주어진다. 이는 번호가 a인 학생이 번호가 b인 학생보다 키가 작은 것을 의미한다. 
  >
  > ```python
  > 6 6
  > 1 5
  > 3 4
  > 5 4
  > 4 2
  > 4 6
  > 5 2
  > ```
  >
  > 

* 출력

  > 자신이 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지를 출력한다. 
  >
  > ```python
  > 1
  > ```



```python
import sys
input = sys.stdin.readline


def dfs(start, go):
                            # 1. dfs로 돌아가며 체크
    if start != go:     
                            # 2. 현재 노드와 거쳐가는 노드가 같지 않다면
        visitnode[start] += 1   
                            # 3. 각자 갈 수 있는 리스트에 1씩 추가
        visitnode[go] += 1
    visited[go] = 1     
                            # 4. 현재 노드에서 거쳐가는 노드로 방문했다고 표시
    for j in arr[go]:   
                            # 5. 거쳐가는 노드에서 갈 수 있는 노드 확인
        if not visited[j]:      
                            # 6. 아직 현재 노드에서 방문하지 않은 노드라면
            dfs(start, j)       
                            # 7. 1번부터 반복


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

res = 0
visitnode = [0] * (n+1)     # 각자 방문할 수 있는 노드 덧셈
for i in range(1, n+1):     # 1번 노드부터 돌면서
    visited = [0] * (n+1)   # 방문 표시 초기화
    dfs(i, i)               # dfs

for i in visitnode:         # 방문 가능한 노드 중,
    if i == n-1:            # 자기 자신 빼고 모두 방문할 수 있는 노드가 존재한다면
        res += 1            # 결과값 ++

print(res)
```

> 아직도 제대로 이해못한 것 같은데,, 플루이드 맞나,,? 너무 어렵다..
>
> 대신 플루이드가 좋은 건 일부러 노드 개수를 적게 준다는 점이다. 메모리 초과를 우려해서 그런 건가.. 하... 근데 나는 진짜,, 효율화를 개선하는 방법을 배울 필요가 있음.



* 모범답안

  ```python
  808
  
  import sys
  input = sys.stdin.readline
  
  def dfs(start, cur):
      if start != cur:
          edge_cnt[start] += 1
          edge_cnt[cur] += 1
      visited[cur] = True
      for w in graph[cur]:
          if not visited[w]:
              dfs(start, w)
  
  
  N, M = list(map(int, input().split()))
  graph = [[] for _ in range(N+1)]
  ans = 0
  for _ in range(M):
      a, b = list(map(int, input().split()))
      graph[a].append(b)
  
  edge_cnt = [0] * (N+1)
  for node in range(1, N+1):
      visited = [False] * (N+1)
      dfs(node, node)
  
  
  for node in range(1, N+1):
      if edge_cnt[node] == N-1:
          ans += 1
  
  print(ans)
  ```

  > 

