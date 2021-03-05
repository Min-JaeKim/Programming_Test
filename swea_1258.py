# python

## swea d4 1258 행렬 찾기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN



> 195ms



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
  t = int(input())
  for tc in range(1, t+1):
      n = int(input())
      arr = [list(map(int, input().split())) for _ in range(n)]
      visited = [[False] * n for _ in range(n)]
      result = []
      row, col = 0, 0
      while row < n:
          if arr[row][col] != 0 and not visited[row][col]:
              tmprow, tmpcol = 0, 0
              for i in range(row, len(arr)):
                  if arr[i][col] == 0:
                      break
                  tmprow += 1
                  for j in range(col, len(arr[i])):
                      if arr[i][j] == 0:
                          break
                      visited[i][j] = True
                      tmpcol += 1
              result.append([tmprow * (tmpcol//tmprow),tmprow, tmpcol//tmprow])
          col += 1
          if col == n:
              col = 0
              row += 1
      result = sorted(result)
      print('#%d %d' % (tc, len(result)), end = ' ')
      for i in range(len(result)):
          print(result[i][1], result[i][2], end = ' ')
      print()
  ```

  > 어떻게 해야 하나 당황스러웠던 문제. 사실상 방문표시만 해주면 금방 끝날 문젠데 오래 끌었다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

  

* 모범답안

  ```python
  150
  
  T = int(input())
   
  def scanner(y, x):
      xp = x
      while xp + 1 < N and board[y][xp + 1] > 0:
          xp += 1
       
      yp = y
      while yp + 1 < N and board[yp + 1][xp] > 0:
          yp += 1
   
      for my in range(y, yp + 1):
          board[my][x] = x - xp - 1
       
      return (yp - y + 1, xp - x + 1)
   
  for case_n in range(1, T + 1):
      N = int(input())
   
      board = []
      for _ in range(N):
          board.append(list(map(int, input().split())))
   
      y = 0
      x = 0
   
      answers = []
   
      while y < N:
          while x <= N:
              if x == N:
                  x = 0
                  break
              elif board[y][x] < 0:
                  #이미 방문체크한 경우
                  x -= board[y][x]
              elif board[y][x] > 0:
                  answers.append(scanner(y, x))
                  x += answers[-1][1]
              else:
                  x += 1
          y += 1
   
      answers.sort(key=lambda x: x[1])
      answers.sort(key=lambda x: x[0])
      answers.sort(key=lambda x: x[0] * x[1])
   
      answer_string = []
      for ast in answers:
          answer_string.append(' '.join(map(str, ast)))
   
      print('#{0} {1} {2}'.format(case_n, len(answers), ' '.join(answer_string)))
  ```

  > 여기도 방문체크 사용하셨지만 람다식을 쓰셨군 람다식이 뭐지?
  >
  > ```python
  > >>> def plus_ten(x):
  > ...     return x + 10
  > ```
  >
  > ```python
  > >>> lambda x: x + 10
  > ```
  >
  > * def -> lambda
  > * 매개변수 x -> x:
  > * return -> 제거
  >
  > 그리고 출력 부분이 너무 어려웠는데, 리스트를 하나 만들고 거기에 이중 리스트를 join하여 문제로 합친다음 마지막 출력역시 답을 모두 합친 리스트를 join하면 된다.

