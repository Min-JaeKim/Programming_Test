# python

## 동빈나 greedy2 98page



```python
x,y = map(int, input().split())
min_li = []

for i in range(x):
        li = list(map(int, input().split()))
        min_li.append(min(li))

    
print(max(min_li))
```

> 헷갈렸던 부분
>
> 1. 애초에 틀렸던 부분이 뭐냐면 list를 받는 부분이었음. list  받을 때, 애초에 한 줄을 한 번에 받아서 문제를 풀었어야 했는데 계속 막혔음.
