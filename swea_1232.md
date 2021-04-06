# python

## swea 1232 d4 사칙연산

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD



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
def order(k):
    global arr
    if arr[k][1] == '+':
        arr[k][1] = str(order(int(arr[k][2])) + order(int(arr[k][3])))
    elif arr[k][1] == '-':
        arr[k][1] = str(order(int(arr[k][2])) - order(int(arr[k][3])))
    elif arr[k][1] == '*':
        arr[k][1] = str(order(int(arr[k][2])) * order(int(arr[k][3])))
    elif arr[k][1] == '/':
        arr[k][1] = str(order(int(arr[k][2])) // order(int(arr[k][3])))
    return int(arr[k][1])

for tc in range(1, 11):
    n = int(input())
    arr = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        arr[i] = input().split()
    # print(*arr)
    order(1)
    res = int(arr[1][1])
    print('#%d %d' % (tc, res))
```

> 뭐,, 나는 내풀이 나쁘지 않다고 생각해.





* 모범답안

  ```python
  def calculation(a, b, c):
      if c == '+':
          return a+b
      elif c == '-':
          return a-b
      elif c == '*':
          return a*b
      else:
          return a/b
   
  t = 10
   
  for tc in range(1, t+1):
      N = int(input())
      tree = [0] * (N+1)
   
      operator = ['+', '-', '/', '*']
      operation = []
   
      for _ in range(N):
          a = input().split()
          if a[1] in operator:
              operation.append(a)
          else:
              tree[int(a[0])] = int(a[1])
   
      for i in reversed(operation):
          tree[int(i[0])] = calculation(tree[int(i[2])], tree[int(i[3])], i[1])
   
   
      print(f'#{tc} {int(tree[1])}')
  ```
  
  > 멋지네 진짜,, 한 수 배워갑니다. reversed함수를 써서 밑 노드부터 순차적으로 계산해 나갔다. for문을 저렇게 쓸 수도 있구나 신기.