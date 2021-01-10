# python

## 코드업 1098

https://codeup.kr/problem.php?id=1098



### 입력

첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

입력값의 정의역은 다음과 같다.

1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

#### 입력 예시

5 5 

3 

2 0 1 1 

3 1 2 3 

4 1 2 5



### 출력

모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.

####  출력 예시

1 1 0 0 0 

0 0 1 0 1 

0 0 1 0 1 

0 0 1 0 1 

0 0 0 0 1



```python
a,b = map(int,input().split())
w_h = [[0] * b for _ in range(a)]
c = int(input())

for tmp in range(c):
    i,j,m,n = map(int, input().split())
    if j == 0 :
        for tmp2 in range(i):
            w_h[m-1][n-1] = 1
            n += 1
    else :
        for tmp2 in range(i):
            w_h[m-1][n-1] = 1
            m += 1

for k in range(a):
    for l in range(b):
        print(w_h[k][l], end = ' ')
    print()
```

> 휴, 내가 계속 틀렸던 것은 고민하던 
>
> w_h [ m-  1 ] [ n-1 ] = 1 이부분이 아닌,
>
> w_h = [[0] * b for _ in range(a)] 이 부분이었다.
>
> 이유는 w_h = [[0] * a for _ in range(b)] 라고 썼기 때문인데, 행과 열을 순차적으로 입력 받기 때문에 틀릴 수 밖에 없었다. 정신 차리고 풀 것.