# python

## baek 2110 공유기 설치 실버1

https://www.acmicpc.net/problem/2110

> python3 380ms

* 문제

  > 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
  >
  > 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
  >
  > C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
  >
  > ```bash
  > 5 3
  > 1
  > 2
  > 8
  > 4
  > 9
  > ```
  >
  
* 출력

  > 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
  >
  > ```bash
  > 3
  > ```



- 틀린 코드

```python
import sys
input = sys.stdin.readline


def sol():
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    start, end, res = 1, arr[-1] - arr[0] + 1, 0

    while start < end:
        mid = (start + end) // 2
        cur_house, count = arr[0], 1

        for i in range(1, n):
            if mid <= arr[i] - cur_house:
                count += 1
                cur_house = arr[i]

        print(mid, count)
        if count < c:
            end = mid
        else:
            if count == c and res < mid:
                res = mid
            start = mid + 1

    print(res)

sol()
```

> ```python
> if count == c and res < mid:
>     res = mid
> ```
>
> 이부분 때문이었는데 반례는 다음과 같다
>
> ```bash
> 4 3
> 1
> 3
> 5
> 7
> ```
>
> 저 좌표 중에 3개만 골라서 공유기를 설치해도 되므로 count가 꼭 c와 같을 필요는 없다. 게다가 res < mid 조건도 필요 없다. 왜냐하면 결론적으로는 최적의 결과가 res에 들어가기 때문. 하 이분탐색 아직도 어렵다. 이분탐색 하면 비트마스킹 연습해야지.



- 두번째 풀이

```python
import sys
input = sys.stdin.readline


def sol():
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    start, end, res = 1, arr[-1] - arr[0] + 1, 0

    while start < end:
        mid = (start + end) // 2
        cur_house, count = arr[0], 1

        for i in range(1, n):
            if mid <= arr[i] - cur_house:
                count += 1
                cur_house = arr[i]

        if count < c:
            end = mid
        else:
            res = mid
            start = mid + 1

    print(res)

sol()
```

> end에 꼭 1을 더한 다음 while문을 돌려야 함을 잊지 말아야 한다.



* 모범답안

  ```python
  174
  
  import sys
  input = sys.stdin.readline
  
  def BOJ_2210():
      N, C = map(int,input().split())
  
      house = [int(input()) for _ in range(N)]
      house.sort()
  
      low, high = 1, (house[-1] - house[0])//(C-1) + 1
      print(high)
  
      while low+1 < high:
          mid = (low + high) // 2
          t, cnt = house[0]+mid, 1
          for h in house:
              if h >= t:
                  t = h + mid
                  cnt += 1
              if cnt == C:
                  break
          if cnt >= C:
              low = mid
          elif cnt < C:
              high = mid
      print(low)
  BOJ_2210()
  ```

  > ```python
  > low, high = 1, (house[-1] - house[0])//(C-1) + 1
  > ```
  >
  > high가 무슨 의미일까.. 왜 최대 길이에서 공유기-1 을 나눈다음 1을 아하 알겠다. 
  >
  > 공유기에서 1을 빼는 이유는 시작점에서 이미 공유기를 하나 설치하기 때문이다.
  >
  > 그리고 마지막에 1을 더하는 이유는 내가 이분탐색 구현할 때 최댓값에 1을 더하는 것과 같은 이유이다.

