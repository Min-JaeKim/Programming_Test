# python

## baek 20055 컨베이어 벨트 위의 로봇 실버1

https://www.acmicpc.net/problem/20055

> python3 1976ms



* 문제

  > 길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다. 벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져 있으며, 각 칸에는 아래 그림과 같이 1부터 2N까지의 번호가 매겨져 있다.
  >
  > ![img](md-images/preview)
  >
  > 벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동한다. i번 칸의 내구도는 Ai이다. 위의 그림에서 1번 칸이 있는 위치를 "**올리는 위치**", N번 칸이 있는 위치를 "**내리는 위치**"라고 한다.
  >
  > 컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려고 한다. 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다. 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다. 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.
  >
  > 컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다. 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.
  >
  > 
  >
  > 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
  > 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
  >    1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
  > 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
  > 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
  >
  > 종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.
  
* 입력

  > 첫째 줄에 N, K가 주어진다. 둘째 줄에는 A1, A2, ..., A2N이 주어진다.
  >
  > ```bash
  > 3 2
  > 1 2 1 2 1 2
  > ```
  >
  
* 출력

  > 몇 번째 단계가 진행 중일때 종료되었는지 출력한다.
  >
  > ```bash
  > 2
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    robot = deque([0] * n)
    arr = deque(arr)
    cnt = 1

    while 1:
        arr.rotate(1)
        robot.rotate(1)
        robot[n-1] = 0

        for i in range(n-1, 0, -1):
            if robot[i-1] and not robot[i] and arr[i]:
                robot[i], robot[i-1] = 1, 0
                arr[i] -= 1
                if i == n-1:
                    robot[i] = 0

        if arr[0] and not robot[0]:
            arr[0] -= 1
            robot[0] = 1

        if arr.count(0) >= k:
            break
        cnt += 1

    print(cnt)


sol()
```

> 와 문제가 무슨말인지 몰라서 며칠 동안 못풀고 있었는데 말이야,,? 오늘 아침 읽어 보니까 갑자기 알겠더라고,, 왜지? 참 이상하다. 이문제 이해 못해서 이번 생에는 끝끝내 못 풀 줄 알았단 말이지,,  결국 풀었군 오래 걸리긴 했지만 ㅎㅎ
>
> 그냥,, 구현이다 문제에 주어진 대로만 코드를 짜면 되는 구현,, 그리고 한 가지 유의할 것은 로봇은 내리는 위치에 오면 과감하게 내려버리기 때문에 처리를 해줘야 한다.



* 모범답안

  ```python
  1528
  
  import sys
  
  def process(N, K):
      belt = list(map(int, sys.stdin.readline().split()))
      robot = [ False for _ in range(N) ]
  
      step = 0
      numOfZero = 0
  
      # print('before', belt)
      # print('before', robot)
  
      while True:
          step += 1
  
          # 1. 회전 & 내리기
          belt.insert(0, belt[2*N-1])
          belt.pop()
          robot.insert(0, False)
          robot.pop()
  
          robot[N-1] = False
  
          # print('after', belt)
          # print('after', robot)
  
          # 2. 로봇 움직이기
          for i in range(N-2, 0, -1):
              if robot[i] and not robot[i+1] and belt[i+1] > 0:
                  robot[i+1] = True
                  robot[i] = False
                  belt[i+1] -= 1
                  if (belt[i+1] == 0): numOfZero += 1
  
          # 3. 로봇 올리기
          if belt[0] > 0:
              robot[0] = True
              belt[0] -= 1
              if (belt[0] == 0): numOfZero += 1
  
          # print('final', belt)
          # print('final', robot)
  
          # 4. 내구도 체크
          if numOfZero >= K: return step
  
  N, K = map(int, sys.stdin.readline().split())
  
  print(process(N, K))
  ```
  
  > 아 insert와 pop을 쓰셧군

