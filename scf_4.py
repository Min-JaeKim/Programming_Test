# Python

## Startup Coding Festival 2021 4





> 



* 문제

  > 

* 입력

  > 
  >
  > ```bash
  > 
  > ```
  
* 출력

  > 
  >
  > ```bash
  > 
  > ```



```python
pre = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
pretmp = list(map(float, input().split()))
pre['A'] = pretmp[0]
pre['B'] = pretmp[1]
pre['C'] = pretmp[2]
pre['D'] = pretmp[3]
pre['E'] = pretmp[4]

r, c = map(int, input().split())
info = [list(input()) for _ in range(r)]
preinfo = [list(input()) for _ in range(r)]
yre = []
ore = []

for i in range(r):
    for j in range(c):
        if info[i][j] == 'Y':
            yre.append([pre[preinfo[i][j]], preinfo[i][j], i, j])
        elif info[i][j] == 'O':
            ore.append([pre[preinfo[i][j]], preinfo[i][j], i, j])

yre = sorted(yre, key = lambda x : (-x[0], x[2], x[3]))
ore = sorted(ore, key = lambda x : (-x[0], x[2], x[3]))

for i in range(len(yre)):
    print(yre[i][1], yre[i][0], yre[i][2], yre[i][3])

for i in range(len(ore)):
    print(ore[i][1], ore[i][0], ore[i][2], ore[i][3])

'''
4.0 3.0 2.1 4.3 5.0
2 3
YYY
YYY
BBB
BBB
4.0 3.0 2.1 4.3 5.0
2 3
WYO
YYO
ABC
BBE
D 4.3 1 0
B 3.0 0 1
B 3.0 1 1
E 5.0 1 2
C 2.1 0 2
'''
```

> yre = sorted(yre, key = lambda x : (-x[0], x[2], x[3]))
>
> 람다식으로 정렬하기..
>
> yre의 0번째 인덱스로 내림차순 정렬 후,
>
> 2번째 인덱스로 오름차순 정렬 후,
>
> 3번째 인덱스로 오름차순 정렬.



* 모범답안

  ```python
  
  ```
  
  > 