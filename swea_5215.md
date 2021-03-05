# python

## swea d3 5215 햄버거 다이어트

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT



> 2475ms



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
  from itertools import combinations
  
  t = int(input())
  for tc in range(1, t+1):
      n, l = map(int, input().split())
      arr, result = [], 0
      for _ in range(n):
          t, k = map(int, input().split())
          arr.append([t, k])
  
      for i in range(n):
          for j in combinations(arr, i+1):
              tmpcal, tmptst = 0, 0
              for t, k in j:
                  tmpcal += k
                  tmptst += t
              if tmpcal <= l:
                  if tmptst > result:
                      result = tmptst
      print('#%d %d' % (tc, result))
  ```

  > 콤비네이션,, 풀이도 짧고 쉽게 풀 수 있지만, 시간적으로 따져봤을 때 엄청 비효율적이다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

  

* 모범답안

  ```python
  137
  
  def select(idx, point, cal):
      global result
   
      if idx == N:
          if result < point:
              result = point
          return
   
      if sum(points[idx:]) + point < result:
          return
   
      if cal + cals[idx] < L:
          select(idx+1, point+points[idx], cal+cals[idx])
      select(idx+1, point, cal)
   
   
  T = int(input())
   
  for tc in range(1, T+1):
      N, L = map(int, input().split())
   
      points = []
      cals = []
   
      for i in range(N):
          point, cal = map(int, input().split())
          points.append(point)
          cals.append(cal)
   
      result = 0
   
      select(0, 0, 0)
   
      print('#{} {}'.format(tc, result))
  ```

  > z칼로리와 맛을 다른 리스트에 담아 준 다음에 재귀를 써서 푸셨다.
  >
  > 시간적으로 엄청 효율적이군.

