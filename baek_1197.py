# Python

## baek 1197 최소 스패닝 트리 골드4

https://www.acmicpc.net/problem/1197



> python3 356ms
>
> pypy3 372ms



* 문제

  > 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
  >
  > 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

* 입력

  > 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
  >
  > 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
  >
  > ```bash
  > 3 3
  > 1 2 1
  > 2 3 2
  > 1 3 3
  > ```
  
* 출력

  > 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
  >
  > ```bash
  > 3
  > ```



```python
import sys
input = sys.stdin.readline


def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]


def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)

    if node1 < node2:
        parents[node2] = node1
    else:
        parents[node1] = node2


v, e = map(int, input().split())
arr, result = [], 0
parents = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

arr.sort(key = lambda x : x[2])

for a, b, c in arr:
    if find(a) != find(b):
        result += c
        union(a, b)

print(result)
```

> 가벼운 mst문제..
>
> 이문제에서 거의 2배 가량 시간을 차이나게 했던 부분은 
>
> `arr.sort(key = lambda x : x[2])`
>
> 여기다. 실질적으로 가중치만 정렬하면 되고, 노드는 굳이 정렬하지 않아도 되기 때문,,



* 모범답안

  ```python
  312
  
# kruskal-mst
  import sys
  
  
  def find_parent(parent, x):
      t = x
      while t != parent[t]:
          t = parent[t]
      parent[x] = t
      return parent[x]
  
  
  def union(parent, rank, x, y):
      a = find_parent(parent, x)
      b = find_parent(parent, y)
      if rank[a] > rank[b]: parent[b] = a
      else:
          parent[a] = b
          if rank[a] == rank[b]:
              rank[b] += 1
  
  
  def main():
      input = sys.stdin.readline
      v,e = map(int, input().split())
      edges = []
      rank = [0] * (v + 1)
      parent = [0] * (v + 1)
      for i in range(1, v + 1):
          parent[i] = i
      res = 0
      for _ in range(e):
          a, b, cost = map(int, input().split())
          edges.append((cost, a, b))
      edges.sort()
      for edge in edges:
          cost, a, b = edge
          if find_parent(parent, a) != find_parent(parent, b):
              union(parent, rank, a, b)
              res += cost
      return res
  
  print(main())
  ```
  
  > sort가 빠른지 lambda가 빠른지 모르겠다..