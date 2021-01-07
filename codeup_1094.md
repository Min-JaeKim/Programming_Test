# python

## 코드업 1094

https://codeup.kr/problem.php?id=1094



### 입력

번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

#### 입력 예시

10 

10 4 2 3 6 6 7 9 8 5



### 출력

출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

####  출력 예시

5 8 9 7 6 6 3 2 4 10



```python
a = int(input())
b = input().split()
c = []
for i in range(0,a):
    c.append(int(b[i]))
for i in range(a-1,-1,-1):
    print(c[i], end = ' ')
    
# 다른코드
a = int(input())
b = input().split()
c = [0 for _ in range(a)]
tmp = 0
for i in range(a-1,-1,-1):
	c[tmp] = int(b[i])
	tmp+=1

for i in range(a):
	print(c[i], end = ' ')
```

> 자꾸 틀렸던 이유는 뭐냐면 for문에서 range 범위를 혼동했기 때문이다. 
>
> a-1이 아니라 a라고 적었고, 마지막 값 -1이 아니라 0이라고 적었기에 계속 틀렸다.
>
> 명심할것.