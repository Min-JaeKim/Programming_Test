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

> 처음에 엄청 꼬아서 생각했음.. 점점 풀다보니 그리디로 풀게 되어 다 뒤집어 엎고,, 새로 갈았다..
>
> 그리고 이코드에서 한 가지 틀린 게 뭐였냐면,
>
> - `while length <= len(s)//2+1:`
>
> 이거였음. while length <= len(s)//2: 이렇게 적었다가 반례 1이 통과가 안되었다 후우,,후후



* 모범답안

  ```python
  def solution(s):
      length = []
      result = ""
      
      if len(s) == 1:
          return 1
      
      for cut in range(1, len(s) // 2 + 1): 
          count = 1
          tempStr = s[:cut] 
          for i in range(cut, len(s), cut):
              if s[i:i+cut] == tempStr:
                  count += 1
              else:
                  if count == 1:
                      count = ""
                  result += str(count) + tempStr
                  tempStr = s[i:i+cut]
                  count = 1
  
          if count == 1:
              count = ""
          result += str(count) + tempStr
          length.append(len(result))
          result = ""
      
      return min(length)
  ```
  
  > 내 코드는 불필요하게 pop하는 것이 많은데,
  >
  > 이렇게 풀면 조금 더 효율적이게 풀 수있다. 멋지다.

