# Python

## baek 5525 IOIOI 실버2

https://www.acmicpc.net/problem/5525



> python3 360ms
>
> pypy3 144ms



* 문제

  > N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
  >
  > - P1 IOI
  > - P2 IOIOI
  > - P3 IOIOIOI
  > - PN IOIOI...OI (O가 N개)
  >
  > I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다. (1 ≤ N ≤ 1,000,000, 2N+1 ≤ M ≤ 1,000,000)
  >
  > ```bash
  >1
  > 13
  > OOIOIOIOIIOII
  > ```
  
* 출력

  > S에 PN이 몇 군데 포함되어 있는지 출력한다.
  >
  > ```bash
  > 4
  > ```



```python
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

ans, result, i = n, 0, 0        # ans에 n을 넣어줌
while i < m-2:                  # 문자열을 도는 동안에
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        # 세 칸이 'IOI'면
        ans -= 1                # IOI 개수값을 1 빼주고
        i += 1                  # 문자열 인덱스 1상승
        if ans == 0:            # 만약 원하는 IOI 개수를 채웠다면
            result += 1         # 결과값 상승
            ans += 1            # 다시 계산해야할 값 1상승
    else:                       # 만약 일치하지 않으면
        ans = n                 # IOI개수값을 초기화
    i += 1                      # 인덱스 1씩 추가

print(result)


'''
2
5
IOIOI

1
6
IOIOOI

2
20
IOIOIOIOIOIOIOIOOIOI
6
'''
```

> 계속 시간초과 났다... 주르륵,,



* 모범답안

  ```python
  188
  
N = int(input())
  M = int(input())
  S = input()
  
  def check_pattern_match(idx, s, pattern):
      for i in range(len(pattern)):
          if s[idx+i] != pattern[i]:
              return idx+i
      return idx+len(pattern)
  
  def check_additional_pattern(idx, s):
      while idx + 2 < len(s):
          if s[idx] == 'O' and s[idx+1] == 'I':
              idx += 2
          else:
              break
      return idx
  
  pattern = 'I' + 'OI'*N
  idx = 0
  answer = 0
  while idx+len(pattern) <= M:
      if S[idx] == 'I':
          ret_idx = check_pattern_match(idx,S,pattern)
          if ret_idx == idx + len(pattern):
              add_idx = check_additional_pattern(ret_idx,S)
              answer += 1 + ((add_idx - ret_idx) // 2)
              idx = add_idx
          else:
              idx = ret_idx
      else:
          idx += 1
  print(answer)
  ```
  
  > 대체 어떻게 시간을 줄인 건지 이해가 안간다. 거의 나의 1/2배인데, 어디서 시간을 줄였는지 모르겠슴.
  >
  > 내 추측으로는 두번째 함수인 check_additional_pattern이 부분 때문인 것 같은데 생각이 나아가지지 않아서 걍 나중에 볼란다..