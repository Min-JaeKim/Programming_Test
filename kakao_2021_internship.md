# kakao 2021 internship

- 01

  ```python
  def solution(s):
      answer = ''
      dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
      tmp = ''
      for i in s:
          if i.isdigit():
              answer += i
          else:
              tmp += i
              if tmp in dic:
                  answer +=  str(dic[tmp])
                  tmp = ''
      answer = int(answer)
      return answer
  
  print(solution('one4seveneight'))
  
  ```

- 02

  ```python
  dr = (-1, 1, 0, 0)
  dc = (0, 0, -1, 1)
  
  
  def solution(places):
      answer = []
      for i in range(len(places)):
          arr = [[] for _ in range(5)]
          for j in range(len(places[i])):
              for k in range(len(places[i][j])):
                  arr[j].append(places[i][j][k])
          for j in range(len(arr)):
              for k in range(len(arr[j])):
                  realflag = 1
                  if arr[j][k] == 'P':
                      for dir in range(4):
                          nr, nc, cnt, xflag = j, k, 0, 0
                          while cnt < 2:
                              if not cnt:
                                  nr, nc = nr + dr[dir], nc + dc[dir]
                                  if 0 <= nr < 5 and 0 <= nc < 5:
                                      if arr[nr][nc] == 'X':
                                          xflag = 1
                                          break
                                      if arr[nr][nc] == 'P':
                                          realflag = 0
                                          answer.append(realflag)
                                          break
                                  else:
                                      break
                              else:
                                  for dir2 in range(4):
                                      if nr + dr[dir2] != j or nc + dc[dir2] != k:
                                          if 0 <= nr + dr[dir2] < 5 and 0 <= nc + dc[dir2] < 5:
                                              if arr[nr + dr[dir2]][nc + dc[dir2]] == 'P':
                                                  realflag = 0
                                                  answer.append(realflag)
                                                  break
                              cnt += 1
                          if xflag:
                              continue
                          if not realflag:
                              break
                  if not realflag:
                      break
              if not realflag:
                  break
          if realflag:
              answer.append(realflag)
  
      return answer
  
  
  print(solution([["POPOO", "OXXXX", "OXXXX", "XOXOO", "PXPXP"]]))
  ```

- 03

  ```python
  def solution(n, k, cmd):
      answer = ''
      arr = [i for i in range(n)]
      delete = []
      iidx = arr[k]
      for i in range(len(cmd)):
          if len(cmd[i]) > 2:
              order, idx = cmd[i].split()
              idx = int(idx)
          else:
              order = cmd[i]
          if order == 'D':
              iidx += idx
          elif order == 'C':
              delete.append([iidx, arr[iidx]])
              del arr[iidx]
              if iidx == len(arr):
                  iidx = len(arr)-1
          elif order == 'U':
              iidx -= idx
          elif order == 'Z':
              tmpidx, num = delete.pop()
              if tmpidx <= iidx:
                  iidx += 1
              arr.insert(tmpidx, num)
      ox, idx = 0, 0
      while idx < len(arr):
          if arr[idx] != ox:
              answer += 'X'
          else:
              answer += 'O'
              idx += 1
          ox += 1
      if len(answer) < n:
          answer = answer +'X'*(n-len(answer))
      return answer
  
  
  print(solution(3, 2, ["C"]))
  ```

- 04

  ```python
  from collections import deque
  
  def solution(n, start, end, roads, traps):
      arr = [[float('inf')] * (n+1) for _ in range(n+1)]
      for s, e, wt in roads:
          arr[s][e] = wt
      if arr[start][end] < 3001:
          return arr[start][end]
      q = deque([[0, start]])
      while q:
          wt, node = q.popleft()
          if arr[start][node] < wt:
              continue
          if node in traps:
              for i in range(len(arr)):
                  for j in range(len(arr[i])):
                      if i < j:
                          arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
          for nnode in range(n+1):
              if wt + arr[node][nnode] < arr[start][nnode] or arr[node][nnode] < 3001:
                  if wt + arr[node][nnode] < arr[start][nnode]:
                      arr[start][nnode] = wt + arr[node][nnode]
                  q.append([wt+arr[node][nnode], nnode])
      return arr[start][end]
  
  
  print(solution(4, 1, 4, [[1, 2, 2], [3, 2, 3], [1, 4, 2]], [2]))
  ```

  