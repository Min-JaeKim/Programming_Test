# Python

## baek 1074 Z 실버1

https://www.acmicpc.net/problem/1074



> python3 68ms
>
> pypy3 ms



* 문제

  > 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
  >
  > ![img](md-images/preview)
  >
  > 만약, N > 1이 라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
  >
  > 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
  >
  > ![img](md-images/preview)
  >
  > N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
  >
  > 다음은 N=3일 때의 예이다.
  >
  > ![img](md-images/preview)

* 입력

  > 첫째 줄에 정수 N, r, c가 주어진다.
  >
  > ```bash
  >2 3 1
  > ```
  
* 출력

  > r행 c열을 몇 번째로 방문했는지 출력한다.
  >
  > ```bash
  > 11
  > ```



```python
'''
로직 설명
1. 질문 검색을 보니 4분할을 하라는 말이 많았습니다.
2. 그래서 고등학생 때를 떠올려
제 1사분면 제 2사분면 제 3사분면 제 4사분면
으로 구분해 값을 찾아나갔습니다.
3. 만약 찾고자 하는 크기가 1이 된다면
순회하면서 답을 더해줬습니다.
'''

import sys
input = sys.stdin.readline


def rcs(row, col, size): # 재귀
    global result
    if size == 1:
        if row == r and col == c:
            print(result)
            exit()
    if row <= r < row + size and \
        col <= c < col + size:
        pass
    else:
        result += size**2
        return

    size //= 2
    rcs(row, col, size)             # 제 1사분면
    rcs(row, col+size, size)        # 제 2사분면
    rcs(row+size, col, size)        # 제 3사분면
    rcs(row+size, col+size, size)   # 제 4사분면


n, r, c = map(int, input().split())
result = 0
size = 2**n // 2    # mid

rcs(0, 0, size)
rcs(0, size, size)
rcs(size, 0, size)
rcs(size, size, size)

'''
10 435 651
445007
'''


```

> 



* 모범답안

  ```python
  N, r, c = map(int, input().split())
  
size = 2 ** N       # 방문 범위의 한 변 크기
  num_start = 0       # 방문 순서 범위의 시작
  index_start_r = 0   # 방문 범위의 시작 r
  index_start_c = 0   # 방문 범위의 시작 c
  
  # 분할 정복
  # 4분의 1 구역 중 해당되는 범위 확인: 가로, 세로 -> 해당 기준에 맞춰 출발(현재 크기/4*i), 도착(현재 크기/4*i+1) 입력
  # 크기가 1이 되면 그 때 숫자를 return
  while size > 1:
      size //= 2      # 4분할
      quarter = [True for _ in range(4)]  # 세부 분할면 결정: 0 1 / 2 3
  
      # 가로 범위 이탈 제외
      if r < index_start_r+size:
          quarter[2], quarter[3] = False, False
      else:
          quarter[0], quarter[1] = False, False
          index_start_r += size   # 아래쪽 영역이므로 다음 시작 범위 변경
  
      # 세로 범위 이탈 제외
      if c < index_start_c+size:
          quarter[1], quarter[3] = False, False
      else:
          quarter[0], quarter[2] = False, False
          index_start_c += size   # 오른쪽 영역이므로 다음 시작 범위 변경
  
      # 방문 순서 시작수 변경
      num_start += (size ** 2 * [i for i in range(4) if quarter[i]][0])
  
  print(num_start)
  ```
  
  > 와 재귀로 풀리는 건 반복문으로도 분명 풀리는 건데
  >
  > 난 이렇게 생각을 못했을까. 대단하다.