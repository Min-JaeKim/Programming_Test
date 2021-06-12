# Python 

## pro level1 키패드 누르기

https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

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
'''
[3, 0] -> [0, 1] -> 4
[3, 2] -> [0, 1] -> 4
'''
def solution(numbers, hand):
    dr = (-1, 1, 0 ,0)
    dc = (0, 0, -1, 1)
    key = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    
    
    def num_find(num):
        for i in range(len(key)):
            for j in range(len(key[i])):
                if key[i][j] == num:
                    return [i, j]
        
        
    answer = ''
    hl, hr = [3,0], [3,2]
    
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            hl = num_find(n)
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            hr = num_find(n)
        else:
            num = num_find(n)
            dist_l = abs(hl[0]-num[0]) + abs(hl[1]-num[1])
            dist_r = abs(hr[0]-num[0]) + abs(hr[1]-num[1])
            if dist_l == dist_r:
                answer += hand[0].upper()
                if hand == 'right':
                    hr = num
                else:
                    hl = num
            else:
                if dist_l < dist_r:
                    answer += 'L'
                    hl = num
                else:
                    answer += 'R'
                    hr = num
            
    return answer
```

> 



* 모범답안

  ```python
  
  ```

  > 

