# Python 

## pro level2 타켓넘버

https://programmers.co.kr/learn/courses/30/lessons/43165

> ![image-20210620233422324](md-images/image-20210620233422324.png)



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
answer = 0
def solution(numbers, target):
    
    def dfs(num, tmp):
        global answer
        
        if num == len(numbers):
            if tmp == target:
                answer += 1
        else:
            dfs(num+1, tmp+numbers[num])
            dfs(num+1, tmp-numbers[num])
        
    dfs(0, 0)
    
    return answer
```

> 오늘은 좀 잘 안풀리는 날이라 쉽게 안풀렸다... 계속 배열을 조작하면 어떻게 하지.. 어떻게 하지.. 이러고만 있었다.. 걍 계속 더해나가면 되는거슬,, ㅉㅉ



* 모범답안

  ![image-20210620234821987](md-images/image-20210620234821987.png)

  ```python
  from itertools import product
  def solution(numbers, target):
      l = [(x, -x) for x in numbers]
      # print(*l)
      s = list(map(sum, product(*l)))
      # print(s)
      return s.count(target)
  ```

  > 

