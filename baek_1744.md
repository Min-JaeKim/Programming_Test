# python

## baek 1744 수 묶기 골드4

https://www.acmicpc.net/problem/1744

> python3 88ms
>



* 문제

  > 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.
  >
  > 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.
  >
  > 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
  >
  > 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 수열의 크기 N이 주어진다. N은 10,000보다 작은 자연수이다. 둘째 줄부터 N개의 줄에, 수열의 각 수가 주어진다. 수열의 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
  >
  > ```bash
  >4
  > -1
  >2
  > 1
  > 3
  > ```
  > 
  
* 출력

  > 수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.
  >
  > ```bash
  > 6
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    res, idx, neg, pos, one, zero = [], 0, [], [], 0, 0

    for a in arr:
        if a == 1:
            one += 1
        elif a > 0:
            pos.append(a)
        elif a < 0:
            neg.append(a)
        else:
            zero = 1

    pos.sort(reverse=True)
    neg.sort()
    pos, neg = deque(pos), deque(neg)

    for i in range(0, len(pos), 2):
        if len(pos) == 1:
            break
        num1, num2 = pos.popleft(), pos.popleft()
        res.append(num1 * num2)

    for i in range(0, len(neg), 2):
        if len(neg) == 1:
            break
        num1, num2 = neg.popleft(), neg.popleft()
        res.append(num1 * num2)

    if pos:
        res.append(pos[0])
    if neg:
        if zero:
            pass
        else:
            res.append(neg[0])
    if one:
        res.append(one)

    print(sum(res))


sol()
```

> 어떻게 풀어야 하는지 고민했던 것 조차 시간 아까웠던 문제. 양수랑 음수랑 0혹은 1과 나누면 되는데 그걸 못해서 고민을 한참했다. 어이가 없다 ㅋㅋㅋㅋㅋㅋㅋ



* 모범답안

  ```python
  56
  
  import sys
  n = int(input())
  arr1 = []
  arr2 = []
  arr3 = []
  ret =0 
  for _ in range(n):
      x = int(sys.stdin.readline())
      if x<1: arr1.append(x)        
      elif x>1:arr2.append(x)
      else: arr3.append(x)
  arr1.sort()
  arr2.sort()
  for i in range(0,len(arr1)-1,2):
      ret+=arr1[i]*arr1[i+1]
  if len(arr1)%2 == 1: ret+=arr1[-1]
  for i in range(len(arr2)-1,0,-2):
      ret+=arr2[i]*arr2[i-1]
  if len(arr2)%2 == 1: ret+=arr2[0]
  ret+=sum(arr3)
  print(ret)
  ```
  
  > 내가 불필요한 연산을 많이 넣었나보다.

