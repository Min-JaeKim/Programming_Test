# Python

## baek 13418 학교 탐방하기 골드3

https://www.acmicpc.net/problem/1197



> python3 1312ms
>
> pypy3 864ms



* 문제

  > 국민대학교 홍보대사 국희는 여름방학을 맞아 고등학생들을 대상으로 학교 내부에 있는 건물을 소개해주는 일을 하게 되어 학교 건물을 차례로 소개할 수 있는 이동 경로를 짜보기로 하였다. 국민대학교는 북한산의 정기를 받는 위치에 있어 건물 간 연결된 길이 험난한 오르막길일 수도 있고, 내리막길일 수도 있다. 국희는 먼저 입구를 기준으로 건물 간 연결된 도로가 오르막길인지, 내리막길인지를 파악하여 오르막길인 경우 점선, 내리막길인 경우 실선으로 표시하였다.
  >
  > ![img](md-images/F1.png)
  >
  > 그림 1
  >
  > 건물을 구분하기 쉽도록 번호를 붙였고, **입구에는 숫자 0**을 붙이기로 하였다. 그 다음 모든 건물을 방문하는 데 필요한 최소한의 길을 선택하여, 해당 길을 통해서만 건물들을 소개하기로 하였다. 이 과정은 굉장히 신중해야 하는데, 오르막길이 많이 포함되게 되면 굉장히 피곤해지기 때문이다.
  >
  > 얼마나 피곤해지는지 알아보기 위해 피로도를 계산하기로 하였다. 오르막길을 *k*번 오를 때, 피로도는 *k*2이 된다. 피로도의 계산은 최초 조사된 길을 기준으로만 한다. 즉, 내리막길로 내려갔다 다시 올라올 때 오르막길이 되는 경우는 **고려하지 않는다**. 입구는 항상 1번 건물과 연결된 도로를 가지며, 출발은 항상 입구에서 한다.
  >
  > ![img](md-images/F2.png)
  >
  > 그림 2
  >
  > ![img](md-images/F3.png)
  >
  > 그림 3
  >
  > 그림 1에서 모든 건물을 소개하기 위해 거쳐야 할 최소한의 도로는 4개임을 알 수 있다. 다음 2개의 그림은 그 4개의 도로를 뽑은 각각의 경우이다. 그림 2는 학교를 소개하는 데 총 3개의 오르막길을 오르게 되며 피로도가 9가 되는 최악의 코스가 된다. 그림 3은 오르막길을 1번만 오르게 되므로 학생들의 피로도는 1이 되는 최적의 코스가 된다. 이 경우 최악의 코스와 최적의 코스간 최종 피로도의 차이는 8이 된다. 국희는 최고의 프로그래머인 당신에게 위와 같은 방식으로 최악, 최선의 경로 간 피로도의 차이를 계산하는 프로그램의 제작을 부탁하였다. 프로그램을 작성하여 국희를 도와주자.

* 입력

  > 입력 데이터는 표준 입력을 사용한다. 입력은 1개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 건물의 개수 N(1≤N≤1,000)과 도로의 개수 M(1≤M≤n*(n-1)/2) 이 주어진다. 입력의 두 번째 줄부터 M+1개의 줄에는 A, B(1≤ A,B ≤ N), C 가 주어진다. 이는 A와 B 건물에 연결된 도로가 있다는 뜻이며, C는 0(오르막길) 또는 1(내리막길)의 값을 가진다. 같은 경로 상에 2개 이상의 도로가 주어지는 경우는 없으며, 입구는 항상 1번 건물과 연결되어 있다. 입구와 1번 도로 간의 연결 관계는 항상 2번째 줄에 주어진다. 입구에서 모든 건물로 갈 수 있음이 보장된다.
  >
  > ```bash
  >4 5
  > 0 1 1
  > 1 2 0
  > 1 4 0
  > 4 2 1
  > 3 4 1
  > 2 3 0
  > ```
  
