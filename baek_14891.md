# Python

## baek 14891 톱니바퀴 실버1

https://www.acmicpc.net/problem/14891



> 100ms



* 문제

  > 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.
  >
  > ![img](md-images/1.png)
  >
  > 이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.
  >
  > ![img](md-images/2.png)
  >
  > ![img](md-images/3.png)
  >
  > 톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다. 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 예를 들어, 아래와 같은 경우를 살펴보자.
  >
  > ![img](md-images/4.png)
  >
  > 두 톱니바퀴의 맞닿은 부분은 초록색 점선으로 묶여있는 부분이다. 여기서, 3번 톱니바퀴를 반시계 방향으로 회전했다면, 4번 톱니바퀴는 시계 방향으로 회전하게 된다. 2번 톱니바퀴는 맞닿은 부분이 S극으로 서로 같기 때문에, 회전하지 않게 되고, 1번 톱니바퀴는 2번이 회전하지 않았기 때문에, 회전하지 않게 된다. 따라서, 아래 그림과 같은 모양을 만들게 된다.
  >
  > ![img](md-images/5.png)
  >
  > 위와 같은 상태에서 1번 톱니바퀴를 시계 방향으로 회전시키면, 2번 톱니바퀴가 반시계 방향으로 회전하게 되고, 2번이 회전하기 때문에, 3번도 동시에 시계 방향으로 회전하게 된다. 4번은 3번이 회전하지만, 맞닿은 극이 같기 때문에 회전하지 않는다. 따라서, 아래와 같은 상태가 된다.
  >
  > ![img](md-images/6.png)
  >
  > 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.
  >
  > 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
  >
  > ```bash
  > 10101111
  > 01111101
  > 11001110
  > 00000010
  > 2
  > 3 -1
  > 1 1
  > ```

* 출력

  > 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.
  >
  > - 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
  > - 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
  > - 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
  > - 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
  >
  > ```bash
  > 7
  > ```



```python
from collections import deque

'''
10'1'01111
01'1'111'0'1
11'0'011'1'0
00'0'000'1'0

n극은 0 s극은 1

시계 방향 회전
t4.appendleft(t4.pop())
반시계 방향 회전
t4.append(t4.popleft())


'''

t1 = deque(list(map(int, input())))
t2 = deque(list(map(int, input())))
t3 = deque(list(map(int, input())))
t4 = deque(list(map(int, input())))

n = int(input())
for i in range(n):
    k, dir = map(int, input().split())
    if k == 1:
        if t1[2] != t2[6]:
            if t2[2] != t3[6]:
                if t3[2] != t4[6]:
                    if dir == 1:
                        t4.append(t4.popleft())
                    else :
                        t4.appendleft(t4.pop())
                if dir == 1: # 시계라면 t2는 반시계
                    t3.appendleft(t3.pop())
                else:
                    t3.append(t3.popleft())
            if dir == 1:
                t2.append(t2.popleft())
            else:
                t2.appendleft(t2.pop())
        if dir == 1:
            t1.appendleft(t1.pop())
        else:
            t1.append(t1.popleft())
    elif k == 2:
        if t2[6] != t1[2]:
            if dir == 1:
                t1.append(t1.popleft()) # 반시계방향 회전
            else : # 반시계라면
                t1.appendleft(t1.pop()) # 시계방향 회전
        if t2[2] != t3[6]:
            if t3[2] != t4[6]:
                if dir == 1:
                    t4.appendleft(t4.pop())
                else :
                    t4.append(t4.popleft())
            if dir == 1: # 시계라면 t2는 반시계
                t3.append(t3.popleft())
            else:
                t3.appendleft(t3.pop())
        if dir == 1:
            t2.appendleft(t2.pop())
        else:
            t2.append(t2.popleft())
    elif k == 3:
        if t3[2] != t4[6]:
            if dir == 1:
                t4.append(t4.popleft()) # 반시계방향 회전
            else : # 반시계라면
                t4.appendleft(t4.pop()) # 시계방향 회전
        if t3[6] != t2[2]:
            if t2[6] != t1[2]:
                if dir == 1:
                    t1.appendleft(t1.pop())
                else :
                    t1.append(t1.popleft())
            if dir == 1: # 시계라면 t2는 반시계
                t2.append(t2.popleft())
            else:
                t2.appendleft(t2.pop())
        if dir == 1:
            t3.appendleft(t3.pop())
        else:
            t3.append(t3.popleft())
    else:
        if t4[6] != t3[2]:
            if t2[2] != t3[6]:
                if t1[2] != t2[6]:
                    if dir == 1:
                        t1.append(t1.popleft())
                    else :
                        t1.appendleft(t1.pop())
                if dir == 1: # 시계라면 t2는 반시계
                    t2.appendleft(t2.pop())
                else:
                    t2.append(t2.popleft())
            if dir == 1:
                t3.append(t3.popleft())
            else:
                t3.appendleft(t3.pop())
        if dir == 1:
            t4.appendleft(t4.pop())
        else:
            t4.append(t4.popleft())

result = 0
if t1[0] == 1:
    result += 1
if t2[0] == 1:
    result += 2
if t3[0] == 1:
    result += 4
if t4[0] == 1:
    result += 8
print(result)
```

> 그냥 풀었던 구현문제 헷갈렸던 부분은 2인덱스를 3인덱스로 착각했기 때문인데 이거 헷갈리면 컴공 아니지 않나 ㅋ ㅋ... 심히 나의 실력이 의심된다.



* 모범답안

  ```python
  arr = [list(map(int, list(input()))) for _ in range(4)]
  k = int(input())
  m = [list(map(int, input().split())) for _ in range(k)]
  
  def move(arr, di):
      if di == 1: narr = [arr[-1]]+arr[:-1]
      else : narr = arr[1:]+[arr[0]]
      return narr

  while m:
      m1, m2 = m.pop(0)
      m1 -= 1
      arr[m1] = move(arr[m1], m2)
      
      #left
      idx = m1
      d = m2
      while idx:
          if arr[idx][6+d] == arr[idx-1][2]: break
          idx -= 1
          d = -d
          arr[idx] = move(arr[idx],d)
      
      #right
      idx = m1
      d = m2
      while idx<3:
          if arr[idx][2+d] == arr[idx+1][6]: break
          idx += 1
          d = -d
          arr[idx] = move(arr[idx],d)
  
  print(arr[0][0] + arr[1][0]*2 + arr[2][0]*4 + arr[3][0]*8)
  ```
  
  > 헐 ㅋ ㅋ,,, 함수를 쓰니 이렇게 깔끔하게 풀 수 있구나 싶다. 천재같네..