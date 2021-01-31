# Python

## baek 17298 오큰수

https://www.acmicpc.net/problem/17298



> 976ms



* 문제

  > 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
  >
  > 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

* 입력

  > 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
  >
  > ```python
  > 4
  > 3 5 2 7
  > ```
  >

* 출력

  > 총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
  >
  > ```python
  > 5 7 7 -1
  > ```



```python
t = int(input())
num = list(map(int, input().split()))
index = []
result = [-1 for _ in range(t)]

for i in range(t):
    if not index:
        index.append(i)
        continue
    else:
        while num[i] > num[index[len(index) - 1]]:
            result[index.pop()] = num[i]
            if not index:
                break
        index.append(i)
        
for i in range(t):    
    print(result[i], end = ' ')
```

> 시간이 왜인지 오래 걸렸다. 스택문제인데 스택으로 안풀고 단순하게 풀다가 고생했던 문제이다. 결국 인덱스를 사용하는 문제라는 것을 알아냈는데 런타임 에러가 나서 else문에 if 문을 추가함으로써 해결할 수 있었다. 저 부분은 약간 끼워맞추기식 코드라 미관상 별로 예뻐 보이지는 않는다.. 근데 추가로 요즘 백준 왜이렇게 채점하는데 시간 오래 걸리는 지 모르겠다.
>
> 그리고 추가로 in not index ~ continue를 하면 while문을 계속 돌게 되고(그러니까 돌고 있던 반복문을 빠져나가 바로 앞에 있는 반복문을 계속 돈다.) 
>
> if not index ~ break를 하면 다 빠져나가 첫 번째 반복문인 for문을 돌게 된다.



* 계속 틀렸던 답안

  ```python
  t = int(input())
  num = list(map(int, input().split()))
  result = []
  max_v = num[0]
  
  for i in range(t):
      max_v = num[i]
      for j in range(i,t):
          if max_v < num[j]:
              max_v = num[j]
              break
      if max_v == num[i]:
          result.append(-1)
      else:
          result.append(max_v)
          
  for i in range(t):    
      print(result[i], end = ' ')
  ```

  > 틀렸습니다가 자꾸 떴던 이유는 출력을 for문으로 안돌렸기 때문인데, for문으로 돌리니까 그제서야 시간초과 떴다. 하여튼간에,, 1초 짜리 문제를 이중 for문을 썼는데 시간 초과 나오지 않는 게 이상하다..



* 모범답안

  ```python
  numbers = int(input())
  num_list = list(map(int, input().split()))
  stack = []
  result = [-1 for _ in range(numbers)]
  
  for i in range(len(num_list)):
      try:
          while num_list[stack[-1]] < num_list[i]:
              result[stack.pop()] = num_list[i]
      except:
          pass
          
      stack.append(i)
          
  for i in range(numbers):
      print(result[i], end = ' ')
  ```

  > 짱 멋진 코드를 찾았는데 이 코드는 try ~ except를 사용해서 엄청 멋져 보인다. 하지만 시간은 나보다 살짝 더 오래 걸리는 정도이다.