* 출력

  > 출력은 표준 출력을 사용한다. 입력받은 데이터에 대해, 주어진 조건을 만족하는 최악의 경로에서의 피로도와 최적의 경로 간 피로도의 차이를 출력한다.
  >
  > ```bash
  > 8
  > ```



```python
'''
로직설명.
1. 모든 간선을 배열에 넣되, 내리막이 먼저 오도록 정렬,
2. 1의 가중치의 합.
3. 오르막이 먼저 오도록 정렬.
4. 2의 가중치의 합.
5. 4번에서 나온 값의 제곱 - 2번에서 나온 값의 제곱
6. cnt변수를 써서 더 빨리 반복문을 탈출할 수 있도록..
'''

import sys
input = sys.stdin.readline

def find(num):
    if parents[num] == num:
        return num
    parents[num] = find(parents[num])
    return parents[num]


def union(i, j):
    i = find(i)
    j = find(j)
    if i > j:
        parents[i] = j
    else:
        parents[j] = i


n, m = map(int, input().split())
arr = []
parents = [i for i in range(n+1)]
for _ in range(m+1):
    a, b, c = map(int, input().split())
    c = 0 if c == 1 else 1
    # 0이 오르막인 게 헷갈려서 0을 내리막으로 바꿈
    arr.append([a, b, c])

maxre, minre, cnt = 0, 0, 0

arr.sort(key = lambda x : x[2])     # 내리막길 정렬~
for i, j, road in arr:              # union find
    if find(i) != find(j):
        cnt += 1
        minre += road
        union(i, j)
    if cnt == n:                    # 모든 간선을 셌다면
        break                       # 반복문 탈출

parents, cnt = [i for i in range(n+1)], 0   # 부모 초기화
arr.sort(key = lambda x : -x[2])    # 오르막길 정렬
for i, j, road in arr:
    if find(i) != find(j):
        cnt += 1
        maxre += road
        union(i, j)
    if cnt == n:
        break

print(maxre*maxre - minre*minre)
```

> mst를 이해하느라 이걸 거진 3일 붙잡고 있던듯.. 이것만 푼 건 아니고 그냥 ㅎㅎ 3일동안 마음아파할 만큼 고민했음.
>
> 암튼 이문제를 풀고나니 mst를 제대로 이해하게 된 것 같아서 다행.
>
> `parents[num] = find(parents[num])` : 이부분이 중요한데, 이 코드를 돌면서 부모를 찾아가는 배열 마저 다 부모로 바꿔줌.



* 모범답안

  ```python
  1296
  
from _collections import deque
  input = __import__('sys').stdin.readline
  
  class DisjointSet:
      def __init__(self, n): self.par = list(range(n+1)); self.rank = [0]*(n+1)
      def union(self, x, y):
          x,y = self.find(x),self.find(y)
          if x==y: return
          xr,yr = self.rank[x], self.rank[y]
          if xr<yr: self.par[x]=y
          else:
              self.par[y]=x
              if xr==yr: self.rank[x]+=1
      def find(self, x):
          if self.par[x] != x: self.par[x] = self.find(self.par[x])
          return self.par[x]
  
  n,m = map(int,input().split())
  e = deque()
  for i in range(m+1):
      a,b,c = map(int,input().split())
      if c: e.appendleft((0,a,b))
      else: e.append((1,a,b))
  cost1 = 0
  D = DisjointSet(n)
  cnt = 0
  for c,a,b in e:
      if D.find(a)!=D.find(b):
          cnt+=1
          cost1+=c
          D.union(a,b)
      if cnt==n: break
  D = DisjointSet(n)
  cnt = 0
  cost2 = 0
  cost1**=2
  for i in range(m+1):
      c,a,b = e.pop()
      if D.find(a)!=D.find(b):
          cnt+=1
          cost2+=c
          D.union(a,b)
      if cnt==n: break
  cost2**=2
  print(cost2-cost1)
  ```
  
  > cnt를 써서그런가? 빠른듯
  >
  > 오 맞았음..
  >
  > 나도 cnt변수 써보니 500ms 아낄 수 있었다.