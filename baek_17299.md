# Python

## baek 17299 오등큰수

https://www.acmicpc.net/problem/17299



> 1012ms



* 문제

  > 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.
  >
  > Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오등큰수는 -1이다.
  >
  > 예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다. A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다. A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.

* 입력

  > 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
  >
  > ```python
  > 7
  > 1 1 2 3 4 2 1
  > ```
  >

* 출력

  > 총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
  >
  > ```python
  > -1 -1 1 2 2 1 -1
  > ```



```python
N = int(input()) // 
arr = list(map(int, input().split()))
fre = [0 for _ in range(max(arr) + 1)]
stack = [0]
result = [-1 for _ in range(N)]

for i in arr:
    fre[i] += 1

for i in range(len(arr)):
    while stack and fre[arr[stack[-1]]] < fre[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

for i in result:
    print(i,end =" ")

# 횟수를 다 저장하고
# for
# if 스택이 비어있다면
#   스택[fre[arr[i]]]
# arr = 1 1 2 3 4 2 1
# fre = 0 3 2 1 1
# stack = 0 1 2 5
# i = 6
# result = -1 -1 -1 2 2

# 4 1 1 2 3 1 2
# 1 -1 -1 1 1 -1 -1
```

> 내가,,, 오등큰수를 풀기 위해,,, 오큰수를 풀었던 md도 끄지 않고 계속 기다리고 있었다............... 드디어 오등큰수를 풀었다.
>
> 내가 주말에 오등큰수 풀이 시작부터 목요일 스터디 때까지 풀지 못했던 이유는 오등큰수 문제 이해를 제대로 하지 못했기 때문이다. 바보 같은 나 ㅜㅜㅜㅜ,,, 제발 확신이 들더라도 문제를 여러 번 읽어 보는 것을 명심해야한다.
>
> 그리고 한 가지 더, 런타임에러 indexerror가 나길래 뭘까 했는데 해답은 frequent 리스트에 있었다. 크기는 N으로 잡는 게 아니라 수들의 가장 큰 수를 크기로 잡는 것이다.



* 모범답안

  ```python
  num = int(input())
  a = list(map(int, input().split(" ")))
  result = ["-1" for _ in range(num)]
  stack = [0]
  count = dict()
  for i in a:
      try:
          count[i] += 1
      except:
          count[i] = 1
  
  for i in range(num):
      while stack and count[a[stack[-1]]] < count[a[i]]:
          result[stack[-1]] = str(a[i])
          stack.pop()
      stack.append(i)
      i+=1
  
  print(" ".join(result))
  
  #932ms
  ```

  > 출력때문인건지 나보다 시간이 적게 나왔다. 이사람은 result를 문자열로 표기했다.