# python

## baek 1406 에디터 실버3

https://www.acmicpc.net/problem/1406

> python3 320ms
>
> pypy3 276ms



* 문제

  > 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
  >
  > 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
  >
  > 이 편집기가 지원하는 명령어는 다음과 같다.
  >
  > | L    | 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)  |
  > | :--- | ------------------------------------------------------------ |
  > | D    | 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨) |
  > | B    | 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨) 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임 |
  > | P $  | $라는 문자를 커서 왼쪽에 추가함                              |
  >
  > 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

* 입력

  > 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.
  >
  > ```bash
  > abcd
  > 3
  > P x
  > L
  > P y
  > ```
  > 
  
* 출력

  > 첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
  >
  > ```bash
  > abcdyx
  > ```



```python
'''
스택을 두 개 만들어서 풀기.
커서가 왼쪽으로 움직일 때마다 스택1을 팝하여 스택2에 푸시하고
반대로 오른쪽으로 움직일 때마다 스택2을 팝하여 스택1에 푸시.

'''
import sys


def sol():
    st1 = list(sys.stdin.readline().strip())
    st2 = []

    for _ in range(int(sys.stdin.readline())):
        c = sys.stdin.readline().strip()
        if len(c) > 2:
            p, string = c.split(' ')
            st1.append(string)
        elif c == 'L':
            if st1:
                st2.append(st1.pop())
        elif c == 'D':
            if st2:
                st1.append(st2.pop())
        elif c == 'B':
            if st1:
                st1.pop()

    print(''.join(st1) + ''.join(reversed(st2)))


sol()
```

> 

* 모범답안

  ```python
  from sys import stdin
  l = stdin.read().rstrip().split("\n")
  txt_l = list(l[0])
  txt_r = []
  l = l[2:]
  
  for o in l:
      if o[0] == "P":
          txt_l.append(o[2])
      elif o=="L" and txt_l:
              txt_r.append(txt_l.pop())
      elif o=="D" and txt_r:
              txt_l.append(txt_r.pop())
      elif o=="B" and txt_l:
              txt_l.pop()
  
  print("".join(txt_l)+"".join(txt_r[::-1]))
  ```

  > 이게 뭔말인가 했는데 애초에 모든 입력을 한 줄 띄어쓰기로 구분한 거였음.. 그 모든 입력을 l에서 담았고 그걸 for문으로 돌려 시간 최적화를 노린거임... 
  >
  > 나는 스택 두 개 쓰는 방법도 몰랐는데 이렇게 최적화하는 방법이 있다는 것에 한 번 더 놀람,,

