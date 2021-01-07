# python

## 코드업 1093

https://codeup.kr/problem.php?id=1093



### 입력

첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

#### 입력 예시

10 1 3 2 2 5 6 7 4 5 9



### 출력

1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

####  출력 예시

1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0



```python
a = int(input())
b = input().split()

li = [0 for tmp in range(23)]

for i in range(a):
	li[int(b[i]) -1] += 1
for i in range(23):
    print(li[i], end = ' ')
```

> 엉터리 코드로 해서 계속 틀렸었는데 그 이유는 b = map(int, input().split())로 받고 for문에서도 계속해서 li[b[i] -1] += 1 로 받았기 때문.
>
> map을 이용해서 int로 미리 설정해 놨지만, b를 사실상 처리하기 위해서는 list 타입일 때 처리하기 쉽기 때문이다.
>
> list랑 map은 알고리즘 공부를 하면서 더 터득해 나가야겠다.