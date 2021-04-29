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
    answer = float('inf')
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i, j, wt in fares:
        dist[i-1][j-1] = wt
        dist[j-1][i-1] = wt
    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if dist[i][k] > dist[i][j] + dist[j][k]:
    #                 dist[i][k] = dist[i][j] + dist[j][k]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]

    for i in range(n):
        answer = min(answer, dist[s-1][i] + dist[i][a-1] + dist[i][b-1])
    return answer
```

> 이게 어렵다기 보다 헷갈렸던 거는 `경출도` 때문이었다. 순서를 다르게 해도 괜찮지 않을까라는 생각에 출경도로 했다가 틀려버렸다. 이유는 뭔지 모르겠는데 ㅠㅠ 그냥 경출도 순서로 포문을 이해하는 게 낫겠다.
>
> 그리고 마지막 거리는 출발에서 셋의 중앙 정점, 셋의 중앙정점에서 a와 b



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
  from collections import defaultdict
  import heapq
  
  def solution(n, s, a, b, fares):
      dic = defaultdict(list)
      for st, ed, co in fares:
          dic[st].append((co, ed))
          dic[ed].append((co, st))
      ans = []
      for i in range(1, n+1):
          Q = [(0, i)]
          visited = [True] * (n+1)
          dp = [float('inf')] * (n+1)
          dp[i] = 0
          while Q:
              co, des = heapq.heappop(Q)
              if visited[des]:
                  visited[des] = False
                  for cost, destination in dic[des]:
                      dp[destination] = min(cost + dp[des], dp[destination])
                      heapq.heappush(Q, (dp[destination], destination))
          ans.append(dp[a] + dp[b] + dp[s])
      print(ans)
  
      return min(ans)
  ```
  
  > 세 점의 중점 중 가장 거리가 짧은 중점을 찾아야 한다.. 다익스트라로 푸는 건 알고 있었지만,, 왜이렇게 어려운건데 ,, ㅠ

