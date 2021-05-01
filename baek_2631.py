# python

## baek 2631 줄세우기 골드5

https://www.acmicpc.net/problem/2631

> python3 68ms
>
> pypy3 108ms



* 문제

  > KOI 어린이집에는 N명의 아이들이 있다. 오늘은 소풍을 가는 날이다. 선생님은 1번부터 N번까지 번호가 적혀있는 번호표를 아이들의 가슴에 붙여주었다. 선생님은 아이들을 효과적으로 보호하기 위해 목적지까지 번호순서대로 일렬로 서서 걸어가도록 하였다. 이동 도중에 보니 아이들의 번호순서가 바뀌었다. 그래서 선생님은 다시 번호 순서대로 줄을 세우기 위해서 아이들의 위치를 옮기려고 한다. 그리고 아이들이 혼란스러워하지 않도록 하기 위해 위치를 옮기는 아이들의 수를 최소로 하려고 한다.
  >
  > 예를 들어, 7명의 아이들이 다음과 같은 순서대로 줄을 서 있다고 하자.
  >
  > 3 7 5 2 6 1 4
  >
  > 아이들을 순서대로 줄을 세우기 위해, 먼저 4번 아이를 7번 아이의 뒤로 옮겨보자. 그러면 다음과 같은 순서가 된다.
  >
  > 3 7 4 5 2 6 1
  >
  > 이제, 7번 아이를 맨 뒤로 옮긴다.
  >
  > 3 4 5 2 6 1 7
  >
  > 다음 1번 아이를 맨 앞으로 옮긴다.
  >
  > 1 3 4 5 2 6 7
  >
  > 마지막으로 2번 아이를 1번 아이의 뒤로 옮기면 번호 순서대로 배치된다.
  >
  > 1 2 3 4 5 6 7
  >
  > 위의 방법으로 모두 4명의 아이를 옮겨 번호 순서대로 줄을 세운다. 위의 예에서 3명의 아이만을 옮겨서는 순서대로 배치할 수가 없다. 따라서, 4명을 옮기는 것이 가장 적은 수의 아이를 옮기는 것이다.
  >
  > N명의 아이들이 임의의 순서로 줄을 서 있을 때, 번호 순서대로 배치하기 위해 옮겨지는 아이의 최소 수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에는 아이들의 수 N이 주어진다. 둘째 줄부터는 1부터 N까지의 숫자가 한 줄에 하나씩 주어진다. N은 2 이상 200 이하의 정수이다.
  >
  > ```python
  > 7
  > 3
  > 7
  > 5
  > 2
  > 6
  > 1
  > 4
  > ```
  >
  > 

* 출력

  > 첫째 줄에는 번호 순서대로 줄을 세우는데 옮겨지는 아이들의 최소 수를 출력한다.
  >
  > ```python
  > 4
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    arr = []
    n = int(input())

    for _ in range(n):
        num = int(input())
        for i in range(len(arr)):
            if arr[i] > num:
                arr[i] = num
                break
        else:
            arr.append(num)
    print(n-len(arr))


sol()


# '''
# 3 7 5 2 6 1 4
# 1 3 7 5 2 6 4
# 1 2 3 7 5 6 4
#
# '''
#
# import sys
# input = sys.stdin.readline
#
# arr, res = [], 0
# for _ in range(int(input())):
#     arr.append(int(input()))
# print(arr)
# strarr = ''.join(str(_) for _ in arr)
# lidx, ridx = 0, len(arr)-1
#
# while lidx < ridx:
#     if lidx != strarr.find(min(strarr[lidx:ridx])):
#         tmpmin = int(min(strarr[lidx:ridx]))
#         del arr[strarr.find(min(strarr[lidx:ridx]))]
#         arr.insert(lidx, tmpmin)
#         res += 1
#         strarr = ''.join(str(_) for _ in arr)
#     if ridx != strarr.rfind(max(strarr[lidx:ridx])):
#         tmpmax = int(max(strarr[lidx:ridx]))
#         del arr[strarr.rfind(max(strarr[lidx:ridx]))]
#         arr.insert(ridx, tmpmax)
#         res += 1
#         strarr = ''.join(str(_) for _ in arr)
#     print(arr)
#     lidx += 1
#     ridx -= 1
#
# print(res)
```

> 밑에는,, 인덱스로 푼 코드인데,, 이미 멀리 가고 나서야 잘못된 코드란 걸 깨달았다. 애초에 문제 의도를 잘못 파악했음,, 아마 문제에서 원한 건 순차적으로 진행되지 않은 숫자를 고르라는 뜻이었던 것 같다. 결국 문제 의도를 파악하지 못하고 답을 봤다. 이때,, 더 효율적으로 풀 수있는 방법이 있을 것 같아서 for else문을 썼다. for 안에 if 문에서 break를 만나지 못하면 else구문을 실행하는 거다..
>
> 다음에 또 이런 문제를 만나면 내가 풀 수 있을까,, 디피는 참 어렵고 험난하다..

* 모범답안

  ```python
  
  ```

  > 

