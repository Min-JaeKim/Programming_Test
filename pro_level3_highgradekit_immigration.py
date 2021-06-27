# Python 

## pro level3 입국심사

https://programmers.co.kr/learn/courses/30/lessons/43238

> ![image-20210628000131160](md-images/image-20210628000131160.png)



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
def solution(n, times):
    left, right = 1, max(times) * n
    
    while left < right:
        mid, tmp = (left+right)//2, 0
        
        for t in times:
            tmp += mid//t
            
        if n <= tmp:
            right = mid
        else:
            left = mid + 1
    
    return right
```

>대체 어떻게 이분 탐색을 해야하나 싶었다. 여기서 더 헷갈렸던 부분은 `20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.` 이 부분이었다. 그래서 답을 봄.
>
>1분부터 최대 시간 사이의 중점을 잡아 그 시간동안 한 심사대에서 심사 받을 수 있는 사람을 모조리 더하는 것이다. 그리고 중요한 것은 while 조건은 left가 right보다 꼭 작다는 조건이어야 한다. 그리고, left를 1씩 높여가야 하며, right는 계속 mid로 주며 낮춰 주는 조건으로 가야 함.



* 모범답안

  

  ```python
  
  ```

  > 

