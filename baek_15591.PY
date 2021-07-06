# python

## baek 15591 MooTube(Silver) 골드5

https://www.acmicpc.net/problem/15591

> python3 5416ms
>



* 문제

  > 농부 존은 남는 시간에 MooTube라 불리는 동영상 공유 서비스를 만들었다. MooTube에서 농부 존의 소들은 재밌는 동영상들을 서로 공유할 수 있다. 소들은 MooTube에 1부터 N까지 번호가 붙여진 N (1 ≤ N ≤ 5,000)개의 동영상을 이미 올려 놓았다. 하지만, 존은 아직 어떻게 하면 소들이 그들이 좋아할 만한 새 동영상을 찾을 수 있을지 괜찮은 방법을 떠올리지 못했다.
  >
  > 농부 존은 모든 MooTube 동영상에 대해 “연관 동영상” 리스트를 만들기로 했다. 이렇게 하면 소들은 지금 보고 있는 동영상과 연관성이 높은 동영상을 추천 받을 수 있을 것이다.
  >
  > 존은 두 동영상이 서로 얼마나 가까운 지를 측정하는 단위인 “USADO”를 만들었다. 존은 N-1개의 동영상 쌍을 골라서 직접 두 쌍의 USADO를 계산했다. 그 다음에 존은 이 동영상들을 네트워크 구조로 바꿔서, 각 동영상을 정점으로 나타내기로 했다. 또 존은 동영상들의 연결 구조를 서로 연결되어 있는 N-1개의 동영상 쌍으로 나타내었다. 좀 더 쉽게 말해서, 존은 N-1개의 동영상 쌍을 골라서 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재하도록 했다. 존은 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 하기로 했다.
  >
  > 존은 어떤 주어진 MooTube 동영상에 대해, 값 K를 정해서 그 동영상과 USADO가 K 이상인 모든 동영상이 추천되도록 할 것이다. 하지만 존은 너무 많은 동영상이 추천되면 소들이 일하는 것이 방해될까 봐 걱정하고 있다! 그래서 그는 K를 적절한 값으로 결정하려고 한다. 농부 존은 어떤 K 값에 대한 추천 동영상의 개수를 묻는 질문 여러 개에 당신이 대답해주기를 바란다.

* 입력

  > 입력의 첫 번째 줄에는 N과 Q가 주어진다. (1 ≤ Q ≤ 5,000)
  >
  > 다음 N-1개의 줄에는 농부 존이 직접 잰 두 동영상 쌍의 USADO가 한 줄에 하나씩 주어진다. 각 줄은 세 정수 pi, qi, ri (1 ≤ pi, qi ≤ N, 1 ≤ ri ≤ 1,000,000,000)를 포함하는데, 이는 동영상 pi와 qi가 USADO ri로 서로 연결되어 있음을 뜻한다.
  >
  > 다음 Q개의 줄에는 농부 존의 Q개의 질문이 주어진다. 각 줄은 두 정수 ki와 vi(1 ≤ ki ≤ 1,000,000,000, 1 ≤ vi ≤ N)을 포함하는데, 이는 존의 i번째 질문이 만약 K = ki라면 동영상 vi를 보고 있는 소들에게 몇 개의 동영상이 추천될 지 묻는 것이라는 것을 뜻한다.
  >
  > ```bash
  > 4 3
  > 1 2 3
  > 2 3 2
  > 2 4 4
  > 1 2
  > 4 1
  > 3 1
  > ```
  >
  
* 출력

  > Q개의 줄을 출력한다. i번째 줄에는 농부 존의 i번째 질문에 대한 답변이 출력되어야 한다.
  >
  > ```bash
  > 3
  > 0
  > 2
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    N, Q = map(int, input().split())
    arr = [[] for _ in range(N+1)]

    for _ in range(N-1):
        p, q, r = map(int, input().split())
        arr[p].append([q, r])
        arr[q].append([p, r])

    def estim(i, a):
        v = [0] * (N+1)
        v[i], q, cnt = 1, deque([i]), 0

        while q:
            node = q.popleft()
            for node2, wt2 in arr[node]:
                if not v[node2] and a <= wt2:
                    cnt += 1
                    q.append(node2)
                    v[node2] = 1

        return cnt

    for _ in range(Q):
        a, b = map(int, input().split())
        print(estim(b, a))

sol()
```

> 하,,, 되게 다양한 방법을 쓴 것 같다. 처음에는 모든 노드에서 모든 노드까지 유사도를 계산해줬다. 그런데 시간초과가 났고 방법이 틀렸음을 깨달았다. 이후, 힙으로 구해야 하는 노드에서부터 모든 노드까지만 계산해줬다. 하지만 이것도 시간초과. 결국에 답을 봤다. 풀이를 말해보자면 일단은 모든 노드가 현재 연결되어 있는 상태이다. 그래서 값을 갱신해 준다거나 그럴 필요 없이, 기록되어 있는 값만으로도 답을 구할 수 있다. 현재 가중치가 구해야 하는 가중치보다 크다면 그 노드만 다시 Q에 넣고 BFS를 쓰면 된다. 한 번작은 노드를 만날 때에는 어차피 그 노드에 연결되어 있는 다른 노드도 작은 가중치로 연결되기 때문이다. 하아하하하



* 모범답안

  ```python
  5036
  
  import sys
  from collections import defaultdict, deque
  
  read = sys.stdin.readline
  
  def bfs(start, minimum):
      visited = [False] * (N + 1)
      visited[start] = True
      queue = deque([start])
      count = 0
  
      while queue:
          video = queue.popleft()
  
          for q, r in graph[video]:
              if not visited[q] and r >= minimum:
                  visited[q] = True
                  queue.append(q)
                  count += 1
  
      return count
  
  
  N, Q = map(int, read().split())
  graph = defaultdict(list)
  
  for _ in range(N - 1):
      p, q, r = map(int, read().split())
  
      graph[p].append((q, r))
      graph[q].append((p, r))
  
  
  for _ in range(Q):
      k, v = map(int, read().split())
      print(bfs(v, k))
  ```

  > 딕셔너리랑 튜플 쓰셨는데 이풀이가 더 빠른가봐.

