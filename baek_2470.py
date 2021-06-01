# python

## baek 2470 두 용액 골드5

https://www.acmicpc.net/problem/2470

> python3 140ms
>
> pypy3 176ms



* 문제

  > KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.  산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.
  >
  > 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 
  >
  > 예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
  >
  > 산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.
  >
  > ```python
  > 5
  > -2 4 -99 -1 98
  > ```
  > 
  > 
  
* 출력

  > 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
  >
  > ```python
  > -99 98
  > ```



```python
'''
-99 -2 -1 4 98

4
-3 -1 1 10
정답: -1 1

-1000 -1 680 999
'''
import sys
input = sys.stdin.readline

def sol():

    n = int(input())
    arr = sorted(list(map(int, input().split())))

    tmpres, resleft, resright = float('inf'), 0, 0
    left, right = 0, n-1

    while left < right:
        tmp = arr[left] + arr[right]
        if abs(tmp) < abs(tmpres):
            resleft, resright = arr[left], arr[right]
            tmpres = tmp
        if tmp > 0:
            right -= 1
        elif tmp < 0:
            left += 1
        else:
            break

    print(resleft, resright)


sol()
```

> 사실 풀면서 감이 잘 안왔다. 그래서 어떻게 풀어야 하는지에 대한 방법을 보았다..
>
> 우선 왼쪽과 오른쪽에 두가지 포인터를 두고 시작하는데, 두 개를 계산했을 때 양수면 더 작은 양수를 찾기 위해 오른쪽 포인터를 중앙으로 데려오고, 음수면 왼쪽 포인터를 중앙으로 데려온다.
>
> 그리고 현재 계산값의 절댓값이 0에 가깝다면 두 용액을 갱신해줌.

* 모범답안

  ```python
  124
  
import sys
  INF = sys.maxsize
  input = sys.stdin.readline
  
  def sol():
    n = int(input())
    target = list(map(int, input().split()))
    target.sort()
  
    lt = 0
    rt = n - 1
    minN = INF
  
    res = []
  
    while lt < rt:
      curr = target[lt] + target[rt]
      if abs(curr) < minN:
        minN = abs(curr)
        res = [target[lt], target[rt]]
      if curr >= 0:
        rt -= 1
      elif curr < 0:
        lt += 1
  
    print(*res)
  
  sol()
  ```
  
  > 오오 나랑 비슷하다

