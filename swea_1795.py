# python

## swea 1795 d6 인수의 생일파티

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4xuqCqBeUDFAUx

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
from heapq import heappush, heappop


for tc in range(1, int(input())+1):
    n, m, x = map(int, input().split())
    dsx = [0] + [float('inf')] * n
    dex = [0] + [float('inf')] * n
    start = [[] for _ in range(n+1)]
    end = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        start[a].append([b, c])
        end[b].append([a, c])

    def dijk(x, arr, dist):
        q = [[0, x]]
        while q:
            wt, node = heappop(q)
            if dist[node] < wt:
                continue
            for nnode, wwt in arr[node]:
                if wwt + wt < dist[nnode]:
                    dist[nnode] = wwt + wt
                    heappush(q, [wwt + wt, nnode])

    dijk(x, start, dsx)
    dijk(x, end, dex)
    dsx[x], dex[x], res = 0, 0, 0
    for i in range(1, n+1):
        if dsx[i] + dex[i] > res:
            res = dsx[i] + dex[i]
    print('#%d %d' % (tc, res))
```

> 미쳣다링,, 어떻게 이렇게 풀릴 수 있는 거임 ㅜ
>
> 모든 노드에서 정해진 도착지점으로 갈 때가 너무 어려웠다. 그 부분을 다익스트라로 해결하려 했는데 모든 노드를 for문을 통해서 다익스트라 쓰려고 하니까 엄청난 시간이 걸렸다. 심지어 답도 틀림..
>
> 그래서 접근방법이 아예 틀렸다 싶어서 포인트를 썼는데 써놓고서 내가 풀고 싶어서 미칠 뻔함 ㅋㅋ
>
> 암튼 이부분은 결국 강의를 보았다.
>
> `end[b].append([a, c])` 이렇게 해결하면 되는데, 어차피 도착지점 매개변수는 x로 넣을 것이라는 것을 망각하고 있었기에 이부분이 좀 이해가 안갔다. 다른지점에서 2로 가는 최소 거리를 계산하고, 그 지점을 다른 노드에서 가는 최솟값을 계산하고.. 이런식으로 완성하면 된다. 멋지다!
>
> 근데 인수야~ 다음부터는 생일 파티하지 말도록!



* 모범답안

  ```python
  
  ```
  
  > 