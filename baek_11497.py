# python

## baek 11497 통나무 건너뛰기 실버1

https://www.acmicpc.net/problem/11497

> python3 280ms.
>
> pypy3 200ms



* 문제

  > 남규는 통나무를 세워 놓고 건너뛰기를 좋아한다. 그래서 N개의 통나무를 원형으로 세워 놓고 뛰어놀려고 한다. 남규는 원형으로 인접한 옆 통나무로 건너뛰는데, 이때 각 인접한 통나무의 높이 차가 최소가 되게 하려 한다.
  >
  > ![img](md-images/1.png)
  >
  > 통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정된다. 높이가 {2, 4, 5, 7, 9}인 통나무들을 세우려 한다고 가정하자. 이를 [2, 9, 7, 4, 5]의 순서로 세웠다면, 가장 첫 통나무와 가장 마지막 통나무 역시 인접해 있다. 즉, 높이가 2인 것과 높이가 5인 것도 서로 인접해 있다. 배열 [2, 9, 7, 4, 5]의 난이도는 |2-9| = 7이다. 우리는 더 나은 배열 [2, 5, 9, 7, 4]를 만들 수 있으며 이 배열의 난이도는 |5-9| = 4이다. 이 배열보다 난이도가 낮은 배열은 만들 수 없으므로 이 배열이 남규가 찾는 답이 된다.
  
* 입력

  > 입력은 T개의 테스트 케이스로 이루어져 있다. 첫 줄에 T가 주어진다.
  >
  > 이어지는 각 줄마다 첫 줄에 통나무의 개수를 나타내는 정수 N(5 ≤ N ≤ 10,000), 둘째 줄에 각 통나무의 높이를 나타내는 정수 Li가 주어진다. (1 ≤ Li ≤ 100,000)
  >
  > ```python
  >3
  > 7
  >13 10 12 11 10 11 12
  > 5
  >2 4 5 7 9
  > 8
  > 6 6 6 6 6 6 6 6
  > ```
  >
  > 

* 출력

  > 각 테스트 케이스마다 한 줄에 주어진 통나무들로 만들 수 있는 최소 난이도를 출력하시오.
  >
  > ```python
  > 1
  > 4
  > 0
  > ```



- 풀이

```python
import sys
input = sys.stdin.readline


def sol():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = 0
        arr.sort()
        narr, left, right = [0]*n, 0, n-1
        for i in range(0, n, 2):
            if n % 2 == 1 and i == n-1:
                narr[left] = arr[i]
                break
            narr[left], narr[right] = arr[i], arr[i+1]
            left += 1
            right -= 1
        left, right = n//2, n//2
        while left > 0 or right < n-1:
            if left > 0:
                res = max(res, narr[left]-narr[left-1])
            if right < n - 1:
                res = max(res, narr[right]-narr[right+1])
            left -= 1
            right += 1
        res = max(res, abs(narr[0]-narr[-1]))
        print(res)

sol()

```

> 처음에 댕청하게,, 순열로 풀었음,, 너무 어이없당 ,, ㅋㅋ ㅋ ㅋ
>
> 그리고 두 번째 시도는 그냥 단순히 현재인덱스에서 현재-1 인덱스 현재-2인덱스 그리고 지금까지 최댓값을 갖고 for문을 돌림. 그랬더니 틀렸음,,, 그럴만두,, `res = max(arr[1]-arr[0], arr[n-1]-arr[n-2])` 이거를 했었어야함.
>
> 그리고 세번째 시도가 피라미드모양으로 만들어 풀기 ㅋㅋ  ㅋ 피라미드 배열을 새로 만들다보니 log(N)을 한 번 더 하게 되어 시간이 조금 길게나옴.



* 모범답안

  ```python
  180
  import sys
input = sys.stdin.readline
  
  
  def sol():
      t = int(input())
      for _ in range(t):
          n = int(input())
          arr = list(map(int, input().split()))
          arr.sort()      # 통나무 정렬 후,
          res = max(arr[1]-arr[0], arr[n-1]-arr[n-2])
          # 개수가 1개나 2개일 수 있으므로,,
          for i in range(n-2):
              if res < arr[i+2] - arr[i]:
                  res = arr[i+2] - arr[i]
          # 피라미드와 같은 형태를 가질테니
          # 2개 씩 건너 뛰면서 최댓값 찾기
          print(res)
  
  sol()
  ```
  
  > 모지,, for문 안에서 max를 지우고 if를 사용하니 220 에서 180으로 빨라졌다.. 앞으로  코드가 좀 길어지더라도 if 써야겠음. 그래서 지금 이문제 1등댐

