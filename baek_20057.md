# python

## baek 20057 마법사 상어와 토네이도 골드3

https://www.acmicpc.net/problem/20057

> python3 1117ms

* 문제

  > [마법사 상어](https://www.acmicpc.net/problem/20056)가 토네이도를 배웠고, 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.
  >
  > 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다. 다음은 N = 7인 경우 토네이도의 이동이다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/preview)
  >
  > 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다. α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다. 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.
  >
  > 토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.

* 입력

  > 첫째 줄에 격자의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
  >
  > ```bash
  > 5
  > 0 0 0 0 0
  > 0 0 0 0 0
  > 0 100 0 0 0
  > 0 0 0 0 0
  > 0 0 0 0 0
  > ```
  >
  
* 출력

  > 격자의 밖으로 나간 모래의 양을 출력한다.
  >
  > ```bash
  > 85
  > ```



- 

```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    r, c, num, cnt, cnt2, direction = n//2, n//2, 1, 0, 0, 0 # 0 좌 1 하 2 우 3 상
    res = 0

    while r != 0 or c != -1:
        if direction == 0:
            nr, nc = r, c -1
            c -= 1

            if arr[nr][nc]:
                sand = arr[nr][nc]
                tmp1 = int(sand * 0.01)
                tmp2 = int(sand * 0.02)
                tmp3 = int(sand * 0.07)
                tmp4 = int(sand * 0.1)
                tmp5 = int(sand * 0.05)

                if 0 <= nr+1 < n and 0 <= nc+1 < n:
                    arr[nr+1][nc+1] += tmp1
                else:
                    res += tmp1
                if 0 <= nr-1 < n and 0 <= nc+1 < n:
                    arr[nr-1][nc+1] += tmp1
                else:
                    res += tmp1

                if 0 <= nr - 2 < n and 0 <= nc < n:
                    arr[nr - 2][nc] += tmp2
                else:
                    res += tmp2
                if 0 <= nr + 2 < n and 0 <= nc< n:
                    arr[nr + 2][nc] += tmp2
                else:
                    res += tmp2

                if 0 <= nr - 1 < n and 0 <= nc < n:
                    arr[nr - 1][nc] += tmp3
                else:
                    res += tmp3
                if 0 <= nr + 1 < n and 0 <= nc < n:
                    arr[nr + 1][nc] += tmp3
                else:
                    res += tmp3

                if 0 <= nr - 1 < n and 0 <= nc - 1 < n:
                    arr[nr - 1][nc - 1] += tmp4
                else:
                    res += tmp4
                if 0 <= nr + 1 < n and 0 <= nc - 1 < n:
                    arr[nr + 1][nc - 1] += tmp4
                else:
                    res += tmp4

                if 0 <= nr < n and 0 <= nc - 2 < n:
                    arr[nr][nc - 2] += tmp5
                else:
                    res += tmp5

                sand = sand - tmp1 * 2 - tmp2 * 2 - tmp3 * 2 - tmp4 * 2 - tmp5

                if 0 <= nr < n and 0 <= nc -1 < n:
                    arr[nr][nc-1] += sand
                else:
                    res += sand

                arr[nr][nc] = 0

        elif direction == 1:
            nr, nc = r+1, c
            r += 1

            if arr[nr][nc]:
                sand = arr[nr][nc]
                tmp1 = int(sand * 0.01)
                tmp2 = int(sand * 0.02)
                tmp3 = int(sand * 0.07)
                tmp4 = int(sand * 0.1)
                tmp5 = int(sand * 0.05)

                if 0 <= nr - 1 < n and 0 <= nc - 1 < n:
                    arr[nr - 1][nc - 1] += tmp1
                else:
                    res += tmp1
                if 0 <= nr - 1 < n and 0 <= nc + 1 < n:
                    arr[nr - 1][nc + 1] += tmp1
                else:
                    res += tmp1

                if 0 <= nr < n and 0 <= nc - 2 < n:
                    arr[nr][nc - 2] += tmp2
                else:
                    res += tmp2
                if 0 <= nr < n and 0 <= nc + 2 < n:
                    arr[nr][nc + 2] += tmp2
                else:
                    res += tmp2

                if 0 <= nr < n and 0 <= nc - 1 < n:
                    arr[nr][nc-1] += tmp3
                else:
                    res += tmp3
                if 0 <= nr < n and 0 <= nc + 1 < n:
                    arr[nr][nc + 1] += tmp3
                else:
                    res += tmp3

                if 0 <= nr + 1 < n and 0 <= nc - 1 < n:
                    arr[nr + 1][nc - 1] += tmp4
                else:
                    res += tmp4
                if 0 <= nr + 1 < n and 0 <= nc + 1 < n:
                    arr[nr + 1][nc + 1] += tmp4
                else:
                    res += tmp4

                if 0 <= nr + 2 < n and 0 <= nc < n:
                    arr[nr + 2][nc] += tmp5
                else:
                    res += tmp5

                sand = sand - tmp1 * 2 - tmp2 * 2 - tmp3 * 2 - tmp4 * 2 - tmp5

                if 0 <= nr + 1 < n and 0 <= nc < n:
                    arr[nr + 1][nc] += sand
                else:
                    res += sand

                arr[nr][nc] = 0

        elif direction == 2:
            nr, nc = r, c + 1
            c += 1

            if arr[nr][nc]:
                sand = arr[nr][nc]
                tmp1 = int(sand * 0.01)
                tmp2 = int(sand * 0.02)
                tmp3 = int(sand * 0.07)
                tmp4 = int(sand * 0.1)
                tmp5 = int(sand * 0.05)

                if 0 <= nr+1 < n and 0 <= nc-1 < n:
                    arr[nr+1][nc-1] += tmp1
                else:
                    res += tmp1
                if 0 <= nr-1 < n and 0 <= nc-1 < n:
                    arr[nr-1][nc-1] += tmp1
                else:
                    res += tmp1

                if 0 <= nr - 2 < n and 0 <= nc < n:
                    arr[nr - 2][nc] += tmp2
                else:
                    res += tmp2
                if 0 <= nr + 2 < n and 0 <= nc< n:
                    arr[nr + 2][nc] += tmp2
                else:
                    res += tmp2

                if 0 <= nr - 1 < n and 0 <= nc < n:
                    arr[nr - 1][nc] += tmp3
                else:
                    res += tmp3
                if 0 <= nr + 1 < n and 0 <= nc < n:
                    arr[nr + 1][nc] += tmp3
                else:
                    res += tmp3

                if 0 <= nr - 1 < n and 0 <= nc + 1 < n:
                    arr[nr - 1][nc + 1] += tmp4
                else:
                    res += tmp4
                if 0 <= nr + 1 < n and 0 <= nc + 1 < n:
                    arr[nr + 1][nc + 1] += tmp4
                else:
                    res += tmp4

                if 0 <= nr < n and 0 <= nc + 2 < n:
                    arr[nr][nc + 2] += tmp5
                else:
                    res += tmp5

                sand = sand - tmp1 * 2 - tmp2 * 2 - tmp3 * 2 - tmp4 * 2 - tmp5

                if 0 <= nr < n and 0 <= nc + 1 < n:
                    arr[nr][nc+1] += sand
                else:
                    res += sand

                arr[nr][nc] = 0
        else:
            nr, nc = r -1, c
            r -= 1

            if arr[nr][nc]:
                sand = arr[nr][nc]
                tmp1 = int(sand * 0.01)
                tmp2 = int(sand * 0.02)
                tmp3 = int(sand * 0.07)
                tmp4 = int(sand * 0.1)
                tmp5 = int(sand * 0.05)

                if 0 <= nr + 1 < n and 0 <= nc - 1 < n:
                    arr[nr + 1][nc - 1] += tmp1
                else:
                    res += tmp1
                if 0 <= nr + 1 < n and 0 <= nc + 1 < n:
                    arr[nr + 1][nc + 1] += tmp1
                else:
                    res += tmp1

                if 0 <= nr < n and 0 <= nc - 2 < n:
                    arr[nr][nc - 2] += tmp2
                else:
                    res += tmp2
                if 0 <= nr < n and 0 <= nc + 2 < n:
                    arr[nr][nc + 2] += tmp2
                else:
                    res += tmp2

                if 0 <= nr < n and 0 <= nc - 1 < n:
                    arr[nr][nc-1] += tmp3
                else:
                    res += tmp3
                if 0 <= nr < n and 0 <= nc + 1 < n:
                    arr[nr][nc + 1] += tmp3
                else:
                    res += tmp3

                if 0 <= nr - 1 < n and 0 <= nc - 1 < n:
                    arr[nr - 1][nc - 1] += tmp4
                else:
                    res += tmp4
                if 0 <= nr - 1 < n and 0 <= nc + 1 < n:
                    arr[nr - 1][nc + 1] += tmp4
                else:
                    res += tmp4

                if 0 <= nr - 2 < n and 0 <= nc < n:
                    arr[nr - 2][nc] += tmp5
                else:
                    res += tmp5

                sand = sand - tmp1 * 2 - tmp2 * 2 - tmp3 * 2 - tmp4 * 2 - tmp5

                if 0 <= nr - 1 < n and 0 <= nc < n:
                    arr[nr - 1][nc] += sand
                else:
                    res += sand

                arr[nr][nc] = 0

        cnt += 1
        if cnt == num:
            cnt = 0
            direction = (direction + 1) % 4
            cnt2 += 1

        if cnt2 == 2:
            cnt2 = 0
            num += 1

    return res


print(sol())
```

