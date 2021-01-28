# Python

## baek 10828

https://www.acmicpc.net/problem/10828



> 164ms



* 문제

  > 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
  >
  > 명령은 총 다섯 가지이다.
  >
  > - push X: 정수 X를 스택에 넣는 연산이다.
  > - pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  > - size: 스택에 들어있는 정수의 개수를 출력한다.
  > - empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
  > - top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

* 입력

  > 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
  >
  > ```python
  > 14
  > push 1
  > push 2
  > top
  > size
  > empty
  > pop
  > pop
  > pop
  > size
  > empty
  > pop
  > push 3
  > empty
  > top
  > ```
  >

* 출력

  > 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
  >
  > ```python
  > 2
  > 2
  > 0
  > 2
  > 1
  > -1
  > 0
  > 1
  > -1
  > 0
  > 3
  > ```



```python
import sys

stack = []
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    if order == "push":
        num = input_split[1]
        stack.append(num)
    elif order == "pop":
        if len(stack) == 0 :
            print(-1)
            continue
        print(stack[len(stack)-1])
        del stack[len(stack)-1]
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif order == "top":
        if len(stack) == 0 :
            print(-1)
            continue
        print(stack[len(stack)-1])
```

> 허무,,, 파이썬은 비교적 엄청 쉽게 풀렸다.
>
> * import sys
> * __int(sys.stdin.readline().rstrip())__ : 한 줄에 여러 값을 입력 받기.
> * __rstrip()__ : 오른쪽 공백 제거, (lstrip() : 왼쪽 공백 제거, strip() : 양쪽 공백 제거)
> * __sys.stdin.readline().rstrip().split()__ : 오른쪽 공백을 제거하고 여러 가지를 입력 받기. 



* 모범답안

  ```python
  mport sys
  
  # 정수 X를 스택에 넣는 연산이다.
  def push(x):
      stack.append(x)
  
  # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
  # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  def pop():
      if(not stack):
          return -1
      else:
          return stack.pop()
  
  # 스택에 들어있는 정수의 개수를 출력한다.
  def size():
      return len(stack)
  
  # 스택이 비어있으면 1, 아니면 0을 출력한다.
  def empty():
      return 0 if stack else 1
  
  # 스택의 가장 위에 있는 정수를 출력한다. 
  # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  def top():
      return stack[-1] if stack else -1
  
  N = int(sys.stdin.readline().rstrip())
  stack = []

  for _ in range(N):
      input_split = sys.stdin.readline().rstrip().split()
  
      order = input_split[0]
  
      if order == "push":
          push(input_split[1])
      elif order == "pop":
          print(pop())
      elif order == "size":
          print(size())
      elif order == "empty":
          print(empty())
      elif order == "top":
          print(top())
  ```
  
  > 별 수 없이 함수로 입력 받아야 하는 듯,, 파이썬 스택이 제공하는 함수들,,
  >
  > * __not stack__
  > * __stack.pop()__
  > * __len(stack)__
  > * __return 0 if stack else 1__ : stack이 비어 있으면 1, 아니면 0
  > * __return stack[-1] if stack else -1__ : stack이 있으면 꼭대기를 출력하고 아니면, -1 출력.
  > * 