# python

## baek 9935 문자열 폭발 골드4

https://www.acmicpc.net/problem/9935

> python3 412ms



* 문제

  > 상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.
  >
  > 폭발은 다음과 같은 과정으로 진행된다.
  >
  > - 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
  > - 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
  > - 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
  >
  > 상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.
  >
  > 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
  
* 입력

  > 첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
  >
  > 둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
  >
  > 두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.
  >
  > ```bash
  > mirkovC4nizCC44
  > C4
  > ```
  >
  
* 출력

  > 첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
  >
  > ```bash
  > mirkovniz
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    a = list(input().strip())
    b = list(input().strip())
    stack = []
    n, m, i = len(a), len(b), 0

    while i < n:
        stack.append(a[i])
        if stack[-m:] == b:
            del stack[-m:]
        i += 1

    print(''.join(stack) if len(stack) >= 1 else 'FRULA')


sol()
```

> 하,, stack을 쓰긴 했는데 다른 스택을 통해서 재할당 해주고 또 다시 처음부터 돌고 그러다 보니까 시간초과가 났다.. 48퍼쯤에!!
>
> 그래서 누가 del연산자 써보라길래 del 써봤더니 5%에서 시간초과남 ㅋㅋ
>
> 결국 이렇게 하는 거였는데, 이대로 하면 처음부터 끝까지 n번만 볼 수 있다.



* 모범답안

  ```python
  240
  
  def main():
      string = input().strip()
      bomb = input().strip()
      bombl = list(bomb)
      b_last = bomb[-1]
      bl = len(bomb)
  
      ans = []
      for l in string:
          ans.append(l)
          if b_last == l and bombl == ans[-bl:]:
              del ans[-bl:]
  
      print(''.join(ans) if ans else "FRULA")
  
  
  if __name__ == '__main__':
      main()
  ```
  
  > 문자열로 하셧군 문자열로 하면 엄청 빠르다. 글고 마지막 문자열이 같을 때에만 슬라이싱을 비교하게 해줬기 때문에 더 단축시킬 수 있음

