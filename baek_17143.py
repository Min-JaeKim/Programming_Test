# python

## baek 17143 낚시왕 골드2

https://www.acmicpc.net/problem/17143

> python3 2364ms

* 문제

  > 낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다. 격자판의 각 칸은 (r, c)로 나타낼 수 있다. r은 행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다. 칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다. 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.
  >
  > 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
  > 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
  > 3. 상어가 이동한다.
  >
  > 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다. 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
  >
  > 왼쪽 그림의 상태에서 1초가 지나면 오른쪽 상태가 된다. 상어가 보고 있는 방향이 속도의 방향, 왼쪽 아래에 적힌 정수는 속력이다. 왼쪽 위에 상어를 구분하기 위해 문자를 적었다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
  >
  > 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.

* 입력

  > 첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)
  >
  > 둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
  >
  > 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
  >
  > ```bash
  > 4 6 8
  > 4 1 3 3 8
  > 1 3 5 2 9
  > 2 4 8 4 1
  > 4 5 0 1 4
  > 3 3 1 2 7
  > 1 5 8 4 3
  > 3 6 2 1 2
  > 2 2 2 3 5
  > ```
  >
  
* 출력

  > 낚시왕이 잡은 상어 크기의 합을 출력한다.
  >
  > ```bash
  > 22
  > ```



- 

```python
import sys
from collections import defaultdict
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, 1, -1)


def sol():
    r, c, m = map(int, input().split())
    arr = [[-1] * c for _ in range(r)]
    idx, jaws, res = 0, defaultdict(list), 0

    for _ in range(m):
        rr, cc, s, d, z = map(int, input().split())
        jaws[idx] = [rr-1, cc-1, s, d-1, z]
        arr[rr-1][cc-1] = idx
        idx += 1

    king = 0

    while king < c:
        for i in range(r):
            if arr[i][king] != -1:
                res += jaws[arr[i][king]][4]
                del jaws[arr[i][king]]
                arr[i][king] = -1
                break

        for i in range(r):
            for j in range(c):
                if arr[i][j] != -1:
                    idx = arr[i][j]
                    arr[i][j] = -1
                    rr, cc, ss, d, z = jaws[idx]
                    s = ss

                    while s > 0:
                        if d == 0:
                            if s > rr:
                                s -= rr
                                rr, d = 0, 1
                            else:
                                rr -= s
                                s = 0
                        if d == 1:
                            if s > r - 1 - rr:
                                s = s - (r - 1- rr)
                                rr, d = r-1, 0
                            else:
                                rr += s
                                s = 0
                        if d == 2:
                            if s > c - 1 - cc:
                                s = s - (c - 1 - cc)
                                cc, d = c-1, 3
                            else:
                                cc += s
                                s = 0
                        if d == 3:
                            if s > cc:
                                s -= cc
                                cc, d = 0, 2
                            else:
                                cc -= s
                                s = 0

                    jaws[idx] = [rr, cc, ss, d, z]

        for i in range(m):
            if i in jaws:
                rr, cc, s, d, z = jaws[i]
                if arr[rr][cc] != -1:
                    if jaws[arr[rr][cc]][4] > z:
                        del jaws[i]
                    else:
                        del jaws[arr[rr][cc]]
                        arr[rr][cc] = i
                else:
                    arr[rr][cc] = i

        king += 1

    print(res)


sol()
```

> 아오씨 방향 설정하는 것 때문에 한참 고민하다가 결국 약속시간 되어서 지금 다시 품. 근데 한 십분만인가,, 그정도 시간만 들이니까 맞을 수 있었다.
>
> 원인은 이동한 상어들을 나중에 한꺼번에 배치해 줘야 하는데 내가 다르게 풀었다. 이동한 순서대로 상어들을 배치해줬었음. 그렇게 되면 아직 이동하지 않은 상어들이 먹혀버리기 때문에 틀릴 수 밖에 없었다. 괜히 바보 같이 방향 전환을 잘못한 줄 알고 한참 봤다 우에엥 근데 내가 생각해도 방향 전환을 너무 빠르게 구현해 버려서 실수가 있을 것이라고 생각이 들었을 수 밖에 없었다.



* 모범답안

  ```python
  740
  
  import sys
  input = sys.stdin.readline
  R, C, M = map(int, input().split())
  arr = {}
  m_r = int((R-1)*2)
  m_c = int((C-1)*2)
  result = 0
  for _ in range(M):
      r,c,s,d,z = map(int, input().split())
      arr[(r-1,c-1)]=[s,d,z]
  
  
  def next_arr(arr, p):
      new_fish_index = {}
      global m_r, m_c, R, result
      for i in range(R):
          if (i,p) in arr:
              result+=arr[(i,p)][2]
              del arr[(i,p)]
              break
      for key, value in arr.items():
          if value[1]<3:
              d = 2
              idx = 0
              if m_r>0:
                  if value[1] == 2:
                      idx = (key[0] + value[0]) % m_r
                  else:
                      idx = (m_r + value[0] - key[0]) % m_r
                  if idx>m_r-idx:
                      d = 1
                      idx = m_r - idx
              new_idx = (idx,key[1])
              value[1] = d
              if new_idx in new_fish_index:
                  if value[2]>new_fish_index[new_idx][2]:
                      new_fish_index[new_idx] = value
              else:
                  new_fish_index[new_idx] = value
          else:
              d = 3
              idx = 0
              if m_c>0:
                  if value[1] == 3:
                      idx = (key[1] + value[0]) % m_c
                  else:
                      idx = (m_c + value[0] - key[1]) % m_c
                  if idx>m_c-idx:
                      d = 4
                      idx = m_c - idx
              new_idx = (key[0],idx)
              value[1] = d
              if new_idx in new_fish_index:
                  if value[2]>new_fish_index[new_idx][2]:
                      new_fish_index[new_idx] = value
              else:
                  new_fish_index[new_idx] = value
      #print_data(new_fish_index)
      return new_fish_index
  
  def print_data(fish_data):
      global R,C
      arr = [[0]*C for i in range(R)]
      for key,value in fish_data.items():
          arr[key[0]][key[1]] = value[2]
      for _ in arr:
          print(_)
      print()
  
  for i in range(C):
      arr = next_arr(arr,i)
  print(result)
  ```

  > 아 확실히 이동하는 걸 수학적으로 풀면 시간을 단축할 수 있구나.
  >
  > 근데 난 이런 걸 바로바로 생각할 수가 없는듯혀

