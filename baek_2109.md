# python

## baek 2109 순회강연 골드4

https://www.acmicpc.net/problem/2109

> python3 100ms

* 문제

  > 한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다. 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다. 각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다. 이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다. 강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.
  >
  > 예를 들어 네 대학에서 제시한 p값이 각각 50, 10, 20, 30이고, d값이 차례로 2, 1, 2, 1 이라고 하자. 이럴 때에는 첫째 날에 4번 대학에서 강연을 하고, 둘째 날에 1번 대학에서 강연을 하면 80만큼의 돈을 벌 수 있다.

* 입력

  > 첫째 줄에 정수 n이 주어진다. 다음 n개의 줄에는 각 대학에서 제시한 p값과 d값이 주어진다.
  >
  > ```bash
  >7
  > 20 1
  >2 1
  > 10 3
  >100 2
  > 8 2
  >5 20
  > 50 10
  > ```
  > 
  
* 출력

  > 첫째 줄에 최대로 벌 수 있는 돈을 출력한다.
  >
  > ```bash
  > 185
  > ```



```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def sol():
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], -x[0]))
    res, heap = [], []

    for i in range(n):
        heappush(heap, arr[i][0])
        if len(heap) > arr[i][1]:
            heappop(heap)

    print(sum(heap))


sol()
```

> 아 나는 왜이렇게 바보 같지 너무 서글프다.
>
> heap에 차례차례 담아주되, 현재 진행할 강의들이 for문 강의 제한 일수보다 개수가 많아지면 제일 급여 적은 강의 pop.



* 모범답안

  ```python
  import sys
  from heapq import *
  input=sys.stdin.readline
  n,hq=int(input()),[]
  for a,b in sorted([[*map(int, input().split())] for i in range(n)],key=lambda x:x[1]):
      heappush(hq,a)
      if b<len(hq):heappop(hq)
  print(sum(hq))
  ```

  > 

