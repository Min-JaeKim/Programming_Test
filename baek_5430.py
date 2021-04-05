# python

## baek 5430 AC 실버2

https://www.acmicpc.net/problem/5430



> 184ms



* 문제

  > 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
  >
  > 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
  >
  > 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.
  >
  > 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
  >
  > 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
  >
  > 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
  >
  > 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)
  >
  > 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
  >
  > ```python
  > 4
  > RDD
  > 4
  > [1,2,3,4]
  > DD
  > 1
  > [42]
  > RRD
  > 6
  > [1,1,2,3,5,8]
  > D
  > 0
  > []
  > ```
  >
  > 

* 출력

  > 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
  >
  > ```python
  > [2,1]
  > error
  > [1,2,3,5,8]
  > error
  > ```



```python
import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    p = list(input().rstrip())     # 'RDD'
    gbg = int(input().rstrip())    # 4
    num = input().rstrip()[1:-1].split(',')
    # ['1','2','3','4']

    flag, l, r = True, 0, 0     # 뒤를 뺄 지 앞을 뺄 지 계산하는 flag, 왼쪽, 오른쪽
    for i in p:                 # 'RDD'를 돌면서
        if i == 'R':            # R이면
            flag = not flag     # 현재 flag 반대로,,
        elif i == 'D':          # D면
            if flag:            # 왼쪽 빼는 거
                l += 1
            else:               # 오른쪽 빼는 거
                r += 1
    if l+r <= gbg:              # 뺀 길이가 문자열 길이보다 짧거나 같다면
        num = num[l:gbg-r]      # 앞과 뒤를 빼주고
        if flag:                # reverse된 상태가 아니라면
            print('[' + ','.join(num) + ']')    # 출력
        else:                   # reverse된 상태라면
            print('[' + ','.join(num[::-1]) + ']')  # 뒤집고 출력
    else:                       # 문자열보다 많이 뺐다면
        print('error')          # 에러
```

> 2.  휴,, 많이 발전해야겠다 나,, 진짜 왜이러냐 요즘



* 모범답안

  ```python
  from sys import stdin, stdout
  def AC(com,n, li):
      com.replace('RR', '')
      l, r, d = 0, 0, True
      for c in com:
          if c == 'R': d = not d
          elif c == 'D':
              if d: l += 1
              else: r += 1
      if l+r <= n:
          res = li[l:n - r]
          if d: return '[' + ','.join(res) + ']\n'
          else: return '[' + ','.join(res[::-1]) + ']\n'
      else:
          return 'error\n'
  
  T = int(stdin.readline())
  for _ in range(T):
      com = stdin.readline()
      n = int(stdin.readline())
      li = stdin.readline().rstrip()[1:-1].split(',')
      if n == 0 : []
      stdout.write(AC(com, n, li))
  ```

  > - com.replace('RR', '') : R이 두 개 나오면 똑같으므로 대체
  > - `return '[' + ','.join(res) + ']\n'` : JOIN은 문자열만 가능하므로 주의할 것,,
  > - `d = not d` : FALSE -> TRUE, TRUE -> FALSE
  > - `stdin.readline().rstrip()[1:-1].split(',')`
  >   - rstrip으로 readline을 통해 들어온 공백 제거.
  >   - [1:-1]을 통해 양 옆 괄호 제거
  >   - 쉼표로 문자열들 나누기