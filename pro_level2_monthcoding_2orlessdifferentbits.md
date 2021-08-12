# Python 

## pro level2 2개 이하로 다른 비트

https://programmers.co.kr/learn/courses/30/lessons/77885

> ![image-20210812101815302](C:%5CUsers%5CPC%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20210812101815302.png)



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
def solution(numbers):
    answer = []
    
    for n in numbers:
        bin_n = ['0'] + list(bin(n)[2:])
        
        if bin_n[-1] == '0':
            answer.append(n+1)
            continue
            
        tmp = bin_n[:]
        
        for l in range(len(bin_n)-1,-1, -1):
            if bin_n[l] == '0':
                break
        tmp[l], tmp[l+1] = '1', '0'
        
        answer.append(int(''.join(tmp), 2))
        
            
    return answer
```

>



* 모범답안

  

  ```python
  def solution(numbers):
      answer = []
      for idx, val in enumerate(numbers):
          answer.append(((val ^ (val+1)) >> 2) +val +1)
  
      return answer
  ```
  
  > 

