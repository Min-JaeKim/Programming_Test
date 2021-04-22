# python

## swea 5247 d4 연산

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do



> 

* 문제

  > 
  
* 입력

  > 
  >
  > ```bash
  >
  > ```
  
* 출력

  > 
  >
  > ```bash
  >
  > ```



```python
from collections import deque


for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    res = float('inf')
    q = deque([[a, 0]])
    v = {}
    while q:
        num, cnt= q.popleft()
        if v.get(num, 0):   # 만약 이미 한 번 만나본 숫자라면
            continue
        else:
            v[num] = 1      # 아니라면 방문표시
        if cnt > 1000000 or num > b + 10 or num < 0:
            continue
        if num == b:
            res = cnt
            break
        q.append([num + 1, cnt + 1])
        q.append([num - 1, cnt + 1])
        q.append([num * 2, cnt + 1])
        q.append([num - 10, cnt + 1])
    print('#%d %d' % (tc, res))
```

> 처음에 dfs로 풀었다.
>
> 예상하고 있었지만 역시 시간초과.. 하 진짜 너무,, 어려운 것 같다.
>
> 결국 시간초과의 벽을 넘지 못하고 다른 사람 풀이를 봤고 딕셔너리를 사용하라는 좋은 해설을 보았다.



* 모범답안

  ```python
  
  ```
  
  > 