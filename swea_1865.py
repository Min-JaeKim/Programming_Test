# python

## swea 1865 d4 동철이의 일분배

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc



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
def dfs(cnt, work):
    global res
    if work <= res:
        return
    if cnt == n:
        res = max(work, res)
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, work*arr[cnt][i])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j]/100
    visited = [0] * n
    maxwork, res, resflag = 0, 0, 1
    dfs(0, 100)
    print('#%d %0.6f' % (tc, res))
```

> 음,, 미리 100으로 나눠서 차근차근 곱해나가며,, 계산 값보다 작아지면 return하는 게 중요함.



* 모범답안

  ```python
  for t in range(int(input())):
      n = int(input())
      p = [[*map(lambda x:x/100,map(int,input().split()))] for _ in range(n)]
   
      d = [0]*(1<<n)
      d[0] = 1
      for mask in range(1<<n):
          x = sum(1 for i in range(n) if mask&(1<<i))
          for j in range(n):
              if mask & (1<<j) == 0:
                  d[mask|(1<<j)] = max(d[mask|(1<<j)],d[mask]*p[x][j])
   
      print(f'#{t+1} {d[-1]*100:.6f}')
  ```
  
  > 이건 솔직히 무슨말인지 모르겠다.. 비트마스크를 열심히 해야하나.. 그런데 비트마스크가 금융권코테에 나올것 같진 않다...
  >
  > `[[*map(lambda x:x/100,map(int,input().split()))] for _ in range(n)]` 
  >
  > 이게 대박임. 
  >
  > 이걸 이해하기 어렵다면
  >
  > `[list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]`
  >
  > 이걸 보면 됨... 100으로 나눈 걸 반복문으로 계산하지 않고 입력 받을 때 받음.