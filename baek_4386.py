# python

## baek 4386 별자리 만들기 골드4

https://www.acmicpc.net/problem/4386

> python3 76ms
>
> pypy3 152ms



* 문제

  > 도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
  >
  > - 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
  > - 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
  >
  > 별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

* 입력

  > 첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
  >
  > 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.
  >
  > ```python
  > 3
  > 1.0 1.0
  > 2.0 2.0
  > 2.0 4.0
  > ```
  >
  > 

* 출력

  > 첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.
  >
  > ```python
  > 3.41
  > ```



```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        p[a] = b
    else:
        p[b] = a


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


n = int(input())
star = []
arr = []
v = [0 for _ in range(n)]
p = [i for i in range(n)]
res, count = 0, 0
for _ in range(n):
    a, b = map(float, input().split())
    star.append([a, b])

for i in range(n):
    for j in range(i+1, n):
        heappush(arr, [((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5, i, j])

for i in range(len(arr)):
    wt, n1, n2 = heappop(arr)
    if find(p[n1]) != find(p[n2]):
        res += wt
        union(n1, n2)
        count += 1
    if count == n-1:
        break

print(res)
```

> 우여곡절이 꽤 있었던 코드.
>
> 1. 유니온파인드로 사용하되, 각 2차원 배열에 맞게 거리를 계산해서 배열에 넣었음. 그리고 최솟값을 찾기 위해 arr[i].index(min(arr[i])) 이런 코드를 썼다. 이 코드를 썼을 때 뭔가 잘못되어 가고 있음을 느꼈어야 했는데 전혀 느끼지 못했고,,
> 2. 그리고 union을 잘못 썼다고 생각했는데 find를 잘못 썼었다. `p[a] = find(p[a])` 이부분이었는데 이부분을 처음에 p[a] = find(a) 이렇게 썼었다. 진짜... 왜그러나 몰라. 
> 3. 이때 진짜 이상함을 느꼈다.. 방문했던 노드는 재차 방문하지 않기로 바꾸면서 코드가 엄청 해괴망측해져갔다.
> 4. 그래서 다 갈아엎고 heapq를 써보기로 했다. 써보고 싶었는데 이때 써서 정말 다행이다.
> 5. 거리, 현재노드, 측정노드 형태로 heap에 넣었음.
> 6. 그걸 이제 pop해주며 계산해 주는데 여기서 또 바보 같은 실수를 했음.
> 7. `find(p[n1]) != find(p[n2]):`  : 바로 이부분인데 find를 안하고 그냥 p[n1] != p[n2]를 했다. 이러면 부모노드까지 미치지 못해서 당연히 틀릴 수 밖에..
> 8. 그래도 이문제를 풀어보며 mst를 조금은 이해하는 단계까진 온 것 같다.



* 모범답안

  ```python
  # 내코드가 제일 빠름
  ```

  > 

