# Python 

## pro level3 표 편집

https://programmers.co.kr/learn/courses/30/lessons/81303

> ![image-20210906211135487](md-images/image-20210906211135487.png)



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
from heapq import *


def solution(n, k, cmd):
    answer = ['O'] * n
    left, right, delete = [], [], []
    for i in range(n):
        heappush(right, i)
    for i in range(k):
        heappush(left, -heappop(right))
    
    for c in cmd:
        if len(c) > 1:
            alpha, num = c.split()
            num = int(num)
        else:
            alpha = c
        
        if alpha == 'U':
            for _ in range(num):
                heappush(right, -heappop(left))
        elif alpha == 'D':
            for _ in range(num):
                heappush(left, -heappop(right))
        elif alpha == 'C':
            delete.append(heappop(right))
            if not right:
                heappush(right, -heappop(left))
        else:
            if delete[-1] < right[0]:
                heappush(left, -delete.pop())
            else:
                heappush(right, delete.pop())
        
    while delete:
        answer[delete.pop()] = 'X'
        
    return ''.join(answer)
```

>하,, 비효율적으로 삭제할 때마다 x하고 up & down 할 때도 x있을 때는 cnt 세주지 않으면서 for문 엄청 돌려서 풀었더니 마지막 서너문제 시간 초과났었다.
>
>그러다가 다른 풀이도 찾아봤는데 너무 힘들어서 포기하고 있을 즈음에 힙큐로 푼 문제를 찾았다 오예에에에 엄청 졸았는데 이런 쉬운 풀이 보니까 갑자기 잠이 팍 깼다. 앞으로 이런 사고 능력도 좀 길러졌으면 좋겠다



* 모범답안

  ```python

  ```
  
  > 

