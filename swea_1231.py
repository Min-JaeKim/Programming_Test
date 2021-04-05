# python

## swea 1231 d4 중위순회

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD



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
import sys
sys.stdin = open('./input.txt')

def ffind(c):
    if leftc[c] != 0:
        ffind(leftc[c])
    print(alpha[c], end='')
    leftc[p[c]] = 0
    if rightc[c] != 0:
        ffind(rightc[c])

for tc in range(1,11):
    n = int(input())
    alpha = ['' for _ in range(n+1)]
    leftc = [0 for _ in range(n+1)]
    rightc = [0 for _ in range(n+1)]
    p = [0 for _ in range(n+1)]
    for _ in range(n):
        tmp = list(input().split())
        if len(tmp) > 1:
            alpha[int(tmp[0])] = tmp[1]
            if len(tmp) > 2:
                leftc[int(tmp[0])] = int(tmp[2])
                p[int(tmp[2])] = int(tmp[0])
                if len(tmp) > 3:
                    rightc[int(tmp[0])] = int(tmp[3])
                    p[int(tmp[3])] = int(tmp[0])
    print('#%d' % tc, end = ' ')
    ffind(1)
    print()
```

> 내 코드는 진짜 난리났다,,, 하,,, 아직 갈길이 멀구나,, 정신차려야겠다





* 모범답안

  ```python
  def in_order(x):
      global path
      if x <= e:
          in_order(x * 2)
          path += Table[x]
          in_order(x * 2 + 1)
   
   
  for tc in range(1, 11):
      e = int(input())
      Table = [0] * (e + 1)
       
      for i in range(1, e + 1):
          Data = input().split()
          Table[i] = Data[1]
   
      path = ''
      in_order(1)
   
      print('#%s %s' % (tc, path))
  ```
  
  > 와,,
  >
  > 머리 진짜 안돈다,,, 대박이다 이렇게 풀 수 있구나.
  >
  > 트리부터는 진짜 머리 싸움인 것 같기도 하다,, 어떻게 이렇게 효율적인 코드를 짤까? 존경스럽다.