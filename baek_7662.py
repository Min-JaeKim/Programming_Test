# python

## baek 7662 이중 우선순위 큐 골드5

https://www.acmicpc.net/problem/7662

> python3 10548ms
>



* 문제

  > 이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다. 전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다. 이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다. 데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다. 
  >
  > 정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자. 
  >
  > Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.
  
* 입력

  > 입력 데이터는 표준입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 Q에 적용할 연산의 개수를 나타내는 정수 k (k ≤ 1,000,000)가 주어진다. 이어지는 k 줄 각각엔 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n이 주어진다. ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다. ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다. 최댓값(최솟값)을 삭제하는 연산에서 최댓값(최솟값)이 둘 이상인 경우, 하나만 삭제됨을 유념하기 바란다.
  >
  > 만약 Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시해도 좋다. Q에 저장될 모든 정수는 32-비트 정수이다. 
  >
  > ```bash
  > 2
  > 7
  > I 16
  > I -5643
  > D -1
  > D 1
  > D 1
  > I 123
  > D -1
  > 9
  > I -45
  > I 653
  > D 1
  > I -642
  > I 45
  > I 97
  > D 1
  > D -1
  > I 333
  > ```
  >
  
* 출력

  > 출력은 표준출력을 사용한다. 각 테스트 데이터에 대해, 모든 연산을 처리한 후 Q에 남아 있는 값 중 최댓값과 최솟값을 출력하라. 두 값은 한 줄에 출력하되 하나의 공백으로 구분하라. 만약 Q가 비어있다면 ‘EMPTY’를 출력하라.
  >
  > ```bash
  > EMPTY
  > 333 -45
  > ```



```python
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def sol():
    t = int(input())
    for _ in range(t):
        n = int(input())
        heap, maxheap, v = [], [], [0] * 1000001

        for i in range(n):
            order = list(input())
            number = int(''.join(order[2:]))

            if order[0] == 'I':
                heappush(heap, [number, i])
                heappush(maxheap, [-number, i])

            else:
                if number == 1:
                    while maxheap and v[maxheap[0][1]]:
                        heappop(maxheap)
                    if maxheap:
                        v[maxheap[0][1]] = 1
                        heappop(maxheap)

                else:
                    while heap and v[heap[0][1]]:
                        heappop(heap)
                    if heap:
                        v[heap[0][1]] = 1
                        heappop(heap)

        while heap and v[heap[0][1]]:
            heappop(heap)
        while maxheap and v[maxheap[0][1]]:
            heappop(maxheap)

        if not heap:
            print('EMPTY')
        else:
            print(-maxheap[0][0], heap[0][0])


sol()
```

> 하,, 뭔 10초나 걸리냐 6초짜리 문젠데 ㅋㅋㅋㅋ. 심지어 이중순위큐를 어떻게 구현해야 하는지 고민했음. 처음에는 받아올 때마다 -1000000 <= 숫자 <= 1000000 인 줄 알고 단순히 방문 배열을 백만까지만 만들었음. 그래서 수가 들어올 때마다 1을 더하거나 pop할 때 빼주는 방식으로 했는데 완조니 틀렸었음. 그래서 인덱스 방식을 찾아서 했는데. 결국엔 이거였다. 그리고 어처구니 없는게 맨끝에 혹시 heap에서는 방문한 걸 maxheap에서는 pop 안했을까봐 while문 돌려서 확인해 줬는데, 이걸 들여 쓰기 한 번 더 해서 틀렸었다. 이거 반례 찾느라 힘들었는데 로직을 찬찬히 보니까,, 그러했다 하아,,



* 모범답안

  ```python
  3300
  import bisect
  import sys
  from collections import deque
  input = sys.stdin.readline
  
  
  def solve():
      pq = deque()
      pqDict = dict()
      for _ in range(int(input())):
          cmd = input().split()
          if cmd[0] == 'I':
              val = int(cmd[1])
            if val not in pqDict:
                  bisect.insort_left(pq, val)
                  pqDict[val] = 1
              else:
                  pqDict[val] += 1
          else:
              if not pq:
                  continue
              if cmd[1] == '1':
                  if (v := pqDict[pq[-1]]) > 1:
                      pqDict[pq[-1]] = v-1
                  else:
                      pqDict.pop(pq[-1])
                      pq.pop()
              else:
                  if (v := pqDict[pq[0]]) > 1:
                      pqDict[pq[0]] = v-1
                  else:
                      pqDict.pop(pq[0])
                      pq.popleft()
      if not pq:
          print("EMPTY")
      else:
          print(pq[-1], pq[0])
  
  
  if __name__ == '__main__':
      for _ in range(int(input())):
          solve()
  ```
  
  > - bisect 
  >   - 이진 탐색 알고리즘
  >   - insort(array, value)
  >     - 이진탐색으로 적절한 자리에 value값을 array에 삽입

