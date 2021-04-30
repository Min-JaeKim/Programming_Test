# python

## baek 9461 파도반 수열 실버3

https://www.acmicpc.net/problem/9461

> python3 68ms
>
> pypy3 120ms



* 문제

  > 오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.
  >
  > 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.
  >
  > N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)
  >
  > ```python
  > 2
  > 6
  > 12
  > ```
  >
  > 

* 출력

  > 각 테스트 케이스마다 P(N)을 출력한다.
  >
  > ```python
  > 3
  > 16
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    t = int(input())
    for _ in range(t):
        dp = [0, 1, 1, 1, 2, 2]
        n = int(input())
        if n < len(dp):
            print(dp[n])
            continue
        for i in range(n-len(dp)+1):
            dp.append(dp[-1] + dp[-5])
        print(dp[-1])

sol()
```

> 처음에 while문으로해서 틀렸다.. 왜틀렸는지는 사실 잘 모름,, 근데 for문이 더 직관적이라서 코드를 바꿨다.



* 모범답안

  ```python
  54
  import sys
  
  T = int(sys.stdin.readline())
  
  arr = [0] * 100
  arr[0] = 1
  arr[1] = 1
  arr[2] = 1
  arr[3] = 2
  arr[4] = 2
  arr[5] = 3
  
  for i in range(6, 100):
      arr[i] = arr[i - 2] + arr[i - 3]
  
  for _ in range(T):
      N = int(sys.stdin.readline())
      print(arr[N - 1])
  ```

  > 내가 놓쳤던 부분이 있었다.. n은 최댓값이 100이라는 점.. 그렇기에 미리 100까지 만들어 놓고 testcase만큼 값을 출력하면 됨

