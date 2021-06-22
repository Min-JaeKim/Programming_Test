# python

## baek 1202 보석 도둑 골드2

https://www.acmicpc.net/problem/1202

> python3 2176ms
>



* 문제

  > 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
  >
  > 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
  >
  > 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
  >
  > 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
  >
  > 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
  >
  > 모든 숫자는 양의 정수이다.
  >
  > ```bash
  > 3 2
  > 1 65
  > 5 23
  > 2 99
  > 10
  > 2
  > ```
  >
  
* 출력

  > 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
  >
  > ```bash
  > 164
  > ```



```python
from sys import stdin
from heapq import heappush, heappop

def sol():
    input = stdin.readline

    n, k = map(int, input().split())
    jewelry = []
    bag, answer = [], 0

    for _ in range(n):
        heappush(jewelry, list(map(int, input().split())))

    for _ in range(k):
        bag.append(int(input()))

    bag.sort()

    jtmp = []
    for b in bag:
        while jewelry and jewelry[0][0] <= b:
            heappush(jtmp, -heappop(jewelry)[1])
        if jtmp:
            answer -= heappop(jtmp)

    print(answer)

sol()
```

> 처음에 heapq를 쓰고, 입력값도 for문으로 입력 받아서 그런가 뭔 2초넘게 나왔다(1초짜리 문제임). 그래서 다른 사람 답안들을 보고 변경했다.
>
> 생각해보니까 입력문을 저렇게 쉽게 받을 수 있는데 왜 굳이 저렇게 길고 보기 싫게 코드 짰는지 이해 못할 일..
>
> 



* 모범답안

  ```python
  1248
  from sys import stdin
  from heapq import heappush, heappop
  
  def sol():
      input = stdin.readline
  
      n, k = map(int, input().split())
  
      answer = 0
      jewelry = [tuple(map(int, input().split())) for _ in range(n)]
      jewelry.sort(key=lambda x: x[0], reverse=True)
      bag = [int(input()) for _ in range(k)]
      bag.sort()

      jtmp = []
      for b in bag:
          while jewelry and jewelry[-1][0] <= b:
              heappush(jtmp, -jewelry.pop()[1])
          if jtmp:
              answer -= heappop(jtmp)
  
      print(answer)
  
  sol()
  ```
  
  > 그리고 heapify로 jewelry를 정렬하기보다 sort를 사용하고 pop을 썼더니 더 빠르게 동작하였다 ㄷㄷ

