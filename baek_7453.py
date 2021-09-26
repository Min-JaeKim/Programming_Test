# python

## baek 7453 합이 0인 네 정수 골드2

https://www.acmicpc.net/problem/7453

> pypy3 10860ms

* 문제

  > 정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.
  >
  > A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 배열의 크기 n (1 ≤ n ≤ 4000)이 주어진다. 다음 n개 줄에는 A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어진다. 배열에 들어있는 정수의 절댓값은 최대 228이다.
  >
  > ```bash
  > 6
  > -45 22 42 -16
  > -41 -27 56 30
  > -36 53 -37 77
  > -36 30 -75 -46
  > 26 -38 -10 62
  > -32 -54 -6 45
  > ```
  >
  
* 출력

  > 합이 0이 되는 쌍의 개수를 출력한다.
  >
  > ```bash
  > 5
  > ```



- 

```python

# 둘 둘 쪼개서 계산.
# cd 더한 것의 반대 부호를 가진 수가 ab 더한 리스트에 있으면 됨


import sys
from collections import defaultdict
input = sys.stdin.readline


def sol():
    n = int(input())
    arr1, arr2, arr3, arr4 = [], [], [], []
    res = 0

    for _ in range(n):
        a, b, c, d = map(int, input().split())
        arr1.append(a)
        arr2.append(b)
        arr3.append(c)
        arr4.append(d)

    ab = defaultdict(int)

    for i in range(n):
        for j in range(n):
            ab[arr1[i] + arr2[j]] += 1

    for i in range(n):
        for j in range(n):
            res += ab.get(-(arr3[i] + arr4[j]), 0)

    print(res)


sol()
```

> 우엥 어려웠다. 이렇게 4개의 for문을 돌려야 할 때는 둘 둘 나눠서 한다음 반대 부호가 있는 것만 확인해 주면 되는구나 흑흑



* 모범답안

  ```python
  4024
  
  import sys
  
  input = sys.stdin.readline
  
  
  def main(n):
      a.sort()
      b.sort()
      ab = [i + j for i in a for j in b]
      ab.sort()
      ab.append((1 << 29) + 2)
      c.sort(reverse=True)
      d.sort(reverse=True)
      cd = [i + j for i in c for j in d]
      cd.sort(reverse=True)
      cd.append((1 << 29) + 1)
      i = j = 0
      k = n * n
      res = 0
      while (i < k and j < k):
          m = ab[i] + cd[j]
          if (m > 0):
              j += 1
          elif (m < 0):
              i += 1
          else:
              u, v = ab[i], cd[j]
              p = i
              q = j
              while (u == ab[i]): i += 1
              while (v == cd[j]): j += 1
              res += (i - p) * (j - q)
  
      return res
  
  
  if __name__ == '__main__':
      n = int(input())
      a, b, c, d = [], [], [], []
      for _ in range(n):
          v, w, x, y = map(int, input().split())
          a.append(v)
          b.append(w)
          c.append(x)
          d.append(y)
      print(main(n))
  ```

  > 투포인터를 쓰셨다 그래서 빠름.
  >
  > 그런데 중간에 비트 연산자를 넣었는데 최댓값을 나타내는 것인 건 알겠다. 그런데 왜 저게 필요한지 잘 모르겠음.. 막상 저 코드 ㅃㅐ고 돌리면 인덱스에러 뜨는데 원인을 모르겠당

