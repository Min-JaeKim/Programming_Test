# python

## baek 3020 개똥벌레 골드5

https://www.acmicpc.net/problem/3020

> python3 472ms
>



* 문제

  > 개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수) 첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.
  >
  > 아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)
  >
  > ![img](md-images/preview)
  >
  > 이 개똥벌레는 장애물을 피하지 않는다. 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.
  >
  > 위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. (4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)
  >
  > ![img](md-images/preview)
  >
  > 하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.
  >
  > 동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)
  >
  > 다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.
  >
  > ```bash
  > 14 5
  > 1
  > 3
  > 4
  > 2
  > 2
  > 4
  > 3
  > 4
  > 3
  > 3
  > 3
  > 2
  > 3
  > 3
  > ```
  >
  
* 출력

  > 첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.
  >
  > ```bash
  > 7 2
  > ```



```python
import sys
input = sys.stdin.readline


def sol():
    n, h = map(int, input().split())
    down, up = [0] * (h+1), [0] * (h+1)
    res_ob, res_cnt = float('inf'), 0

    for i in range(n):
        if i % 2 == 0:
            down[int(input())] += 1
        else:
            up[int(input())] += 1

    for i in range(h-1, 0, -1):
        down[i] += down[i+1]
        up[i] += up[i+1]

    for i in range(1, h+1):
        if down[i] + up[h - i + 1] < res_ob:
            res_ob = down[i] + up[h - i + 1]
            res_cnt = 0
        if res_ob == down[i] + up[h - i + 1]:
            res_cnt += 1

    print(res_ob, res_cnt)


sol()
```

> 이분탐색 공부하고 싶었는데 누적합 공부했다
>
> 누적합이 정말 잘어울리는 문제였음 풀이가 눈에 쏙속 들어온다
>
> 실력을 많이 길러야 함을 느꼈다.



* 모범답안

  ```python
  216
  
  import sys
  
  
  def solve(N, H, xs):
      obs = [0] * H
      for b in xs[::2]:
          obs[b] -= 1
      for t in xs[1::2]:
          obs[H - t] += 1
  
      bump = N // 2
      min_value = bump
      min_count = 0
      for h in range(H):
          bump += obs[h]
          if bump < min_value:
              min_value = bump
              min_count = 1
          elif bump == min_value:
              min_count += 1
      return min_value, min_count
  
  
  def main():
      stdin = sys.stdin
      N, H = [int(x) for x in stdin.readline().split()]
      xs = [int(stdin.readline()) for _ in range(N)]
      print(*solve(N, H, xs))
  
  
  if __name__ == "__main__":
      main()
  
  ```
  
  > 하여간 엄청 희한한 방법으로 푸셨다
  >
  > 이것도 누적합 맞는 것 같긴 한데 좀 특이한 누적합이다
  >
  > 아예 위와 아래를 함께 계산하셨는데 위는 + 아래는 - 이런식으로 하심
  >
  > 내 머리가 따라잡기에는 역부족인 것 같다

