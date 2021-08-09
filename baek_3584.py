# python

## baek 3584 가장 가까운 공통 조상 골드4

https://www.acmicpc.net/problem/3584

> python3 136ms

* 문제

  > 루트가 있는 트리(rooted tree)가 주어지고, 그 트리 상의 두 정점이 주어질 때 그들의 가장 가까운 공통 조상(Nearest Common Anscestor)은 다음과 같이 정의됩니다.
  >
  > - 두 노드의 가장 가까운 공통 조상은, 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드를 말합니다.
  >
  > ![nca.png](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 예를 들어 15와 11를 모두 자손으로 갖는 노드는 4와 8이 있지만, 그 중 깊이가 가장 깊은(15와 11에 가장 가까운) 노드는 4 이므로 가장 가까운 공통 조상은 4가 됩니다.
  >
  > 루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요

* 입력

  > 첫 줄에 테스트 케이스의 개수 T가 주어집니다.
  >
  > 각 테스트 케이스마다, 첫째 줄에 트리를 구성하는 노드의 수 N이 주어집니다. (2 ≤ N ≤ 10,000)
  >
  > 그리고 그 다음 N-1개의 줄에 트리를 구성하는 간선 정보가 주어집니다. 한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻입니다. (당연히 정점이 N개인 트리는 항상 N-1개의 간선으로 이루어집니다!) A와 B는 1 이상 N 이하의 정수로 이름 붙여집니다.
  >
  > 테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.
  >
  > ```bash
  > 2
  > 16
  > 1 14
  > 8 5
  > 10 16
  > 5 9
  > 4 6
  > 8 4
  > 4 10
  > 1 13
  > 6 15
  > 10 11
  > 6 7
  > 10 2
  > 16 3
  > 8 1
  > 16 12
  > 16 7
  > 5
  > 2 3
  > 3 4
  > 3 1
  > 1 5
  > 3 5
  > ```
  >
  
* 출력

  > 각 테스트 케이스 별로, 첫 줄에 입력에서 주어진 두 노드의 가장 가까운 공통 조상을 출력합니다.
  >
  > ```bash
  > 4
  > 3
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    t = int(input())

    for _ in range(t):
        n = int(input())
        parents = [0] * (n+1)

        dic, res = {}, 0

        for _ in range(n-1):
            a, b = map(int, input().split())
            parents[b] = a

        n1, n2 = map(int, input().split())
        dic[n1], dic[n2] = 1, 1
        q = deque([[n1, n2]])

        while q:
            node1, node2 = q.popleft()
            next_node1, next_node2 = parents[node1], parents[node2]

            if next_node1 and next_node1 in dic:
                res = next_node1
                break

            dic[next_node1] = 1

            if next_node2 and next_node2 in dic:
                res = next_node2
                break

            dic[next_node2] = 1

            q.append([next_node1, next_node2])

        print(res)


sol()
```

> 



* 모범답안

  ```python
  92
  
  import sys
  def find_nodelist(node,tree):
      result=[node]
      while tree[node] != 0:
          result.append(tree[node])
          node=tree[node]
      return result
  
  def solution():
      T=int(sys.stdin.readline())
      for _ in range(T):
          N=int(sys.stdin.readline())
          tree=[0]*(N+1)
          for _ in range(N-1):
              A,B=map(int,sys.stdin.readline().split())
              tree[B]=A
          node1, node2=map(int,sys.stdin.readline().split())
  
          node1_List=find_nodelist(node1,tree)
          node2_List=find_nodelist(node2,tree)
  
          # 뒤 부터 탐색 무조건 root 노드부터 이기 때문에
          pre=0
          for a,b in zip(node1_List[::-1],node2_List[::-1]):
              if a==b:
                  pre=a
              else:
                  print(pre)
                  break
          else:
              print(pre)
  solution()
  ```

  > 아 루트부터 시작해서 어긋날 때 종료하는구나. 근데 이게 내것보다 빠르다니.. 난 자식 노드에서 시작해서 거슬러 올라간다음 일치되는 곳에서 끝나는 게 당연히 빠르다고 생각했는데 ㅜㅜ
