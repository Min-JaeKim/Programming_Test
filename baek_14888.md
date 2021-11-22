# python

## baek 14888 연산자 끼워넣기 실버1

https://www.acmicpc.net/problem/14888

> python3 84ms



* 문제

  > N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
  >
  > 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
  >
  > 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.
  >
  > - 1+2+3-4×5÷6
  > - 1÷2+3+4-5×6
  > - 1+2÷3×4-5+6
  > - 1÷2×3-4+5+6
  >
  > 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
  >
  > - 1+2+3-4×5÷6 = 1
  > - 1÷2+3+4-5×6 = 12
  > - 1+2÷3×4-5+6 = 5
  > - 1÷2×3-4+5+6 = 7
  >
  > N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
  >
  > ```bash
  > 6
  > 1 2 3 4 5 6
  > 2 1 1 1
  > ```
  >
  
* 출력

  > 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
  >
  > ```bash
  > 54
  > -24
  > ```



```python
84

import sys
input = sys.stdin.readline

min_v, max_v = float('inf'), -float('inf')


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    p, m, x, d = map(int, input().split())

    def recursion(cur, p, m, x, d, cnt):
        global min_v, max_v

        if cnt == n:
            if cur < min_v:
                min_v = cur
            if max_v < cur:
                max_v = cur
            return

        if p:
            recursion(cur + arr[cnt], p-1, m, x, d, cnt+1)
        if m:
            recursion(cur - arr[cnt], p, m-1, x, d, cnt+1)
        if x:
            recursion(cur * arr[cnt], p, m, x-1, d, cnt+1)
        if d:
            if cur < 0:
                recursion(-(-cur // arr[cnt]), p, m, x, d-1, cnt+1)
            else: recursion(cur // arr[cnt], p, m, x, d-1, cnt+1)

    recursion(arr[0], p, m, x, d, 1)
    print(max_v)
    print(min_v)


sol()
```

> 하,,, 진짜 멍충이 똥멍충이 ㅠㅠ
>
> 최솟값 최댓값 초기화를 엉망진창으로 해놔서 뭐가 틀린 건지도 모르고 고민했잔수 ㅜㅜ 
>
> 식은 잘세웠어 ㅎㅎ 토닥토닥 ㄱㅊㄱㅊ



* 모범답안

  ```python
  72
  
  import sys
  input = sys.stdin.readline
  
  N = int( input() )
  nums = list( map( int, input().split() ) )
  oper = list( map( int, input().split() ) )
  
  # method 2
  def backtrack( prevVal, size, idx, plus, minus, multi, divide ):
  	global max, min
  	if size == N - 1:
  		if max < prevVal:
  			max = prevVal
  		if min > prevVal:
  			min = prevVal
  	else:
  		if plus:
  			backtrack( prevVal + nums[idx], size + 1, idx + 1, plus - 1, minus, multi, divide )
  
  		if minus:
  			backtrack( prevVal - nums[idx], size + 1, idx + 1, plus, minus - 1, multi, divide )
  
  		if multi:
  			backtrack( prevVal * nums[idx], size + 1, idx + 1, plus, minus, multi - 1, divide )
  
  		if divide:
  			if prevVal < 0:
  				backtrack( -(abs(prevVal) // nums[idx]), size + 1, idx + 1, plus, minus, multi, divide - 1 )
  			else:
  				backtrack( prevVal // nums[idx], size + 1, idx + 1, plus, minus, multi, divide - 1 )
  max = -(10**9+1)
  min = 10 ** 9 + 1
  backtrack( nums[0], 0, 1, *oper )
  print( max, min, sep = '\n' )
  ```
  
  > 

