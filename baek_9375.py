# python

## 백준 9375 패션왕신해빈 실버 3

https://www.acmicpc.net/problem/9375



> python3 68ms
>
> pypy3 120ms



* 문제

  > 해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
  
* 입력

  > 첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.
  >
  > - 각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
  > - 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
  >
  > 모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.
  >
  > ```bash
  > 2
  > 3
  > hat headgear
  > sunglasses eyewear
  > turban headgear
  > 3
  > mask face
  > sunglasses face
  > makeup face
  > ```

* 출력

  > 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.
  >
  > ```bash
  > 5
  > 3
  > ```



```python
'''
소인수 분해를 통한 약수 구하기
2의 2승 3의 2승의 약수의 개수는 (2+1) * (3+1)

hat headgear
sunglasses eyewear
turban headgear

딕셔너리 이용. 위와 같은 경우라면
cloth = {'headgear' : 2, 'eyewear' : 1}
이렇게 저장됨
'''

import sys
input = lambda : sys.stdin.readline().rstrip()  # 입력

tc = int(input())
for _ in range(tc):                 # 테스트 케이스
    n = int(input())                # 경우의 수
    cloth = {}                      # 딕셔너리
    for _ in range(n):
        a, b = input().split()
        if b not in cloth:          # 옷의 종류만 입력 받으면 됨
            cloth[b] = 1
        else:
            cloth[b] += 1           # 옷의 종류가 하나 씩 들어올 때마다 1씩 추가
    result = 1
    for value in cloth.values():
        result *= (value + 1)       # 약수의 개수 구하기
    print(result-1)                 # 입지 않은 경우의 수 감소

```

> 어떻게 풀었는지 잘 모르겠다..
>
> 처음에 조합으로 풀었는데 시간초과 떴다. 요즘은 진짜 시간초과를 밥먹듯이 해서 아주 미쳐버릴 것 같다.. 백준은 왜이렇게 시간에 야박한지 모르겠다. 아니면 파이썬이 다른 언어보다 시간초과가 잘나는 것일까?



### 모범답안

```python
import sys

input = sys.stdin.readline
num = int(input())

for _ in range(num):
    lists = {}
    ans = 1
    n = int(input())
    for i in range(n):
        x, y = input().split()
        if lists.get(y) != None:
            lists[y].append(x)
        else:
            lists[y] = [x]
    for k,v in lists.items():
        ans = ans * (len(v) +1)
    print(ans-1)
```

> ![img](md-images/image.png)
>
> * get은 딕셔너리를 사용할 때 쓴다.