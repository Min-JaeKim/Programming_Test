# python

## swea d4 4613 러시아 국기 같은 깃발

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj



> 190ms



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
  
  import sys
  sys.stdin = open('./input.txt')
  
  t = int(input())
  for tc in range(1, t+1):
      r, c = map(int, input().split())
      arr = [list(input()) for _ in range(r)]
      result, whitecnt = r*c, 0
      for i in range(r-2):
          for j in range(c):
              if arr[i][j] != 'W':
                  whitecnt += 1
          bluecnt = 0
          for j in range(i+1, r-1):
              for l in range(c):
                  if arr[j][l] != 'B':
                      bluecnt += 1
  
              redcnt = 0
              for l in range(j+1, r):
                  for k in range(c):
                      if arr[l][k] != 'R':
                          redcnt +=1
  
              if result > whitecnt + bluecnt + redcnt:
                  result = whitecnt + bluecnt + redcnt
  
      print('#%d %d' % (tc,result))
  ```

  > 오웅 슅,, 첨에 어떻게 풀어야 하는지 감이 안왔다. 순열로 풀고 싶었는데 그렇게하면 경우의 수가 엄청나질 것 같고, 또한 시간도 엄청 나올 것 같아서 고민을 하였다. 하지만 결국에 한 줄 한 줄 계산해 줬다. 순열과 별반 다를 게 없는데 시간이 별로 나오지 않았다. 당황!
  >
  > 암튼 이 문제를 풀면서 제일 단순하게 풀 수 있는 방법이라고 생각한다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

  

* 모범답안

  ```python
  121
  
  T = int(input())
  for test_case in range(1, T + 1):
      N, M = map(int,input().split())
      board = [input() for _ in range(N)]
      new_board=[]
      for i in range(N):
          w = board[i].count('W')
          b = board[i].count('B')
          new_board.append([w,b,M-(w+b)])
      for i in range(1,N):
          new_board[i][0] += new_board[i-1][0]
          new_board[i][1] += new_board[i-1][1]
          new_board[i][2] += new_board[i-1][2]
       
      res = 0
      for x in range(N-2):
          for y in range(x+1,N-1):
              white = new_board[x][0]
              blue = new_board[y][1] - new_board[x][1]
              red = new_board[N-1][2] - new_board[y][2]
              total = white+blue+red
              if res < total:
                  res = total
      print(f'#{test_case} {N*M-res}')
  ```

  > 엄청 빠른 멋진 코드인데 중요한 것은 이해가 안된다는 것이다...
  >
  > 보고 좀 배우려고 했는데 도무지 이해가 안되어서 배울 수가 없었다.
  >
  > 마지막 이중 포문에서 이해가 안갔다. 위의 줄마다 칠해진 W B R를 계산하는 곳까지는 이해가 갔다. 이후 진행하던 줄에서 위의 같은 색의 개수를 빼는 게 이해가 안갔다. 예를들어 현재 마지막 줄까지 빨간색이 10개 칠해져있다면, 위에서 두 번째의 빨간색이 칠해진 개수를 뺀다. 그렇게 한 줄 한 줄 진행해 나가는데 이해가 안된다...

