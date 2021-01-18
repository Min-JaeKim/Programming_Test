# python

## 동빈나 greedy 92page



```python
a,b,c = map(int, input().split())
li = list(map(int, input().split()))
    
li.sort(reverse = True)
result = 0
count = 0


while True:
    for i in range(c):
        if count == b:
            break
        result += li[0]
        count += 1
    if count >= b:
        break
    result += li[1]
    count += 1
    
print(result)
```

> 아 무한루프를 빠져나가는 데에 헤매지만 않았어도 쉽게 끝냈을 텐데 1시간이나 걸렸다 ㅜㅜ 
>
> 모르는 점을 잘 보안해 내고 다양한 문제를 풀어봄으로써 극복하는 게 최우선으로 보인다.





> 틀린 코드
>
> ```python
> a,b,c = map(int, input().split())
> li = list(map(int, input().split()))
>     
> li.sort(reverse = True)
> result = 0
> count = 0
> 
> 
> while True:
>     if count == b:
>         break
>     for i in range(c):
>         result += li[0]
>         count += 1
>     result += li[1]
>     count += 1
>     
> print(result)
> ```
>
> 1. 일단 list 입력 받는 거 몰라서 헤맸고,
> 2. sort를 하면 원래 값이 sort되는 것,
> 3. reverse로 sort하는 것.
> 4. 자꾸 무한루프가 도는데 원인을 밝혀내지 못했다. 헉 뭐지? 갑자기 된다. 왜지?
> 5. 아 왜인지 알아냈는데 for문을 돌다 보면 어느순간 b보다 더 커지게 되고, 나는 b와 같을 때에만 무한루프 while문을 탈출하게 설정해 놨으니 계속 무한루프를 도는 것이다.



### 모범답안

```python
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)
# 가장 큰 수가 더해지는 횟수 계산

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)

## kia~ 엄청 깔끔한 모범답안. 보고 배우자.
```

