# python

## baek 14725 개미굴 골드2

https://www.acmicpc.net/problem/14725

> python3 564ms

* 문제

  > 개미는(뚠뚠) 오늘도(뚠뚠) 열심히(뚠뚠)  일을 하네.
  >
  > 개미는 아무말도 하지 않지만 땀을 뻘뻘 흘리면서 매일 매일을 살길 위해서 열심히 일을 하네.
  >
  > 한 치 앞도(뚠뚠) 모르는(뚠뚠) 험한 이 세상(뚠뚠) 그렇지만(뚠뚠) 오늘도 행복한 개미들!
  >
  > 우리의 천재 공학자 윤수는 이 개미들이 왜 행복한지 궁금해졌다.
  >
  > 행복의 비결이 개미가 사는 개미굴에 있다고 생각한 윤수는 개미굴의 구조를 알아보기 위해 로봇 개미를 만들었다.
  >
  > 로봇 개미는 센서가 있어 개미굴의 각 층에 먹이가 있는 방을 따라 내려가다 더 이상 내려갈 수 없으면 그 자리에서 움직이지 않고 신호를 보낸다.
  >
  > 이 신호로 로봇 개미는 개미굴 각 층을 따라 내려오면서 알게 된 각 방에 저장된 먹이 정보를 윤수한테 알려줄 수 있다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/1.png)
  >
  > 로봇 개미 개발을 완료한 윤수는 개미굴 탐사를 앞두고 로봇 개미를 테스트 해보기 위해 위 그림의 개미굴에 로봇 개미를 투입했다. (로봇 개미의 수는 각 개미굴의 저장소를 모두 확인할 수 있을 만큼 넣는다.)
  >
  > 다음은 로봇 개미들이 윤수에게 보내준 정보다.
  >
  > - KIWI BANANA
  > - KIWI APPLE
  > - APPLE APPLE
  > - APPLE BANANA KIWI
  >
  > (공백을 기준으로 왼쪽부터 순서대로 로봇 개미가 각 층마다 지나온 방에 있는 먹이 이름을 뜻한다.)
  >
  > 윤수는 로봇 개미들이 보내준 정보를 바탕으로 다음과 같이 개미굴의 구조를 손으로 그려봤다.
  >
  > ```
  > APPLE
  > --APPLE
  > --BANANA
  > ----KIWI
  > KIWI
  > --APPLE
  > --BANANA
  > ```
  >
  > (개미굴의 각 층은 "--" 로 구분을 하였다.
  >
  > 또 같은 층에 여러 개의 방이 있을 때에는 사전 순서가 앞서는 먹이 정보가 먼저 나온다.)
  >
  > 우리의 천재 공학자 윤수는 복잡한 개미굴들을 일일이 손으로 그리기 힘들어 우리에게 그려달라고 부탁했다.
  >
  > 한치 앞도 모르는 험한 이세상 그렇지만 오늘도 행복한 개미들!
  >
  > 행복의 비결을 알기 위해 윤수를 도와 개미굴이 어떤 구조인지 확인해보자.

* 입력

  > 첫 번째 줄은 로봇 개미가 각 층을 따라 내려오면서 알게 된 먹이의 정보 개수 N개가 주어진다.  (1 ≤ N ≤ 1000)
  >
  > 두 번째 줄부터 N+1 번째 줄까지, 각 줄의 시작은 로봇 개미 한마리가 보내준 먹이 정보 개수 K가 주어진다. (1 ≤ K ≤ 15)
  >
  > 다음 K개의 입력은 로봇 개미가 왼쪽부터 순서대로 각 층마다 지나온 방에 있는 먹이 정보이며 먹이 이름 길이 t는 (1 ≤ t ≤ 15) 이다. 
  >
  > ```bash
  > 2
  > 3 A B C
  > 4 A B C D
  > ```
  >
  
* 출력

  > 개미굴의 시각화된 구조를 출력하여라.
  >
  > 개미굴의 각 층을 "--" 로 구분하며, 같은 층에 여러개의 방이 있을 때에는 사전 순서가 앞서는 먹이 정보가 먼저 나온다.
  >
  > ```bash
  > A
  > --B
  > ----C
  > ------D
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = []
    for _ in range(n):
        tmp = list(input().split())
        arr.append(tmp[1:])

    arr.sort()
    # 이미 출력한 단어 기록
    visit_dic = {}

    for i in range(n):
        tmp_string = ''

        for j in range(len(arr[i])):
            tmp_string += arr[i][j]

            if tmp_string not in visit_dic:
                visit_dic[tmp_string] = 1
                floor = '--' * j
                print(floor + arr[i][j])


sol()
```

> 



* 모범답안

  ```python
  import sys
  n = int(sys.stdin.readline())
  ant = []
  
  for i in range(n):
      ant.append(sys.stdin.readline().split()[1:])
  
  tmp = []
  for i in sorted(ant):
      count = 0
      for j in range(len(tmp)):
          if tmp[j] == i[j]:
              count += 1
          else:
              break
      cnt = count
      for j in range(count, len(i)):
          print('--' * cnt + i[j])
          cnt += 1
      tmp = i
  ```

  > 어떻게 문자열 방문표시를 하나했더니 이전 문자열만 사용하면 되므로 리스트를 통해 옮겨 담았구만!
  >
  > 그래서 겹치는 게 있을 경우에만 카운트를 높여 주며 다음 문자열로 넘어 간다.
