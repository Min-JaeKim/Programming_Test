# python

## baek 1644 소수의 연속합 골드3

https://www.acmicpc.net/problem/1644

> python3 1176ms

* 문제

  > 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
  >
  > - 3 : 3 (한 가지)
  > - 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
  > - 53 : 5+7+11+13+17 = 53 (두 가지)
  >
  > 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
  >
  > 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)
  >
  > ```bash
  >41
  > ```
  >
  
* 출력

  > 첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
  >
  > ```bash
  >3
  > ```



```python
def sol():

    n = int(input())

    if n == 1:
        print(0)
        exit()

    tmplist = [True for _ in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if tmplist[i]:
            for j in range(i+i, n+1, i):
                tmplist[j] = False
    arrlist = [i for i in range(2, n+1) if tmplist[i]]

    # print(arrlist)

    res = 0

    left, right = 0, 1
    sum = arrlist[left]
    length = len(arrlist)

    while right < length+1:
        while sum > n:
            sum -= arrlist[left]
            left += 1
        if sum == n:
            res += 1
        if right < length:
            sum += arrlist[right]
        right += 1

    print(res)


sol()
```

> 하 진짜 별문제 아닌데 ㅜ 소수 구하는 게 너무 힘들었다. 크기가 4000000인데 누가 이중 포문 썼길래 나도 당당히 썼는데 ㅋㅋㅋ 그렇게 푸는 게 아니었다. 하나 하나 일일이 소수인지 찾아줬는데 그렇게 푸는게 아니라 일단 현재 수까지 모든 수를 boolean으로 표현하고 true일 때만 그 수의 2배부터 그 수만큼 계속 더해가며 for문을 돌리며 (그니까 그 수의 배수) false로 바꿔줌.
>
> 그리고 투포인터로 값을 구해나갔다. 어떻게 푸는 지는 하나도 모르겠고, 결국 알고리즘 분류 보고서 아이디어를 얻어 풀었다. 하 소수 구하ㅡ는 아이디어 너무 좋다 더 발전해야지 ㅠㅠ



* 모범답안

  ```python
  448
  
  from math import sqrt
  
  
  def solve(n):
      def primes(n):
          mask = [True] * (n + 1)
          for i in range(2, int(sqrt(n)) + 1):
              if not mask[i]:
                  continue
              mask[i::i] = [False] * ((len(mask) - 1) // i)
              mask[i] = True
          mask[0] = False
          mask[1] = False
          return [p for p in range(n + 1) if mask[p]]
  
      ps = primes(n)
      start = 0
      stop = 0
      acc = 0
      count = 0
      for stop in range(len(ps)):
          acc += ps[stop]
          if acc == n:
              count += 1
          while acc >= n and start <= stop:
              acc -= ps[start]
              if acc == n:
                  count += 1
              start += 1
      return count
  
  
  n = int(input())
  print(solve(n))
  ```

  > 뭐지 비트마스크같은 거 써서 그런가 시간 엄청 빠르네

