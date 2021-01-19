# python

## ssafy java homework 02. Array



```python
li = []

a = int(input())
while a != 0:
    li.append(a)
    a = int(input())
    
li2 = [0 for _ in range(10)]

for i in range(len(li)):
    li2[ li[i] // 10 ] += 1
    
for i in range(len(li2)):
    if(li2[i] != 0):
        print("{} : {}개".format(i,li2[i]))
```

> 헷갈렸던 부분
>
> 1. li2 를 선언할 때, 0~9까지 크기를 설정해 놓아야 하는데 짧게 생각하고 li와 같은 길이의 리스트를 만들어서 계속 list out of range와 같은 오류가 났다.
> 2. print문이 어정쩡해서 format으로 다시 멀쩡히 처리하였다.
