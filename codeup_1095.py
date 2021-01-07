# python

## 코드업 1095

https://codeup.kr/problem.php?id=1095



### 입력

번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

#### 입력 예시

10 

10 4 2 3 6 6 7 9 8 5



### 출력

출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.

####  출력 예시

2



```python
a = int(input())
b = list(map(int,input().split()))
min = 24
for i in range(a):
    if min > b[i]:
        min = b[i]
print(min)
```

> b = map(int, input().split()) 라고 출력하니 b[i]로 나타낼 수 없었던 것이다. 따라서 앞에 list라고 표기해 줘야 한다.