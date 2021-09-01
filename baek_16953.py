# python

## baek 16953 A -> B 실버1

https://www.acmicpc.net/problem/16953

> python3 300ms

* 문제

  > 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
  >
  > - 2를 곱한다.
  > - 1을 수의 가장 오른쪽에 추가한다. 
  >
  > A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

* 입력

  > 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.
  >
  > ```bash
  > 2 162
  > ```
  >
  
* 출력

  > A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
  >
  > ```bash
  > 5
  > ```



- 틀린 코드

```python
from heapq import *


def sol():
    a, b = map(int, input().split())
    dupl = set()
    dupl.add(a)
    heap, res = [[1, a]], -1

    while heap:
        cnt, num = heappop(heap)

        if num == b:
            print(cnt)
            exit()
        if num > b:
            continue

        tmp1, tmp2 = num * 2, num * 10 + 1

        if tmp1 not in dupl:
            dupl.add(tmp1)
            heappush(heap, [cnt+1, tmp1])
        if tmp2 not in dupl:
            dupl.add(tmp2)
            heappush(heap, [cnt+1, tmp2])

    print(-1)


sol()
```

> 이런 문제 유형은 많이 풀어 보았다.



* 모범답안

  ```python
  56
  
  n,m = map(int,input().split())
  count=0
  while n!=m:
      if n>m:
          count=-2
          break
      elif str(m)[-1]=='1':
          m=m//10
          count+=1
      elif m%2==0:
          m=m//2
          count+=1
      else:
          count=-2
          break
  print(count+1)
  ```

  > 허허 이렇게도 풀 수 있군?
  >
  > 2곱하는 것과 뒷자리가 1로 끝나는 게 겹칠일이 없으니 그 부분을 노려서 잘 푼 것 같다.

