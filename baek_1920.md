# python

## baek 1920 수 찾기 실버4

https://www.acmicpc.net/problem/1920

> python3 644ms

* 문제

  > N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
  >
  > ```bash
  > 5
  > 4 1 5 2 3
  > 5
  > 1 3 7 9 5
  > ```
  >
  
* 출력

  > M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
  >
  > ```bash
  > 1
  > 1
  > 0
  > 0
  > 1
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    m = int(input())
    t = list(map(int, input().split()))
    for tmp in t:
        left, right, flag = 0, n, False

        while left < right:
            mid = (left + right) // 2

            if tmp == arr[mid]:
                flag = True
                print(1)
                break

            if tmp <= arr[mid]:
                right = mid

            else:
                left = mid + 1

        if not flag:
            print(0)


sol()
```

> 이진탐색 까먹어서 아주아주 쉬운 문제로 풀어 보았다.
>
> right는 반드시 n으로 둬야함. 어차피 //2 를 하면서 작은 정수가 mid값에 들어가기 때문



* 모범답안

  ```python
  120
  
  import sys
  input = sys.stdin.readline
  
  def BOJ_1920():
      n,A,m = input(),set(input().split()),input()
      res=""
      for i in input().split():
          res += "1\n" if i in A else "0\n"
      print(res)
  BOJ_1920()
  ```

  > 아 대박 ㅋㅋㅋㅋ 
  >
  > set 시간복잡도가 O(1)이었지 대박이넹 .. ㅋㅋ.ㅋ...... 굿

