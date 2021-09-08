# python

## baek 2457 공주님의 정원 골드4

https://www.acmicpc.net/problem/2457

> python3 588ms

* 문제

  > 오늘은 공주님이 태어난 경사스러운 날이다. 왕은 이 날을 기념하기 위해 늘 꽃이 피어있는 작은 정원을 만들기로 결정했다.
  >
  > 총 N개의 꽃이 있는 데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다. 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다. (올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.)
  >
  > 이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.
  >
  > 1. 공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
  > 2. 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다. 
  >
  > N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오. 

* 입력

  > 첫째 줄에는 꽃들의 총 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 각 꽃이 피는 날짜와 지는 날짜가 주어진다. 하나의 날짜는 월과 일을 나타내는 두 숫자로 표현된다. 예를 들어서, 3 8 7 31은 꽃이 3월 8일에 피어서 7월 31일에 진다는 것을 나타낸다. 
  >
  > ```bash
  > 10
  > 2 15 3 23
  > 4 12 6 5
  > 5 2 5 31
  > 9 14 12 24
  > 6 15 9 3
  > 6 3 6 15
  > 2 28 4 25
  > 6 15 9 27
  > 10 5 12 31
  > 7 14 9 1
  > ```
  >
  
* 출력

  > 첫째 줄에 선택한 꽃들의 최소 개수를 출력한다. 만약 두 조건을 만족하는 꽃들을 선택할 수 없다면 0을 출력한다.
  >
  > ```bash
  > 5
  > ```



- 

```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr, answer = [], []    # 모든 꽃과 만족하는 꽃들의 최소 개수를 넣을 배열

    # 이건 단순히 ㅇ월 ㅇ일을 하나의 숫자로 만들기 위한 for문
    # 예를 들어 7월 5일일 경우 705로 변환.
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        start, end = str(a)+str(b).rjust(2,'0'), str(c)+str(d).rjust(2, '0')
        arr.append([int(start), int(end)])

    # 정렬
    arr.sort()
    endpoint, tmp = 301, [] # 문제에 주어진 첫 기준 날짜, 301보다 일찍 피는 꽃들을 임시로 저장할 배열

    # 꽃들을 돌면서
    for i in range(n):

        # 가장 마지막으로 확정된 꽃의 지는 시기와 맞물리는 꽃이라면
        # tmp 배열에 넣어줌
        if arr[i][0] <= endpoint:
            tmp.append(arr[i])

        # 만약 더이상 꽃이 지는 시기와 피는 시기가 맞물리지 않는다면
        else:
            # 계산할 꽃이 없다면 만족하는 꽃이 없다는 뜻이므로 종료
            if not tmp:
                print(0)
                exit()

            # 지는 시기를 기준으로 정렬
            tmp.sort(key=lambda x: -x[1])
            # endpoint는 그 꽃의 지는 시기를 넣어 주고
            endpoint = tmp[0][1]
            # 확정된 꽃을 넣는 배열에 넣어줌.
            answer.append(tmp[0])
            # 꽃 임시 저장 배열 초기화
            tmp = []
            # 만약 마지막으로 들어간 꽃이 12월 1일 이후에 진다면
            # 모든 조건을 만족하므로 종료.
            if answer[-1][1] >= 1201:
                break

            if arr[i][0] <= endpoint:
                tmp.append(arr[i])
            else:
                print(0)
                exit()

    for i in range(len(tmp)-1, -1, -1):

        if tmp[i][1] >= 1201:
            answer.append(tmp[i])
            break
    
    # 조건을 만족하는 꽃들의 개수 출력
    print(len(answer) if answer and answer[-1][1] >= 1201 else 0)


sol()
```

> 예외 케이스를 잘 봐야한다.
>
> 1. 문제를 꼼꼼히 읽어야 함 11 30으로 주어지면 11 29까지만 피어있는다는 뜻.
> 2. 배열의 마지막 꽃이 if에 속한다면 answer 배열에 들어가지 않으므로 마지막에 for문을 한 번 더 돌려 줘야 함.
> 3. 시간 단축으로 중요한 건, 현재 들어가는 꽃이 11 30 이후에 지는 꽃이라면 이제 더 볼 것 없으므로 종료.



* 모범답안

  ```python
  288
  
  import sys
  input = sys.stdin.readline
  flower = []
  for _ in range(int(input())):
      a, b, c, d = map(int, input().split())
      if a < 3:
          a, b = 3, 1
      if c > 11:
          c, d = 12, 1
      if c > 2:
          flower.append((a, b, c, d))
  flower = sorted(flower, key=lambda x:(x[0], x[1]))
  def gardening():
      cur_month, cur_day = 3, 1
      max_month, max_day = 3, 1
      cnt = 0
      for a, b, c, d in flower:
          if a > max_month or (a == max_month and  b > max_day):
              return 0
          if a > cur_month or (a == cur_month and  b > cur_day):
              cur_month, cur_day = max_month, max_day
              cnt += 1
          if c > max_month or (c == max_month and d > max_day):
              max_month, max_day = c, d
          if max_month == 12 and max_day == 1:
              return cnt + 1
      return 0
  print(gardening())
  ```

  > 

