# Python 

## pro level3 네트워크

https://programmers.co.kr/learn/courses/30/lessons/43162

> .



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
def solution(n, computers):
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            p[a] = b
        else:
            p[b] = a
    
    def find(c):
        if p[c] == c:
            return c
        p[c] = find(p[c])
        return p[c]
    
    
    p = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1 and find(i) != find(j):
                union(i, j)
                
    for i in range(n):
        p[i] = find(i)
    
    return len(set(p))
```

> 유니온 파인드를 다 까먹어 버린걸까,,
>
> 그건 그렇고 반례가 하나 있는데 그걸 못찾았다.
>
> 대신
>
> for i in range(n):
>         p[i] = find(i)
>
> 이 코드로 해결했는데 앞으로 유니온파인드 쓰려면 걍 저 코드도 같이 쓰는 게 낫겠다. 연산 개수가 200이었다.



* 모범답안

  ```python
  def solution(n, computers):
      temp = []
      for i in range(n):
          temp.append(i)
      for i in range(n):
          for j in range(n):
              if computers[i][j]:
                  for k in range(n):
                      if temp[k] == temp[i]:
                          temp[k] = temp[j]
      return len(set(temp))
  ```

  > 이거 완전 천재아냐
  >
  > 이걸 어케 플로이드와샬로 풀 생각을 할 수 있어

