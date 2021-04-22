# python

## swea 5248 d3 그룹 나누기

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

learn - advanced - graph

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


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(n+1)]
    v, res = {}, 0
    for i in range(0, m*2, 2):
        if find(p[arr[i]]) != find(p[arr[i+1]]):
            # 짝이 되고 싶은 애들끼리 부모를 동일하게 묶어줌.
            union(arr[i], arr[i+1])
    for i in range(1, n+1):
        # 마지막으로 부모가 안묶인 애들이 있을 수 있으니 재차 묶어줌.
        # 이거를 안하면, 진짜 안묶인 애들이 있으니 꼭 해야 한다.
        find(i)
    for i in range(1, len(p)):
        if v.get(p[i]):
            continue
        else:
            v[p[i]] = 1
            res += 1
    print('#%d %d' % (tc, res))
```

> 어려웠던 듯,,



* 모범답안

  ```python
  def get_parent(x):
      if parent[x] != x: parent[x] = get_parent(parent[x])
      return parent[x]
   
  def union_parent(x, y):
      a = get_parent(x)
      b = get_parent(y)
      if a > b: parent[a] = b
      else: parent[b] = a
   
  for t in range(int(input())):
      N, M = map(int, input().split())
      parent = [i for i in range(N+1)]
      votes = list(map(int, input().split()))
      for i in range(0, M*2, 2): union_parent(votes[i], votes[i+1])
      answer = set()
      for i in parent: answer.add(get_parent(i))
      print('#{} {}'.format(t+1, len(answer)-1))
      
      
      -------------------
      
      
  def union(a, b):
      a = find(a)
      b = find(b)
      if a > b: p[a] = b
      else: p[b] = a
  
  
  def find(c):
      if p[c] != c: p[c] = find(p[c])
      return p[c]
  
  
  for tc in range(1, int(input())+1):
      n, m = map(int, input().split())
      arr = list(map(int, input().split()))
      p = [i for i in range(n+1)]
      v, res = {}, 0
      for i in range(0, m*2, 2):
          union(arr[i], arr[i+1])
      group = set()
      for i in range(1, len(p)):
          group.add(find(i))
      print('#%d %d' % (tc, len(group)))
  ```
  
  > 아,, 그냥 딕셔너리 안쓰고 set을 이용할 수 있구나..
  >
  > 나도 다시 이렇게 고쳐줬다.