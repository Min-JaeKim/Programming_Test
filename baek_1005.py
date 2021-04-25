# python

## baek 1005 ACM Craft 골드3

https://www.acmicpc.net/problem/1005

> python3 900ms
>
> pypy3 472ms



* 문제

  > 서기 2012년! 드디어 2년간 수많은 국민들을 기다리게 한 게임 ACM Craft (Association of Construction Manager Craft)가 발매되었다.
  >
  > 이 게임은 지금까지 나온 게임들과는 다르게 ACM크래프트는 다이나믹한 게임 진행을 위해 건물을 짓는 순서가 정해져 있지 않다. 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다. 매 게임시작 시 건물을 짓는 순서가 주어진다. 또한 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.
  >
  >  
  >
  > ![img](md-images/star.JPG)
  >
  > 위의 예시를 보자.
  >
  > 이번 게임에서는 다음과 같이 건설 순서 규칙이 주어졌다. 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. (동시에 진행이 가능하다) 그리고 4번 건물을 짓기 위해서는 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다.
  >
  > 따라서 4번건물의 건설을 완료하기 위해서는 우선 처음 1번 건물을 건설하는데 10초가 소요된다. 그리고 2번 건물과 3번 건물을 동시에 건설하기 시작하면 2번은 1초뒤에 건설이 완료되지만 아직 3번 건물이 완료되지 않았으므로 4번 건물을 건설할 수 없다. 3번 건물이 완성되고 나면 그때 4번 건물을 지을수 있으므로 4번 건물이 완성되기까지는 총 120초가 소요된다.
  >
  > 프로게이머 최백준은 애인과의 데이트 비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다! 최백준은 화려한 컨트롤 실력을 가지고 있기 때문에 모든 경기에서 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다. 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은 좌절하고 있었다. 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.

* 입력

  > 첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다) 
  >
  > 둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다. 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 
  >
  > 마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.
  >
  > ```python
  > 2
  > 4 4
  > 10 1 100 10
  > 1 2
  > 1 3
  > 2 4
  > 3 4
  > 4
  > 8 8
  > 10 20 1 5 8 7 1 43
  > 1 2
  > 1 3
  > 2 4
  > 2 5
  > 3 6
  > 5 7
  > 6 7
  > 7 8
  > 7
  > ```
  >
  > 

* 출력

  > 건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.
  >
  > 건설순서는 모든 건물이 건설 가능하도록 주어진다.
  >
  > ```python
  > 120
  > 39
  > ```



```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

'''
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
'''

def sol():
    
    def dfs(w):
        maxtime = 0
        for i in progress[w]:
            # 현재 건설완료되어야 하는 건물 중
            if dp[i] == -1:
                # 아직 시간이 정해지지 않은 건물이 있다면
                dfs(i)
                # dfs에 넣고
                maxtime = max(maxtime, dp[i])
                # maxtime으로 계산
            else:
                # 시간이 정해져 있다면
                maxtime = max(maxtime, dp[i])
                # maxtime으로 최대 시간 뽑아냄
        dp[w] = maxtime + time[w]
        # 이전 건물의 최대시간 + 현재 건물 시공 시간

    for tc in range(int(input())):
        n, k = map(int, input().split())
        time = [0] + list(map(int, input().split()))
        # 각 건물 당 소요 시간
        progress = [[] for _ in range(n+1)]
        # 현재 건물을 짓기 위해 꼭 지어야 하는 건물 리스트
        # 예를 들어 위의 입력이라면
        # [[], [], [1], [1], [2,3]]
        dp = [-1] * (n+1)
        # 0초도 분명 존재할 것이기에 -1로 초기화
        for _ in range(k):
            a, b = map(int, input().split())
            progress[b].append(a)
        w = int(input())
        dfs(w)
        print(dp[w])


sol()
```

> 아놔.. 다익스트라로 풀어서 틀렸다. ㅠ 밑에는 다익스트라 풀이.
>
> 결국 다른 사람 풀이를 보았다. 완조니 정통 다이나믹 프로그래밍이다. 나도 분명 풀 때 이상각을 하긴 했는데 처음에 안돌아가길래 의아했다. 지금 생각해보면 당연히 재귀로 구현했어야 할 문제인데 그렇지 않아서 문제가 된 것 같기도 하다.
>
> 그리고 의외로 n이 1000개라 생각해서
>
> `sys.setrecursionlimit(10**6)`
>
> 이걸 염두하지 않았는데 런타임에러 떴다.. 꼭 해줘야 하는듯. 그리고 심지어 pypy는 메모리초과나서 괄호 부분을 10000으로 바꿔줘야 함.

- 틀린 풀이

```python
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def sol():
    for tc in range(int(input())):
        n, k = map(int, input().split())
        arr = [0] + list(map(int, input().split()))
        start = [[] for _ in range(n+1)]
        dist = [0] + [0] * n
        for _ in range(k):
            a, b = map(int, input().split())
            start[b].append([a, arr[a]])
        w = int(input())
        q = [[arr[w], w]]
        res = arr[w]
        while q:
            wt, node = heappop(q)
            wt = abs(wt)
            if wt < dist[node]:
                continue
            for i in start[node]:
                if wt + i[1] > dist[i[0]]:
                    dist[i[0]] = wt + i[1]
                    res = max(res, dist[i[0]])
                    heappush(q, [-(wt + i[1]), i[0]])
        print(res)


sol()
```

> 꽤 깔끔하게 풀었다고 생각했는데 시간초과 났다.
>
> - heappush(q, [-(wt + i[1]), i[0]]) : 최대힙 저장방법



* 모범답안

  ```python
  import sys
  input = sys.stdin.readline
  sys.setrecursionlimit(10**6)
  
  
  def solve():
      def dfs(u):
          if dp[u] != -1:
              return dp[u]
          m=max([dp[v] if dp[v]!=-1 else dfs(v) for v in adj[u]],default=0)
          dp[u]=m+t[u]
          return dp[u]
  
      n, k = map(int, input().split())
      adj = [[] for _ in range(n+1)]
      dp = [-1 for _ in range(n+1)]
      t = [0]+list(map(int, input().split()))
      for _ in range(k):
          x, y = map(int, input().split())
          adj[y].append(x)
      print(adj)
      w = int(input())
      print(dfs(w))
  
  
  solve()
  ```

  > 

