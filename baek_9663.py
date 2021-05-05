# python

## baek 9663 N-Queen 골드5

https://www.acmicpc.net/problem/9663

> python3 ms
>
> pypy3 13696ms



* 문제

  > N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
  >
  > N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
  >
  > ```python
  >8
  > ```
  >
  > 
  
* 출력

  > 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
  >
  > ```python
  >92
  > ```



```python
import sys
input = sys.stdin.readline

res = 0


def sol():
    n = int(input())
    arr = [-1] * n

    def dfs(cnt):
        global res
        if cnt == n:
            res += 1
            return
        for i in range(n):
            if i not in arr:    # 행과 열 검색
                flag = 1
                for j in range(cnt):
                    if abs(arr[j] - i) == abs(j-cnt):   # 대각선 검색
                        flag = 0
                        break
                if flag:
                    arr[cnt] = i
                    dfs(cnt+1)
                    arr[cnt] = -1


    dfs(0)
    print(res)


sol()
```

> 도저히 문제를 이해 못하겠어서 풀이를 봤다. 사실 풀이를 보고 나서야 내가 생각했던 그 방법이 맞았구나 했다. 왜 생각을 실현하지 못했냐면 경우의 수가 엄청 많을 거라고 생각했기 때문이다. 역시는 역시,,, 실제로 파이썬3로 돌리면 시간초과가 난다.
>
> 아마 이게 파이썬3로 돌렸을 때 최선의 풀이일 것이다.





* 모범답안

  ```python
  
  ```
  
  > 

