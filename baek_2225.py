# python

## baek 2225 합 분해 골드5

https://www.acmicpc.net/problem/2225

> python3 72ms



* 문제

  > 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
  >
  > 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.
  
* 입력

  > 첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.
  >
  > ```bash
  > 20 2
  > ```
  >
  
* 출력

  > 첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.
  >
  > ```bash
  > 21
  > ```



```python
def sol():
    n, k = map(int, input().split())
    arr = [[0] * (n+1) for _ in range(k+1)]

    for i in range(n+1):
        arr[1][i] = 1

    for i in range(k+1):
        arr[i][1] = i
        arr[i][0] = 1

    for i in range(1, k+1):
        for j in range(1, n+1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    print(arr[k][n] % 1000000000)


sol()
```

> 난 수학 문제에 약하다 흑흑,,, 수학 + dp는 정말 나의 최약체,,
>
> 규칙성을 찾으면 된다.
>
> 1부터 차근차근 보면됨



* 모범답안

  ```python
  56
  
  def fac(n):
      sum =1
      for _ in range(1, n+1):
          sum *= _
      return sum
  
  n, r = map(int, input().split())
  print(fac(n+r-1)//(fac(r-1)*fac(n))%1000000000)
  ```
  
  > 미쳤당,,

