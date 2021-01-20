# python

## 동빈나 greedy3 99page



```python
a,b = map(int, input().split())
count = 0

while True:
    if (a == 1):  break
    if a % b == 0:
        a /= b
        count += 1
    else :
        a -= 1
        count += 1
        
print(count)
```

> 프로그래머스에서 비슷한 그리디 문제를 풀었던 경험이 있다. 그때 굉장히 어렵게 풀어서 갈피를 못잡았기 때문에 이번에 슬쩍 해설을 보았다.
>
> 이문제는 프로그래머스와 다르게 나눌 수 있을 때까지 나누는 것을 최우선적으로 생각하면 쉽게 풀리는 문제다.
>
> 앞으로 문제에서 요구하는 바를 쉽게 캐치하는 것이 중요해 보인다.
>
> 아 그리고 추가로,, 테스트케이스가 없기 때문에 내 코드가 정말로 잘 짠 것인지 의문이 들기도 한다. 실제 시험장 가서는 히든 테스트케이스가 있기 때문에 정말로 완벽한 코드를 작성하는 것이 중요하다.





### 모범답안

```python
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    # 완조니,, 나눌 수 있는 상태로 만들어줌.
    
    result += n - target
    # 뺄셈 횟수를 추가
    
    n = target
    if n < k:
        break	# 더이상 나눌 수 없을 때 탈출
    result += 1
    n //= k
    
result += (n-1)
print(result)

## 타인의 코드를 이해한다는 것은 어려운 일이다,,,
```