> 방향마다 배율의 위치가 달라지는데 이걸 어떻게 축약하지?



* 모범답안

  ```python
  1136
  
  def san(sand, y, x):
      global ans
      if 0 <= y < N and 0 <= x < N: mat[y][x] += sand
      else: ans += sand
  
  def tor(sand, dir, y, x):
      mat[y][x] = 0
      sand1 = sand // 100
      sand2 = sand // 50
      sand5 = sand // 20
      sand7 = sand * 7 // 100
      sand10 = sand // 10
      sanda = sand - sand5 - 2 * (sand1 + sand2 + sand7 + sand10)
      if dir == 1:
          san(sand1, y - 1, x + 1); san(sand1, y + 1, x + 1);
          san(sand2, y - 2, x); san(sand2, y + 2, x);
          san(sand7, y - 1, x); san(sand7, y + 1, x);
          san(sand10, y - 1, x - 1); san(sand10, y + 1, x - 1);
          san(sanda, y, x - 1); san(sand5, y, x - 2);
      elif dir == 2:
          san(sand1, y - 1, x - 1); san(sand1, y - 1, x + 1);
          san(sand2, y, x - 2); san(sand2, y, x + 2);
          san(sand7, y, x - 1); san(sand7, y, x + 1);
          san(sand10, y + 1, x - 1); san(sand10, y + 1, x + 1);
          san(sanda, y + 1, x); san(sand5, y + 2, x);
      elif dir == 3:
          san(sand1, y + 1, x - 1); san(sand1, y - 1, x - 1);
          san(sand2, y + 2, x); san(sand2, y - 2, x);
          san(sand7, y + 1, x); san(sand7, y - 1, x);
          san(sand10, y + 1, x + 1); san(sand10, y - 1, x + 1);
          san(sanda, y, x + 1); san(sand5, y, x + 2);
      elif dir == 4:
          san(sand1, y + 1, x - 1); san(sand1, y + 1, x + 1);
          san(sand2, y, x - 2); san(sand2, y, x + 2);
          san(sand7, y, x - 1); san(sand7, y, x + 1);
          san(sand10, y - 1, x - 1); san(sand10, y - 1, x + 1);
          san(sanda, y - 1, x); san(sand5, y - 2, x);
  
  def circuit():
      y, x = N // 2, N // 2
      cnt = 1
      while True:
          for _ in range(cnt):
              if (y, x) == (0, 0): return
              x -= 1
              tor(mat[y][x], 1, y, x)
          for _ in range(cnt):
              y += 1
              tor(mat[y][x], 2, y, x)
          cnt += 1
          for _ in range(cnt):
              x += 1
              tor(mat[y][x], 3, y, x)
          for _ in range(cnt):
              y -= 1
              tor(mat[y][x], 4, y, x)
          cnt += 1
  
  N = int(input())
  mat = [list(map(int, input().split())) for _ in range(N)]\
  
  ans = 0
  circuit()
  print(ans)
  ```

  > 아 이게 지도에서 유효한 값이라는 걸 함수로 쓰면 중복 코드를 제거할 수 있구나!!! 나 완전 짱멍충

