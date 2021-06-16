# python

## baek 1463 1로 만들기 실버3

https://www.acmicpc.net/problem/1463

> python3 96ms
>



* 문제

  > 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
  >
  > 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
  >2. X가 2로 나누어 떨어지면, 2로 나눈다.
  > 3. 1을 뺀다.
  >
  > 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
  
* 입력

  > 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
  >
  > ```bash
  > 10
  > ```
  >
  
* 출력

  > 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
  >
  > ```bash
  > 3
  > ```



```python
from collections import deque


def sol():
    n = int(input())
    dic = {}
    dic[n] = 0
    q = deque([[n, 0]])
    while q:
        num, cnt = q.popleft()
        if num < 1:
            continue
        if num == 1:
            print(cnt)
            exit()
        if num % 3 == 0:
            if num//3 not in dic or cnt+1 < dic[num//3]:
                q.append([num//3, cnt+1])
                dic[num//3] = cnt+1
        if num % 2 == 0:
            if num//2 not in dic or cnt+1 < dic[num//2]:
                q.append([num//2, cnt+1])
                dic[num//2] = cnt+1
        if num-1 not in dic or cnt+1 < dic[num-1]:
            q.append([num-1, cnt+1])
            dic[num-1] = cnt+1


sol()
```

> 정신 똑바로 차리지 않고 풀었다.. num을 n으로 써놔서 오래걸림 ㅡㅡ



* 모범답안

  ```python
  def dp(n):
      if n in memo:
          return memo[n]
      # 나머지를 더해준 이유 짐작: 7의 경우 2, 3으로 나누어 지지 않으므로 -1를 무조건 해줘야한다.
      # 이 경우를 나머지로 더해주는 것으로 짐작된다.
      m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
      memo[n] = m
      return m
  
  
  memo = {1: 0, 2: 1}
  n = int(input())
  print(dp(n))
  ```

  > 어떻게 이런 생각하는지 나는 못따라가겠음 ㅠㅠ

