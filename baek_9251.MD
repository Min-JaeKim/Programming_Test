# python

## baek 9251 LCS 골드5

https://www.acmicpc.net/problem/9251

> python3 524ms

* 문제

  > LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
  >
  > 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

* 입력

  > 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
  >
  > ```bash
  > ACAYKP
  > CAPCAK
  > ```
  >
  
* 출력

  > 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
  >
  > ```bash
  > 4
  > ```



- 

```python
def sol():
    a = input()
    b = input()
    n1, n2 = len(a), len(b)
    dp = [[0] * (n2+1) for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n1][n2])


sol()
```

> dp를 이용해 LCS를 풀었다. 어렵다. 뭔말인지 몰라서 손으로 시뮬레이션을 계속 돌렸다



* 모범답안

  ```python
  64
  
  a=input()
  b=input()
  T=[0]*300
  row=0
  X=0
  al = len(a)
  bl = len(b)
  for i in range(al):
      T[ord(a[i])]+=(2**i)
  for i in range(al):
      if(a[i]==b[0]):
          row+=(2**i)
          break
  for i in range(1, bl):
      X = T[ord(b[i])]|row
      row=X&((X-(row*2+1))^X)
  
  cnt = 0
  while(row):
      cnt+=(row%2)
      row//=2
  
  print(cnt)
  ```

  > 몰라,, 비트연산자 이해 못하겠어

