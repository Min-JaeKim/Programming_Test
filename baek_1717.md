# python

## baek 1717 집합의 표현 골드4

https://www.acmicpc.net/problem/1717

> python3 480ms



* 문제

  > 초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
  >
  > 집합을 표현하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 n(1 ≤ n ≤ 1,000,000), m(1 ≤ m ≤ 100,000)이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다. a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.
  >
  > ```bash
  > 7 8
  > 0 1 3
  > 1 1 7
  > 0 7 6
  > 1 7 1
  > 0 3 7
  > 0 4 2
  > 0 1 1
  > 1 1 1
  > ```
  >
  
* 출력

  > 1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력한다. (yes/no 를 출력해도 된다)
  >
  > ```bash
  > NO
  > NO
  > YES
  > ```



```python
import sys
sys.setrecursionlimit(999999)
input = sys.stdin.readline


def sol():

    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            p[a] = b
        else:
            p[b] = a

    def find(c):
        if c == p[c]:
            return c
        p[c] = find(p[c])
        return p[c]

    n, m = map(int, input().split())
    p = [i for i in range(n+1)]

    for _ in range(m):
        flag, a, b = map(int, input().split())

        if not flag:
            if find(a) != find(b):
                union(a, b)
        else:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')

    print(p)


sol()
```

> union find 를 다시 외워야 할 필요성을 느꼈다. 배운지 오래되면서 내 기억이 왜곡된 부분이 많았던 듯.



* 모범답안

  ```python
  244
  
  import sys
  
  input = sys.stdin.readline
  
  
  def sol1717():
      n, m = map(int, input().split())
      u = [-1] * (n + 1)
  
      answer = []
      for _ in range(m):
          t, a, b = map(int, input().split())
          if t:
              answer.append('YES' if find(u, a) == find(u, b) else 'NO')
          else:
              union(u, a, b)
              
      return '\n'.join(answer)
  
  
  def union(u, a, b):
      a = find(u, a)
      b = find(u, b)
      if a != b:
          if u[a] < u[b]:
              u[a] += u[b]
              u[b] = a
          else:
              u[b] += u[a]
              u[a] = b
  
  
  def find(u, x):
      if u[x] < 0:
          return x
      u[x] = find(u, u[x])
      return u[x]
  
  
  if __name__ == '__main__':
      print(sol1717())
  ```
  
  > flag가 0일 때 부모가 일치하는 지 확인하느 코드가 없군

