# Python

## pro level3 합승 택시 요금

https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3



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





```python
def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    # for i in range(n):
    #     print(d[i])
    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
        # print(d[s-1][i], d[i][a-1], d[i][b-1])
    return minv
```

> 



- 틀린코드

  ```python
  from collections import deque
  
  def solution(n, s, a, b, fares):
      def union(i, j):
          i = find(p[i])
          j = find(p[j])
          if i > j:
              p[i] = j
          else:
              p[j] = i
      def find(k):
          if p[k] != k:
              p[k] = find(p[k])
          return p[k]
      fanswer, sflag, aflag, bflag = 0, 0, 0, 0
      sanswer, arr, dist = 0, [[] for _ in range(n+1)], [float('inf')] * (n+1)
      p = [i for i in range(n+1)]
      fares.sort(key = lambda x : x[2])
      for i, j, wt in fares:
          arr[i].append([j, wt])
          arr[j].append([i, wt])
      for i, j, wt in fares:
          if find(i) != find(j):
              union(i, j)
              if find(i) == find(s) or find(i) == find(a) or find(i) == find(b) or \
              find(j) == find(s) or find(j) == find(a) or find(j) == find(b):
                  fanswer += wt
              if find(s) == find(a) == find(b):
                  break
      # q = deque([[s, 0]])
      # while q:
      #     node, wt = q.popleft()
      #     if dist[node] < wt:
      #         continue
      #     for nnode, wwt in arr[node]:
      #         if wwt + wt < dist[nnode]:
      #             dist[nnode] = wwt + wt
      #             q.append([nnode, wwt+wt])
      # print(dist)
      # sanswer = dist[a] + dist[b]
      
      return fanswer
  ```

  



* 모범답안

  ```python
  
  ```
  
  > 반복문을 돌긴 해야하나봄

