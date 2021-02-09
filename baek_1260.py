# Python

## baek 1260 DFS와 BFS

https://www.acmicpc.net/problem/1260



> 244ms



* 문제

  > 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

* 입력

  > 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
  >
  > ```bash
  > 4 5 1
  > 1 2
  > 1 3
  > 1 4
  > 2 4
  > 3 4
  > ```

* 출력

  > 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
  >
  > ```bash
  > 1 2 4 3
  > 1 2 3 4
  > ```



```python
from collections import deque
import sys

sys.stdin = open('./input.txt', encoding='utf8')

def dfs(v): # DFS 시작
    visit[v] = 1 # 시작지점 방문 표시 1
    print(v, end = ' ') # 그리고 출력
    for i in range(1,n+1): # FOR문으로 인접해 있나 확인
        if visit[i] == 0 and arr[v][i] == 1: # 방문하지도 않고 인접해있다면
            dfs(i) # 재귀로 DFS 돌려줌

def bfs(v): # BFS 시작
    que = deque([]) # QUEUE를 사용한다
    que.append(v) # 첫 시작을 QUE에 넣어줌
    visit[v] = 0 # 그리고 방문표시는 0로 표시, DFS와 차별점을 둠
    while que: # QUE에 인자가 있다면
        tmp = que.popleft() # 임시 변수에 QUE를 넣어주고
        print(tmp, end = ' ') # 방금 POP한 것을 출력
        for i in range(1,n+1): # 인접해있는지 확인
            if visit[i] == 1 and arr[tmp][i] == 1: # 방문도 하지 않았고, 인접해 있다면
                que.append(i) #QUE에 넣어주고
                visit[i] = 0 # 방문표시

n,m,v = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

dfs(v)
print()
bfs(v)
```

> 말이 안되는 게 예전에 C++로 풀었을 때는 12MS걸렸다.. ㄷㄷ



* 모범답안

  ```python
  
  ```

  > 