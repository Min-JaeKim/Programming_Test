# python

## baek 9465 스티커 실버2

https://www.acmicpc.net/problem/9465

> python3 994ms



* 문제

  > 상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.
  >
  > 상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
  >
  > ![img](md-images/sticker.png)
  >
  > 모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다. 먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.
  >
  > 위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 점수는 260이 되고 이 것이 최대 점수이다. 가장 높은 점수를 가지는 두 스티커 (100과 70)은 변을 공유하기 때문에, 동시에 뗄 수 없다.

* 입력

  > 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다. 다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다. 연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다. 
  >
  > ```bash
  >2
  > 5
  >50 10 100 20 40
  > 30 50 70 10 60
  > 7
  > 10 30 10 50 100 20 40
  > 20 40 30 50 60 20 80
  > ```
  > 
  
* 출력

  > 각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.
  >
  > ```bash
  > 260
  > 290
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(2)]
        dp = [[0] * n for _ in range(2)]
        dp[0][0], dp[1][0], dp[0][1], dp[1][1] = arr[0][0], arr[1][0], arr[0][1] + arr[1][0], arr[1][1] + arr[0][0]

        for i in range(2, n):
            dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
            dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])

        print(max(dp[0][-1], dp[1][-1]))


sol()
```

> 가벼운 dp문제 dp는 규칙만 찾으면 답을 금방 구할 수 있다.



* 모범답안

  ```python
  712
  
  from sys import stdin
  
  readline = stdin.readline
  
  def get_max_score():
      N = int(readline())
      stickers = [list(map(int, readline().split())) for _ in range(2)]
      # 상단 스티커를 땐 경우
      # 하단 스티커를 땐 경우
      # 아무것도 때지 않은 경우
      up, down, none = 0, 0, 0
  
      for i in range(N):
          # 위 스티커를 땐 경우 > 이전 아래 스티커를 땐 경우, 아무것도 때지 않은 경우 중 큰 것
          # 아래 스티커를 땐 경우 > 이전 위 스티커를 땐 경우, 아무것도 때지 않은 경우 중 큰 것        
          # 아무것도 때지 않은 경우 > 이전의 위, 아래를 땐 경우 중 큰 것
          up, down, none = max(down, none) + stickers[0][i], max(up, none) + stickers[1][i], max(up, down)
  
      return max(none, up, down)
  
  
  if __name__ == "__main__":
      T = int(readline())
      for _ in range(T):
          print(get_max_score())
  ```
  
  > 나처럼 dp배열을 만들어서 사용하는 것이 아니라 단순히 변수에 저장하며 진행해 나갔다. 그래서 0.2초 빨랐던 것이라고 생각..

