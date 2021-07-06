# Python 

## pro level3 징검다리 건너기

https://programmers.co.kr/learn/courses/30/lessons/64062

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

```

>



* 모범답안

  ![image-20210706134528656](md-images/image-20210706134528656.png)

  ```python
  def solution(stones, k):
      left, right = 1, 200000000
      
      while left < right:
          mid, cnt = (left + right) // 2, 0
          for t in stones:
              if t - mid <= 0:
                  cnt += 1
              else:
                  cnt = 0
              if cnt >= k:
                  break
          if cnt >= k:
              right = mid
          else:
              left = mid + 1
              
      return left
  ```
  
  > 도무지 이분탐색이라는 풀이가 생각이 안났는데 아무튼 지금은 이해했다.. 휴.. 이해한 토대로 풀이를 작성해 보자.
  >
  > 일단 최소인원 최대인원 각각 1명과 200000000으로 둔다. (각 stone의 최소 최대 크기)
  >
  > 각 돌을 mid로 빼면서 현재 지나갈 수 있는 인원을 계속 탐색한다. 결론적으로 left와 right는 같아진다는 점. 

