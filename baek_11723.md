# python

## baek 11723 집합 실버5

https://www.acmicpc.net/problem/3649

> python3 3540ms

* 문제

  > 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
  >
  > - `add x`: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
  > - `remove x`: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
  > - `check x`: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
  > - `toggle x`: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
  > - `all`: S를 {1, 2, ..., 20} 으로 바꾼다.
  > - `empty`: S를 공집합으로 바꾼다. 

* 입력

  > 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
  >
  > 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
  >
  > ```bash
  > 26
  > add 1
  > add 2
  > check 1
  > check 2
  > check 3
  > remove 2
  > check 1
  > check 2
  > toggle 3
  > check 1
  > check 2
  > check 3
  > check 4
  > all
  > check 10
  > check 20
  > toggle 10
  > remove 20
  > check 10
  > check 20
  > empty
  > check 1
  > toggle 1
  > check 1
  > toggle 1
  > check 1
  > ```
  >
  
* 출력

  > `check` 연산이 주어질때마다, 결과를 출력한다.
  >
  > ```bash
  > 1
  > 1
  > 0
  > 1
  > 0
  > 1
  > 0
  > 1
  > 0
  > 1
  > 1
  > 0
  > 0
  > 0
  > 1
  > 0
  > ```



- 

```python
import sys
input = sys.stdin.readline


def sol():
    v = [0 for _ in range(21)]
    m = int(input())

    for _ in range(m):
        order = input().strip()
        if order == 'all' or order == 'empty':
            com = order
        else:
            com, x = order.split()
            x = int(x)

        if com == 'add':
            v[x] = 1
        elif com == 'remove':
            v[x] = 0
        elif com == 'check':
            if v[x]:
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            if v[x]:
                v[x] = 0
            else:
                v[x] = 1
        elif com == 'all':
            for i in range(1, 21):
                v[i] = 1
        else:
            for i in range(1, 21):
                v[i] = 0


sol()
```

> 아 실1인줄알았는데 실5넹 다른 문제 푸러야겠다
>
> 이문제 처음에 계속 에러났던 건 readline으로 받을 때 맨 끝에 공백도 받기 때문.
>
> 따라서 strip 으로 잘라줘야 함.



* 모범답안

  ```python
  2068
  
  import sys
  
  
  def solve():
      read = sys.stdin.readline
      m = int(read())
      all_s = [str(i) for i in range(1, 21)]
      s = []
      div = 520912
      for i in range(m // div):
          ans = []
          for _ in range(div):
              cmd = read().split()
              if cmd[0] == 'add':
                  if cmd[1] not in s:
                      s.append(cmd[1])
              if cmd[0] == 'remove':
                  if cmd[1] in s:
                      s.remove(cmd[1])
              if cmd[0] == 'check':
                  ans.append('1' if cmd[1] in s else '0')
              if cmd[0] == 'toggle':
                  if cmd[1] in s:
                      s.remove(cmd[1])
                  else:
                      s.append(cmd[1])
              if cmd[0] == 'all':
                  s = all_s
              if cmd[0] == 'empty':
                  s = []
          print('\n'.join([i for i in ans]))
      ans = []
      for _ in range(m % div):
          cmd = read().split()
          if cmd[0] == 'add':
              if cmd[1] not in s:
                  s.append(cmd[1])
          if cmd[0] == 'remove':
              if cmd[1] in s:
                  s.remove(cmd[1])
          if cmd[0] == 'check':
              ans.append('1' if cmd[1] in s else '0')
          if cmd[0] == 'toggle':
              if cmd[1] in s:
                  s.remove(cmd[1])
              else:
                  s.append(cmd[1])
          if cmd[0] == 'all':
              s = all_s
          if cmd[0] == 'empty':
              s = []
      print('\n'.join([i for i in ans]))
  
  
  solve()
  
  ```

  > 희한하다  `div = 520912` 이게 뭔 숫자인지 모르겠음.. 이게 핵심적인 숫자 같긴 한데 모르겠다

