# python

## baek 2138 전구와 스위치 실버2

https://www.acmicpc.net/problem/2138

> python3 ms
>
> pypy3 ms



* 문제

  > N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는(1) 상태와 꺼져 있는 (0) 상태 중 하나의 상태를 가진다. i(1<i<N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.
  >
  > N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 자연수 N(2≤N≤100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다.
  >
  > ```bash
  > 
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

