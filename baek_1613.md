# python

## baek 1613 역사 골드3

https://www.acmicpc.net/problem/1613

> python3 592ms



* 문제

  > 역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.
  >
  > 세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.

* 입력

  > 첫째 줄에 첫 줄에 사건의 개수 n(400 이하의 자연수)과 알고 있는 사건의 전후 관계의 개수 k(50,000 이하의 자연수)가 주어진다. 다음 k줄에는 전후 관계를 알고 있는 두 사건의 번호가 주어진다. 이는 앞에 있는 번호의 사건이 뒤에 있는 번호의 사건보다 먼저 일어났음을 의미한다. 물론 사건의 전후 관계가 모순인 경우는 없다. 다음에는 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s(50,000 이하의 자연수)이 주어진다. 다음 s줄에는 각각 서로 다른 두 사건의 번호가 주어진다. 사건의 번호는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
  >
  > ```bash
  >5 5
  > 1 2
  >1 3
  > 2 3
  > 3 4
  > 2 4
  > 3
  > 1 5
  > 2 4
  > 3 1
  > ```
  > 
  
* 출력

  > s줄에 걸쳐 물음에 답한다. 각 줄에 만일 앞에 있는 번호의 사건이 먼저 일어났으면 -1, 뒤에 있는 번호의 사건이 먼저 일어났으면 1, 어떤지 모르면(유추할 수 없으면) 0을 출력한다.
  >
  > ```bash
  > 0
  > -1
  > 1
  > ```



```python
import sys
from collections import defaultdict
input = sys.stdin.readline


def sol():
    n, k = map(int, input().split())
    lose, win = defaultdict(set), defaultdict(set)

    for _ in range(k):
        a, b = map(int, input().split())
        win[a].add(b)
        lose[b].add(a)

    for i in range(1, n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    s = int(input())
    for _ in range(s):
        a, b = map(int, input().split())
        if b not in win[a] and a not in win[b]:
            print(0)
        elif a in win[b]:
            print(1)
        elif b in win[a]:
            print(-1)


sol()
```

> 아아 무슨말인지 알겠어. 그러니까 예를 들어 2라고 치면, lose[2]를 돌 때의 의미는 2를 이긴애들이다. 2를 이긴 애들한테 2가 이긴 애들을 update해 준다.



* 모범답안

  ```python
  352
  
  import sys
  input=sys.stdin.readline
  sys.setrecursionlimit(10**9)
  n,m=map(int,input().split())
  taller=[set() for _ in range(n)]
  e=[[] for _ in range(n)]
  for _ in range(m):
    a,b=map(int,input().split())
    e[a-1].append(b-1)
  v=[0]*n
  def find_taller(i):
    if v[i]: return taller[i]
    v[i]=1
    for j in e[i]:
      taller[i].add(j)
      taller[i]|=find_taller(j)
    return taller[i]
  for i in range(n):
    find_taller(i)
  for _ in range(int(input())):
    a,b=map(int,input().split())
    if b-1 in taller[a-1]: print(-1)
    elif a-1 in taller[b-1]: print(1)
    else: print(0)
  ```
  
  > 내함수에서 따지자면 win 리스트만 이용한 건데 그게 어덯게 통과가 되지? 나는 lose를 지웠을 때 틀렸음 뭘까... 그리고 `|=` 이거는 set의 덧셈.. 한꺼번에 add, update 해 주는 것과 똑같다.

