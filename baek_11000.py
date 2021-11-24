# python

## baek 11000 강의실 배정 골드5

https://www.acmicpc.net/problem/11000

> python3 404ms



* 문제

  > 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 
  >
  > 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
  >
  > 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
  >
  > 수강신청 대충한 게 찔리면, 선생님을 도와드리자!
  
* 입력

  > 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
  >
  > 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)
  >
  > ```bash
  > 3
  > 1 3
  > 2 4
  > 3 5
  > ```
  >
  
* 출력

  > 강의실의 개수를 출력하라.
  >
  > ```bash
  > 2
  > ```



```python
import sys
from heapq import *
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    heap = []

    for s, t in arr:
        if heap and heap[0] <= s:
            heappop(heap)
            heappush(heap, t)
        else:
            heappush(heap, t)

    print(len(heap))


sol()
```

> 



* 모범답안

  ```python
  
  ```
  
  > 

