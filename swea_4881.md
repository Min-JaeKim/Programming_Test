# python

## swea d2 4881 배열 최소 합

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do



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
  def bfs(row, tmpsum):
      global result 
      if tmpsum > result: # 진행하고 있던 임시 값이 결과값보다 크다면
          return # 다른 거 진행
      if row == n: # 모든 행을 다 돌았다면
          if tmpsum < result: # 게다가 결과값을 갱신할 수 있다면
              result = tmpsum
          return # 갱신하고 return
  
      for i in range(n): # 열 반복문
          if visited[i] == False: # 방문이 되지 않은 열이라면
              visited[i] = True # 방문해주고
              bfs(row + 1, tmpsum + arr[row][i]) # 그 다음 행과 임시값을 넣고 bfs 재귀를 돌림
              visited[i] = False # 계산 끝난 열은 다음 연산을 위해 방문표시는 false로 되돌려줌
  
  t = int(input())
  for tc in range(1, t+1):
      n = int(input())
      arr = [list(map(int, input().split())) for _ in range(n)]
      visited, result = [False for _ in range(n)], n * 10 # 열 방문 표시, 결과는 최댓값으로
      bfs(0, 0) # 0행부터 시작하고, 임시 결과값도 0
      print('#%d %d' % (tc, result))
  ```

  > 재귀 진짜 어려워 잘 모르겠다 재귀는,,
  >
  > 시간 초과가 났었는데 중간에 임시 결과값이 저장된 결과값보다 커지면 빠져나오는 것을 잊지 말았어야 했다.
  >
  > 

  

* 모범답안

  ```python
  def MyCalc(y):
      global sub_result, result
  
      if result < sub_result:
          return
  
      if y == N:
          if sub_result < result:
              result = sub_result
          return
  
      for x in range(N):
          if not visited[x]:
              visited[x] = True
              sub_result += lst[y][x]
              MyCalc(y+1)
              visited[x] = False
              sub_result -= lst[y][x]
  
  
  TC = int(input())
  for tc in range(1, TC+1):
      N = int(input())
      lst = [list(map(int, input().split())) for _ in range(N)]
      visited = [0] * N
      sub_result, result = 0, 987654321
      MyCalc(0)
  
      print(f'#{tc} {result}')
  ```

  > 

