# python

## 동빈나 greedy3 99page



```python
# 하,, 코드가 날아갔다...
# 대충 if문과 for문을 통해서 단순하게 반복하는 코드로 짰다
```

> 오류는 나지 않았지만 쉽게 푸는 방법이 필요했다.





### 모범답안

```python
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx, ny
    
print(x,y)

# 엄청 쉽게 풀었다. dx와 dy를 통해 방향을 제시했고, move_types와 순서를 맞춰줌으로써 for문에서 쉽게 해결해 나갈 수 있게 하였다.
```

