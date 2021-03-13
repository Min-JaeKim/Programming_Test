# Python

## baek 2002 추월 골드V

https://www.acmicpc.net/problem/2002



> 100ms



* 문제

  > 대한민국을 비롯한 대부분의 나라에서는 터널 내에서의 차선 변경을 법률로 금하고 있다. 조금만 관찰력이 있는 학생이라면 터널 내부에서는 차선이 파선이 아닌 실선으로 되어 있다는 것을 알고 있을 것이다. 이는 차선을 변경할 수 없음을 말하는 것이고, 따라서 터널 내부에서의 추월은 불가능하다.
  >
  > 소문난 명콤비 경찰 대근이와 영식이가 추월하는 차량을 잡기 위해 한 터널에 투입되었다. 대근이는 터널의 입구에, 영식이는 터널의 출구에 각각 잠복하고, 대근이는 차가 터널에 들어가는 순서대로, 영식이는 차가 터널에서 나오는 순서대로 각각 차량 번호를 적어 두었다.
  >
  > N개의 차량이 지나간 후, 대근이와 영식이는 자신들이 적어 둔 차량 번호의 목록을 보고, 터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차들이 몇 대 있다는 것을 알게 되었다. 대근이와 영식이를 도와 이를 구하는 프로그램을 작성해 보자.
  
* 입력

  > 입력은 총 2N+1개의 줄로 이루어져 있다. 첫 줄에는 차의 대수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 대근이가 적은 차량 번호 목록이 주어지고, N+2째 줄부터 N개의 줄에는 영식이가 적은 차량 번호 목록이 주어진다. 각 차량 번호는 6글자 이상 8글자 이하의 문자열로, 영어 대문자('A'-'Z')와 숫자('0'-'9')로만 이루어져 있다.
  >
  > 같은 차량 번호가 두 번 이상 주어지는 경우는 없다.
  >
  > ```bash
  > 4
  > ZG431SN
  > ZG5080K
  > ST123D
  > ZG206A
  > ZG206A
  > ZG431SN
  > ZG5080K
  > ST123D
  > ```

* 출력

  > 첫째 줄에 터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차가 몇 대인지 출력한다.
  >
  > ```bash
  > 1
  > ```



```python
'''
1. 대근이와 영식이의 메모를 각각의 que에 push
2. 만약 대근[0]과 영식[0]이 일치하지 않으면,
3. 결과를 1 증가하고, 영식[0]을 pop한다음
3-1. 대근의 배열에 해당하는 값을 찾아 없애줌 (remove)

'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque([])
y = deque([])
for _ in range(n):
    d.append(input())

for _ in range(n):
    y.append(input())

result = 0
while y:
    if d[0] == y[0]:
        d.popleft()
        y.popleft()
    else:
        d.remove(y[0])
        y.popleft()
        result += 1

print(result)


'''
5
431
508
123
206
842
842
508
431
123
206
2

'''
```

> 너무 짧게 생각하고 풀었다. 조금 더 예외케이스를 생각하고 풀 것.



* 모범답안

  ```python
  64
  
  import sys
  
  def find_closest_false(check_exceed, cur):
      for i in range(cur+1,len(check_exceed)):
          if not check_exceed[i]:
              return i

  N = int(input())
  
  car_in = {}
  for i in range(N):
      car_in[sys.stdin.readline().rstrip()] = i
  
  target = 0
  answer = 0
  check_exceed = [False for _ in range(N)]
  for i in range(N):
      car_number = sys.stdin.readline().rstrip()
      if car_in[car_number] == target:
          # print('target found!')
          # print('car_number: %s, in: %d, out: %d'%(car_number, car_in[car_number],i))
          target = find_closest_false(check_exceed, target)
      else:
          check_exceed[car_in[car_number]] = True
          answer += 1
  print(answer)
  ```
  
  > 아 이래서 문제 설명에 해쉬를 이용하라고 했구나. 파이썬에서 딕셔너리를 이용하니 이렇게 빠르고 쉽게 풀 수 있군 신기. 하긴.. 나처럼 리스트안에서 해당 값을 찾고 삭제하는 것 자체가 엄청나게 시간을 소모하는 로직이다.