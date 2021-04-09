# Python

## pro level2 괄호변환

https://programmers.co.kr/learn/courses/30/lessons/60058



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
def uandv(p):
    global answer
    if len(p) == 0:     # 빈문자열일경우
        return ''       # 걍 return
    stack, o, c = [], 0, 0
    for i in p:
        if i == '(':    # 균형 문자열 찾기
            o += 1
        else:
            c += 1
        stack.append(i)
        if o == c:
            break
    u = stack
    testu, flag = [], True
    for i in u:         # 올바른 문자열 찾기
        if i == '(':
            testu.append(i)
        else:
            if not testu:
                flag = False    # 올바르지 않다면
                break
            else:
                testu.pop()
    v = uandv(p[o + c:])
    if not flag:            # 올바르지 않다면 제시문 따라서
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i] = ')'
        v = '(' + v + ')' + ''.join(u)
    else:                   # 올바르다면
        v = ''.join(u) + v  # u에다가 v를 붙여 return
    return v


def solution(p):
    answer = uandv(p)
    return answer
```

> 문제가 이해가 되지 않아서 한참을 헤맸던 문제.
>
> 그런데 진짜 문제 그대로 코드 짜면 된다. 푸핫,,



* 모범답안

  ```python
  def solution(p):
      if p=='': return p
      r=True; c=0
      for i in range(len(p)):
          if p[i]=='(': c-=1
          else: c+=1
          if c>0: r=False
          if c==0:
              if r:
                  return p[:i+1]+solution(p[i+1:])
              else:
                  return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
  ```
  
  > 이게,,, 뭔소리지? 이해 못했슴,,,

