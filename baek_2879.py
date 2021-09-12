# python

## baek 2879 코딩은 예쁘게 골드1

https://www.acmicpc.net/problem/2879

> python3 176ms

* 문제

  > 백준이는 한 작은 회사에 취직했다. 이 회사에서 백준이는 소스 코드의 뒤죽박죽인 인덴트를 고치고 있다. 인덴트는 각 줄을 탭 키를 이용해 들여 쓰는 것을 말한다. 다행히 백준이가 사용하는 편집기는 연속된 줄을 그룹으로 선택하고, 여기에서 각 줄의 앞에 탭을 추가하거나, 삭제할 수 있다. 백준이를 도와 코드의 뒤죽박죽인 인덴트를 예쁘게 고치는 방법을 생각해보자.
  >
  > 줄의 개수 N과 각 줄의 앞에 있는 탭의 개수와 올바른 탭의 개수가 주어진다. 이때, 한 번 편집을 할 때, 다음과 같은 명령을 수행할 수 있다.
  >
  > - 연속된 줄을 그룹으로 선택한다.
  > - 선택된 줄의 앞에 탭 1개를 추가하거나 삭제한다.
  >
  > 위의 두 명령을 모두 수행하는 것이 하나의 편집이며, 선택된 줄의 개수와는 상관이 없다. 만약, 선택한 줄 중에 단 한 줄이라도 탭이 없을 경우에는, 탭을 삭제하는 명령을 수행할 수 없다.
  >
  > 백준이가 몇 번 편집 만에 코드의 인덴트를 올바르게 고칠 수 있는지 구하는 프로그램을 작성하시오. 이때, 편집 회수의 최솟값을 구해야 한다.

* 입력

  > 첫째 줄에 줄의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 현재 줄에 있는 탭의 개수가 주어지며, 1번째 줄부터 순서대로 주어진다. 탭의 개수는 0보다 크거나 같고, 80보다 작거나 같은 정수이다. 셋째 줄에는 각 줄의 올바른 탭의 개수가 주어진다. 1번째 줄부터 순서대로 주어지며, 이 값도 0보다 크거나 같고, 80보다 작거나 같은 정수이다.
  >
  > ```bash
  > 3
  > 3 4 5
  > 6 7 8
  > ```
  >
  
* 출력

  > 첫째 줄에 코드의 인덴트를 올바르게 고치는 편집 회수의 최솟값을 출력한다.
  >
  > ```bash
  > 3
  > ```



- 

```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    correct = list(map(int, input().split()))
    res, flag, tmp, stop = 0, 'p', [], False
    v, num = [0] * n, float('inf')

    while not stop:
        stop = True

        for i in range(n):
            if stop and not v[i]:
                stop = False

            if not stop:
                if arr[i] == correct[i]:
                    v[i] = 1
                if v[i]:
                    break
                if correct[i] < arr[i]:
                    if flag == 'p':
                        if tmp:
                            while tmp:
                                idx = tmp.pop()
                                arr[idx] += num
                                if arr[idx] == correct[idx]:
                                    v[idx] = 1
                            res += num
                        flag = 'n'
                        num = float('inf')

                    if arr[i] - correct[i] < num:
                        num = arr[i] - correct[i]
                    tmp.append(i)

                elif arr[i] < correct[i]:
                    if flag == 'n':
                        if tmp:
                            while tmp:
                                idx = tmp.pop()
                                arr[idx] -= num
                                if arr[idx] == correct[idx]:
                                    v[idx] = 1
                            res += num
                        flag = 'p'
                        num = float('inf')

                    if correct[i] - arr[i] < num:
                        num = correct[i] - arr[i]
                    tmp.append(i)

        if tmp:
            while tmp:
                if flag == 'n':
                    idx = tmp.pop()
                    arr[idx] -= num
                    if arr[idx] == correct[idx]:
                        v[idx] = 1
                else:
                    idx = tmp.pop()
                    arr[idx] += num
                    if arr[idx] == correct[idx]:
                        v[idx] = 1
            res += num

    print(res)


sol()
```

> 처음에 문제를 잘못이해하고 단순하다고 생각했었다.
>
> 걍 증가와 감소가 나뉠 때에만 끊어줘서, 그 안에서 가장 큰 인덴트 횟수를 결과값에 더해 줬더니 fail..
>
> 결론적으로, 인덴트는 한 번씩 할 때마다 횟수가 1 추가되므로 중간 중간에 결과값과 같아지는 수가 존재할 것이다. 그래서 그 부분마다 끊어 주며 계산해 줬어야 했다. 그러다 보니 코드가 엄청 더러워졌는데 그래도 골드1을 최초로, 그것도 혼자서 풀었다는 것에 만족할래.



* 모범답안

  ```python
  56
  
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  d = [x - y for x, y in zip(a, b)]
  print(sum(w - v for v, w in zip([0] + d, d + [0]) if v < w))
  ```

  > 내가 이렇게 풀 수 있을까 ㅋㅋㅋㅋㅋㅋ 하,, 우선 저 for문은
  >
  > [0, -3, 5, -3] [-3, 5, -3, 0]
  >
  > 이렇게 도는데 0을 추가하여 엇갈려서 계산함으로써,, 저렇게 풀 수 있는듯,, 몰라,,

