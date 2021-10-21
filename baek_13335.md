# python

## baek 13335 트럭 실버1

https://www.acmicpc.net/problem/13335

> python3 100ms
>



* 문제

  > 강을 가로지르는 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n 개의 트럭이 건너가려고 한다. 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다. 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 다리의 길이는 w 단위길이(unit distance)이며, 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다. 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.
  >
  > 예를 들어, 다리의 길이 w는 2, 다리의 최대하중 L은 10, 다리를 건너려는 트럭이 트럭의 무게가 [7, 4, 5, 6]인 순서대로 다리를 오른쪽에서 왼쪽으로 건넌다고 하자. 이 경우 모든 트럭이 다리를 건너는 최단시간은 아래의 그림에서 보는 것과 같이 8 이다.
  >
  > ![img](md-images/1.png)
  >
  > Figure 1. 본문의 예에 대해 트럭들이 다리를 건너는 과정.
  >
  > 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때, 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하라.
  
* 입력

  > 입력 데이터는 표준입력을 사용한다. 입력은 두 줄로 이루어진다. 입력의 첫 번째 줄에는 세 개의 정수 n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)이 주어지는데, n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다. 입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데, ai는 i번째 트럭의 무게를 나타낸다.
  >
  > ```bash
  >4 2 10
  > 7 4 5 6
  >```
  > 
  
* 출력

  > 출력은 표준출력을 사용한다. 모든 트럭들이 다리를 건너는 최단시간을 출력하라.
  >
  > ```bash
  > 8
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    n, w, l = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque([])
    idx, time, time2, wt, res = 0, 1, 0, 0, 0

    while idx < n:
        while l < wt + arr[idx]:
            tmp_wt, tmp_time = q.popleft()
            wt -= tmp_wt
            time2 = tmp_time + w
        truck_time = max(time, time2)
        q.append([arr[idx], truck_time])
        wt += arr[idx]
        idx += 1
        res = truck_time
        time = truck_time + 1

    print(res + w)


sol()
```

> 이걸 뭘 그렇게 오래 푸냐,,
>
> 너무너무너무 쉬운데 스스로 자괴감 들게 하는 그런 문제였다 하,,



* 모범답안

  ```python
  72
  
  import sys
  
  
  def solution(n, w, load, trucks):
      # 변수 초기화
      t_len = len(trucks)
      timer = [0] * t_len
      answer = 0
      cur_capacity = trucks[0]
      timer[0] = 1
      # head 는 다음에 추가 할 트럭의 index
      # tail 은 다음에 빼야 할 트럭의 index
    head, tail = 0, 0
      while tail < t_len:
          # 0. 1초 흐름
          answer += 1  # 1초 늘려
          # 1. 트럭이 다리를 다 지나간 상황
          if timer[tail] + w <= answer:
              cur_capacity -= trucks[tail]
              tail += 1
          # 2. 더이상 올라올 트럭이 없음
          if head + 1 >= t_len:
              continue
          # 3. 트럭이 다리에 더 올라올 수 있는 상황
          if cur_capacity + trucks[head + 1] <= load:
              cur_capacity += trucks[head + 1]
              timer[head + 1] = answer
              head += 1
  
      return answer
  
  
  if __name__ == "__main__":
      N, W, L = map(int, sys.stdin.readline().rstrip().split())
      A = list(map(int, sys.stdin.readline().rstrip().split()))
      print(solution(N, W, L, A))
  ```
  
  > 

