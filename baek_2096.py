# python

## baek 2096 내려가기 골드4

https://www.acmicpc.net/problem/2096

> python3 288ms



* 문제

  > N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.
  >
  > 먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.
  >
  > ![img](md-images/down.png)
  >
  > 별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.
  
* 입력

  > 첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.
  >
  > ```bash
  > 3
  > 1 2 3
  > 4 5 6
  > 4 9 0
  > ```
  >
  
* 출력

  > 첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.
  >
  > ```bash
  > 18 6
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    left_max, mid_max, right_max = 0, 0, 0
    left_min, mid_min, right_min = 0, 0, 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        left_max, mid_max, right_max = max(left_max + a, mid_max + a), max(left_max + b, mid_max + b, right_max + b), max(mid_max + c, right_max + c)
        left_min, mid_min, right_min = min(left_min + a, mid_min + a), min(left_min + b, mid_min + b, right_min + b), min(mid_min + c, right_min + c)

    print(max(left_max, mid_max, right_max), min(left_min, mid_min, right_min))


sol()
```

> 와 미친 나 1등이다
>
> 처음에는 당연히 dp 배열 선언해서 했는데 (사실 bfs로 해야하는 건가 싶어서 고민하다가 알고리즘 분류를 보게댐 ;; 이것부터 큰 실수) 메모리초과가 났다.
>
> 휴 그리고 너무 그러면 안됐었는데 질문검색을 보고 배열에 저장하지 않고, 입력 받는 즉시 처리해 줘도 됨을 깨달음.
>
> 결국 맞긴 했는데,, 너무 혼자 고민하는 시간을 안 갖는 것 같아서 그게 가장 큰 문제 같다.



* 모범답안

  ```python
  
  ```
  
  > 

