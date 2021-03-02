# python

## swea d3 1217 거듭 제곱

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD



> 



* 문제

  > 

* 입력

  > 
  >
  > ```bash
  > 
  > ```

* 출력

  > 
  >
  > ```bash
  > 
  > ```



* 제출

  ```python
  #재귀
  from datetime import datetime
  
  def power(n, cnt):
      global m
      if cnt == m:
          return n
      return power(n, cnt+1) * n
  for _ in range(1, 11):
      tc = int(input())
      n, m = map(int, input().split())
      start = datetime.now()
      print('#%d %d' % (tc, power(n, 1)))
      print(datetime.now() - start)
      
      
  #메모이제이션
  from datetime import datetime
  
  def power(n, cnt):
      if cnt in memo:
          return memo[cnt]
      memo[cnt] = power(n, cnt -1) * n
      return memo[cnt]
  for _ in range(1, 11):
      tc = int(input())
      n, m = map(int, input().split())
      start = datetime.now()
      memo = {0 : 1, 1: n}
      print('#%d %d' % (tc, power(n, m)))
      print(datetime.now() - start)
  ```

  > 메모이제이션  어렵다
  >
  > 

  

* 모범답안

  ```python
  
  ```

  > 

