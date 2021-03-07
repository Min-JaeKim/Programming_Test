# Python

## baek 1987 알파벳 골드4

https://www.acmicpc.net/problem/1987



> python3 2378ms



* 문제

  > 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
  >
  > 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
  >
  > 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
  
* 입력

  > 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.
  >
  > ```bash
  > 2 4
  > CAAB
  > ADCB
  > ```

* 출력

  > 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
  >
  > ```bash
  > 3
  > ```
  
  

```python
from datetime import datetime
import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
start = datetime.now()
q, result = set([]), 0
s = arr[0][0]
q.add((0, 0, s))

while q:
    row, col, a = q.pop()
    result = max(result, len(a))
    if result == 26:
        break
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < r and 0 <= nc < c and (arr[nr][nc] not in a):
            q.add((nr, nc, a + arr[nr][nc]))

print(result)
print(datetime.now()-start)


'''
16 4
ABCD
EFAD
ASDA
NGHZ
ABCD
EFAD
ASDA
NGHZ
ABCD
EFAD
ASDA
NGHZ
ABCD
EFAD
ASDA
NGHZ
8

2 4
CAAB
ADCB
3 

3 6
HFDFFB
AJHGDH
DGAGEH
6

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH 
10


'''
```

> 허허,, 문제에는 분명 깊이 우선 탐색이라고 적혀 있고, 나도 분명 처음에 깊이 우선탐색이 맞다 생각해서 풀었다. 최단 거리는 아니고, 최대한의 새로운 문자열을 저장하는 것이기 때문이다. 근데 결론적으로는 queue를 사용해서 푸는 문제였다. 그렇다고 해서 완전한 bfs는 아니고.. 그렇다고 재귀로 들어가는 dfs는 더더욱 아니다..
>
> 그리고 가장 중요한 핵심은 set과 문자열인데, 우선 set부터 설명해 본다. set을 쓰지 않았을 경우, 방문표시를 하지 않는 코드이기 때문에 중복값이 엄청 들어올 수 있다. 따라서 set을 써서 중복값을 미리 배제해 줘야 한다.
>
> 마지막으로 문자열로 not in을 써야 한다. 처음에는 리스트와 함께 not in을 썼다가 시간 초과 났다. 뭐 이건 당연한 결과라고 생각했으니 대수롭지 않게 넘겼다. 두번째로는 queue를 넘길때 리스트에 현재 알파벳을 추가([:])해서 넘기는 방향으로 했는데, 이것 또한 시간 초과. 그럼 방법은 문자열 하나 밖에 없었다. 문자열 뒤에 알파벳을 주렁주렁 달아놓고 not in 을 쓰면 시간초과도 안나고 정말 쉽게 끝날 일...
>
> 진짜 힘겨운 모험이었다. 집중도 안되고 문제도 안풀리는데 심지어 포기하기도 싫어서 여러 방향으로 접근했다가 낭패를 보았다.. 이런 건 빨리 해답을 찾아 보는 게 답인가 보다.



* 모범답안

  ```python
  r, c = map(int, input().split())
  board = [list(input()) for _ in range(r)]
  
  answer = 0
  alphabet = [0]*26
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  def dfs(x, y, cnt):
      for i in range(4):
          nx = x+dx[i]
          ny = y+dy[i]
          
          if nx<0 or nx>=r or ny<0 or ny>=c:
              continue
          
          if not alphabet[ord(board[nx][ny])-65]:
              alphabet[ord(board[nx][ny])-65] = 1
              dfs(nx, ny, cnt+1)
              alphabet[ord(board[nx][ny])-65] = 0
          else:
              global answer
              answer = max(answer, cnt)
  
  alphabet[ord(board[0][0])-65] = 1
  dfs(0, 0, 1)
  
  print(answer)
  ```

  > 하,, dfs로 풀려면 이렇게 풀어야 하는구나. 참 멋진 코드다.

