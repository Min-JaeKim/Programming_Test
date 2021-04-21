# python

## swea 2814 d3 최장 경로

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB



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
def dfs(node, move):
    global res
    if move > res:
        res = move
    v[node] = 1
    for i in range(len(arr[node])):
        if not v[arr[node][i]]:
            dfs(arr[node][i], move+1)
    v[node] = 0


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    res = 0
    v = [0 for _ in range(n+1)]
    for j in range(1, n+1):
        dfs(j, 1)

    print('#%d %d' % (tc, res))
    
    
    
    
'''
반례
1
6 10
1 3
3 2
2 4
5 5
4 2
1 6
6 2
4 3
2 5
5 1
6
'''    
def dfs(node, move):
    global res
    res = max(move, res)
    for i in range(len(arr[node])):
        if not v[arr[node][i]]:
            v[arr[node][i]] = 1
            dfs(arr[node][i], move + 1)


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    res = 0
    for j in range(1, n + 1):
        v = [0 for _ in range(n + 1)]
        v[j] = 1
        dfs(j, 1)

    print('#%d %d' % (tc, res))
```

> 처음에 bfs로 풀었다... 왜냐면 그냥 재귀가 싫었기 때문이다. 싫었다기 보다 그냥 시간을 무지막지하게 써버리는 게 싫어서 재귀를 안한 건데 생각해보니 최장경로의 문제였다. 최단 거리였으면 bfs를 썼겠지만 끝까지 파고 들어가는 게 중요한 문제였다.
>
> 그래서 두번째 코드처럼 방문 표시를 한 다음 다녀온 다음에 다시 false로 바꾸지 않는 코드로 짰다. 그러면 fail을 한다. 그 이유는 이미 방문했던 곳을 나중에 방문하면 더 긴 거리를 갈 수 있는 경우가 있기 때문이다. 반례는 적어 놓았다.



* 모범답안

  ```python
  def dfs(n, count):
      global result
      if count > result:
          result = count
   
      visited[n] = True
      for i in range(1, N+1):
          if adj[n][i] and not visited[i]:
              dfs(i, count+1)
      visited[n] = False
   
   
  for tc in range(1, int(input())+1):
      N, M = map(int, input().split())
      adj = [[False]*(N+1) for _ in range(N+1)]
      visited = [False]*(N+1)
      for _ in range(M):
          x, y = map(int, input().split())
          adj[x][y], adj[y][x] = True, True
      result = 0
      for n in range(1, N+1):
          dfs(n, 1)
      print(f'#{tc} {result}')
  ```
  
  > 특별한 건 접점 노드끼리 1로 표시했다는 것.
  >
  > append를 쓰지 않고 =연산자를 사용해서 그런지 시간이 살짝 빠르다.