# python

## baek 2258 정육점 실버1

https://www.acmicpc.net/problem/2258

> python3 428ms
>



* 문제

  > 은혜는 정육점에서 고기를 사려고 한다. 보통 정육점에서는 자신이 원하는 양을 이야기하면 그 양만큼의 고기를 팔지만, 은혜가 방문한 정육점에서는 세일 행사를 하고 있었기 때문에 N 덩어리의 고기를 이미 잘라놓고 판매하고 있었다.
  >
  > 각각의 덩어리들은 이미 정해져 있는 무게와 가격이 있는데, 어떤 덩어리를 샀을 때에는 그 덩어리보다 싼 고기들은 얼마든지 덤으로 얻을 수 있다(추가 비용의 지불 없이). 또한 각각의 고기들은 부위가 다를 수 있기 때문에 비용과 무게와의 관계가 서로 비례하는 관계가 아닐 수도 있다. 은혜는 이러한 점을 고려하지 않고, 어느 부위든지 자신이 원하는 양만 구매하면 되는 것으로 가정한다. 또한 만약 가격이 더 싸다면 은혜가 필요한 양보다 더 많은 고기를 살 수도 있다.
  >
  > 각 덩어리에 대한 정보가 주어졌을 때, 은혜가 원하는 양의 고기를 구매하기 위해 필요한 최소 비용을 계산하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 두 정수 N(1≤N≤100,000), M(1≤M≤2,147,483,647)이 주어진다. N은 덩어리의 개수를 의미하고, M은 은혜가 필요한 고기의 양이다. 다음 N개의 줄에는 각 고기 덩어리의 무게와 가격을 나타내는 음 아닌 두 정수가 주어진다. 무게의 총 합과 가격의 총 합은 각각 2,147,483,647을 넘지 않는다.
  >
  > ```bash
  > 4 9
  > 1 2
  > 2 4
  > 3 6
  > 4 8
  > ```
  > 
  
* 출력

  > 첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
  >
  > ```bash
  > 8
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], -x[0]))
    meat, flag, res, price, smpr = 0, 0, float('inf'), 0, 0

    for i in range(n):
        meat += arr[i][0]
        if arr[i][1] == price:
            smpr += price
        else:
            price, smpr = arr[i][1], arr[i][1]

        if m <= meat:
            res = min(smpr, res)
            flag = 1

    print(res if flag else -1)


sol()
```

> 아 진짜 그리디를 열심히 연습해야겠다고 느낀게 진짜 나에게 너무 버거운 문제였다고 생각함.
>
> 처음에 현재 고기보다 값이 싼 고기만 덤으로 준다는 조건을 온전히 받아들이지 못하고, 같은 가격의 고기를 만났을 때의 조건은 처리하지 않았다. 같은 가격의 고기는 비용에 포함해야 함.. 나는 들어오는 리스트 전부 한 바퀴 돌았지만 최적화된 답은 적절한 답이 나올 때 관둔다. 멋지네,,



* 모범답안

  ```python
  312
  
  import sys
  input = sys.stdin.readline
  
  
  def getMinCost(meats):
      meats.sort(reverse=True, key=lambda x: x[0])
      meats.sort(key=lambda x: x[1])
  
      weightCount = 0
      sameCostCount = 0
      costList = []
  
      for i in range(N):
          w, c = meats[i]
  
          weightCount += w
          # 같은 가격인 고기들을 여러 개 살 경우
          if i >= 1 and c == meats[i-1][1]:
              sameCostCount += c
          # 일반적인 경우, 이전 고기보다 현재 고기가 비쌀 경우
          else:
              sameCostCount = c
  
          if weightCount >= M:
              costList.append(sameCostCount)
  
              if sameCostCount == c:
                  break
  
      if costList:
          return min(costList)
      else:
          return -1
  
  
  if(__name__ == "__main__"):
      # 입력
      N, M = map(int, input().split())
  
      meats = []
      for _ in range(N):
          meats.append(list(map(int, input().split())))
  
      # 처리
      minCost = getMinCost(meats)
      print(minCost)
  
  ```

  > 아 그러니까 결국 하나만 산 게 결과 리스트에 들어온다면 그것이 최적화된 답 중 마지막일 테니 끝내는구나. 현명하다. 하 진짜 힘든문제였다.

