# Python 

## pro level2 더 맵게

https://programmers.co.kr/learn/courses/30/lessons/42626

> .



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
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1
    return -1 if scoville[0] < K else answer
```

> 



* 모범답안

  ```python
  
  ```

  > 

