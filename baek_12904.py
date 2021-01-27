# Python

## baek 12904

https://www.acmicpc.net/problem/12904



> 104ms



* 문제

  > 수빈이는 A와 B로만 이루어진 영어 단어가 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.
  >
  > 이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
  >
  > - 문자열의 뒤에 A를 추가한다.
  > - 문자열을 뒤집고 뒤에 B를 추가한다.
  >
  > 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

* 입력

  > 첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 999, 2 ≤ T의 길이 ≤ 1000, S의 길이 < T의 길이)
  >
  > ```python
  > B
  > ABBA
  > ```
  > 
  >
  
* 출력

  > S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
  >
  > ```python
  > 1
  > ```



```python
s = input()
t = input()
slen = len(s)
tlen = len(t)

while len(s) != len(t):
    slen = len(s)
    tlen = len(t)
    if t[tlen-1] == 'A':
        t = t[:-1]
    else :
        t = t[:-1]
        t = t[::-1]
    
    
if s == t:
    print(1)
else :
    print(0)
```

> 진짜 java에서는 여러 가지 다양한 ide를 써야 해서 1시간 걸리는 문제를,, 파이썬에서는 10분만에 쉽게 풀 수 있다..
>
> 이번에 알게 된 것.
>
> * __t = t[:-1]__ : 를 통해서 t의 문자열의 마지막 문자열을 제거할 수 있다.
> * __t = t[::-1]__ : 를 통해서 t의 문자열을 뒤집을 수 있다.





* 모범답안

  ```python
  from sys import stdin
  
  
  if __name__ == "__main__":
      s, t = [list(stdin.readline().strip()) for _ in range(2)]
  
      while len(s) != len(t):
          if t[-1] == 'A':
              t.pop()
          else:
              t.pop()
              t = t[::-1]
  
      print(1 if s == t else 0)
  ```
  
  > * __[list(stdin.readline().strip()) for _ in range(2)]__
  >
  >   ```python
  >   from sys import stdin
  >   
  >   s, t = [list(stdin.readline().strip()) for _ in range(2)]
  >   
  >   print(s,t)
  >   ```
  >
  >   > ab
  >   > abba
  >   > ['a', 'b'] ['a', 'b', 'b', 'a']

