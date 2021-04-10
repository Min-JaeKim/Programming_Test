# Python

## pro level2 문자열압축

https://programmers.co.kr/learn/courses/30/lessons/60057



> ![image-20210410233142244](md-images/image-20210410233142244.png)



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
def solution(s):
    answer = float('inf')
    length = 1
    while length <= len(s)//2+1:
        stack = []
        stack.append(s[:length])
        idx = length
        while idx < len(s):
            if ''.join(stack[-1]) == s[idx:idx+length]:
                stack.pop()
                tmpnum = []
                if stack:
                    if stack[-1].isdigit():
                        tmpnum.insert(0, stack.pop())
                    if tmpnum:
                        tmpnum = int(''.join(tmpnum)) + 1
                    else:
                        tmpnum = 2
                else:
                    tmpnum = 2
                stack.append(str(tmpnum))
            stack.append(s[idx:idx+length])
            idx += length
        stack = ''.join(stack)
        answer = min(answer, len(stack))
        length += 1
    return answer
```

> 



* 모범답안

  ```python
  
  ```
  
  > 

