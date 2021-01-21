# python

## 동빈나 구현 113 page

```python
n = int(input())
count = 0
time = 59

for i in range(n+1):
    for j in range(time+1):
        for k in range(time+1):
            result = str(i) + str(j) + str(k)
            if '3' in result:
                count += 1
                
print(count)
```

> 계속 실패했던 이유는 중복값을 한 번 더 세기 때문이었다. 예를들어 55933과 55933을 다른 수로 보고 2번 씩 세는데, 이 문제를 해결하기 위해 if문으로 처리 해야만 했다.
>
> 하나 더 배워가기,,



* 계속 실패한 코드

```java
n = int(input())
count = 0
time = 59

for i in range(n+1):
    for j in range(time+1):
        for k in range(time+1):
            result = str(i) + str(j) + str(k)
            for m in range(len(result)):
                if(result[m] == '3'):
                    print(result)
                    count += 1
                    continue
                
print(count)
```

