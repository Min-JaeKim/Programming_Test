# Python

## baek 2961 도영이가 만든 맛있는 음식 실버1

https://www.acmicpc.net/problem/2961



> python3 76ms



* 문제

  > 도영이는 짜파구리 요리사로 명성을 날렸었다. 이번에는 이전에 없었던 새로운 요리에 도전을 해보려고 한다.
  >
  > 지금 도영이의 앞에는 재료가 N개 있다. 도영이는 각 재료의 신맛 S와 쓴맛 B를 알고 있다. 여러 재료를 이용해서 요리할 때, 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.
  >
  > 시거나 쓴 음식을 좋아하는 사람은 많지 않다. 도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다. 또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.
  > 
  > 재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 재료의 개수 N(1 ≤ N ≤ 10)이 주어진다. 다음 N개 줄에는 그 재료의 신맛과 쓴맛이 공백으로 구분되어 주어진다. 모든 재료를 사용해서 요리를 만들었을 때, 그 요리의 신맛과 쓴맛은 모두 1,000,000,000보다 작은 양의 정수이다.
  >
  > ```bash
  > 4
  > 1 7
  > 2 6
  > 3 8
  > 4 9
  > ```

* 출력

  > 첫째 줄에 신맛과 쓴맛의 차이가 가장 작은 요리의 차이를 출력한다. 
  >
  > ```bash
  > 1
  > ```
  
  

```python
from itertools import combinations

n = int(input())
arr = []
for _ in range(n):
    sour, bitt = map(int, input().split())
    arr.append([sour, bitt])
result = 1000000000

for i in range(1, n+1):
    for perm in combinations(arr,i):
        s, b = 1, 0
        for sour, bitt in perm:
            s *= sour
            b += bitt
        if abs(s - b) < result:
            result = abs(s - b)

print(result)
```

> 아정말 멍총이다 ㅜㅜ permutations를 써놓고 왜 시간초과 나지 시간초과나지 이러고 있었다 정말 바보 똥개 ㅜㅜ



* 모범답안

  ```python
  from itertools import combinations
  
  N = int(input())
  ingredients = [tuple(map(int, input().split())) for _ in range(N)]
  ingredients
  
  def cal(arr):
      s_list = [a[0] for a in arr]
      b_list = [a[1] for a in arr]
      s = 1
      for i in s_list:
          s *= i
      b = 0
      for i in b_list:
          b += i
  
      return abs(s-b)
  
  diff = float('inf')
  for i in range(1,N+1):
      for case in combinations(ingredients, i):
          tmp = cal(case)
          if tmp < diff:
              diff = tmp
  
  print(diff)
  ```

  > * __diff = float('inf')__ : 그어떤 수보다 더 큰 수
  >
  > ```python
  > # 순서가 있는 순열
  > for i in range(1, 4):
  >     for perm in permutations(a, i):
  >         print(perm)
  > ```
  >
  > > ([1, 2],)
  > > ([3, 4],)
  > > ([5, 6],)
  > > ([1, 2], [3, 4])
  > > ([1, 2], [5, 6])
  > > ([3, 4], [1, 2])
  > > ([3, 4], [5, 6])
  > > ([5, 6], [1, 2])
  > > ([5, 6], [3, 4])
  > > ([1, 2], [3, 4], [5, 6])
  > > ([1, 2], [5, 6], [3, 4])
  > > ([3, 4], [1, 2], [5, 6])
  > > ([3, 4], [5, 6], [1, 2])
  > > ([5, 6], [1, 2], [3, 4])
  > > ([5, 6], [3, 4], [1, 2])
  >
  > ```python
  > # 순서가 없는 조합
  > for i in range(1, 4):
  >     for com in combinations(a, i):
  >         print(com)
  > ```
  >
  > > ([1, 2],)
  > > ([3, 4],)
  > > ([5, 6],)
  > > ([1, 2], [3, 4])
  > > ([1, 2], [5, 6])
  > > ([3, 4], [5, 6])
  > > ([1, 2], [3, 4], [5, 6])
  >
  > 조합을 써야 시간초과가 안난다 이멍퉁아 ㅜㅜ

