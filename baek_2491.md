# Python

## baek 2491 수열 실버2

https://www.acmicpc.net/problem/2491



> python3 156ms



* 문제

  > 0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라. 
  >
  > 예를 들어 수열 1 2 2 4 4 5 7 7 2 의 경우에는  1≤2≤2≤4≤4≤5≤7≤7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다. 수열 4 1 3 3 2 2 9 2 3 의 경우에는 3≥3≥2≥2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다. 또 1 5 3 6 4 7 1 3 2 9 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.
  
* 입력

  > 첫째 줄에는 수열의 길이 N이 주어지고, 둘째 줄에는 N개의 숫자가 빈칸을 사이에 두고 주어진다. N은 1 이상 100,000 이하의 정수이다.
  >
  > ```bash
  > 9
  > 1 2 2 4 4 5 7 7 2
  > ```

* 출력

  > 첫째 줄에 가장 긴 길이를 출력한다.
  >
  > ```bash
  > 8
  > ```



```python
n = int(input()) # 수열의 수 입력
arr = list(map(int, input().split())) # 수열 입력

if n == 1: # 한 개 주어지면
    print(1) # 한 개 출력하고
    exit() # 바로 끝내기
if n == 2: # 두 개 주어지면
    print(2) # 두 개 출력하고
    exit() # 바로 끝내기


flag, cnt, max = True if arr[0] <= arr[1] else False, 1, 0
# 현재 오름차순 방향인지(True) 내림차순 방향인지(False), 현재 진행 중이면서 맞게 흘러가는 숫자들 개수, 흐름이 바뀔 때 최댓값 교체

i = 1 # index값
while i < n: # 인덱스가 끝까지 도다르기 전에
    if flag: # flag가 True라면(오름차순 방향이라면)
        if arr[i] >= arr[i-1]: # True진행인데 현재의 수가 이전의 수보다 크다면
            cnt += 1 # 개수 + 1
            i += 1 # 인덱스 값도 1 증가
        else: # True 진행인데 내림차순 방향으로 바뀌었다면
            if max < cnt: # max값이 현재의 수보다 작을 때
                max = cnt # max값 교체
            for j in range(i-1, -1, -1): # 1 3 3 2 와 같은 부분을 해결하기 위하 for문
                if arr[j] == arr[j-1]: # 현재 인덱스가 2에 있더라도 두 번째 3으로 되돌아가서
                    i = j # 인덱스를 바꿔줌 (두 번째 3으로 되돌아가도 3 3을 비교할 것이므로)
                else: # 만약 동일 수가 없다면
                    break # for문을 종료
            flag = False # 내림차순으로 flag를 변경
            cnt = 1 # 개수 세기는 다시 1부터
    else: # 내림차순 flag라면
        if arr[i] <= arr[i-1]: # 내림차순일 때
            cnt += 1 # 개수 증가
            i += 1 # 인덱스도 증가
        else: # 오름차순으로 바뀌었다면
            if max < cnt: # max값을 변경할 수 있을 때
                max = cnt # 변경
            for j in range(i-1, -1, -1): # 5 3 3 6 일 때 현재 인덱스가 6에 있다면
                if arr[j] == arr[j - 1]: # 인덱스를 두 번째 3으로 바꿔 주기 위한 과정
                    i = j # 
                else:
                    break
            flag = True # 양수 flag로 바꾸고
            cnt = 1 # 개수는 1로 초기화

print(max if cnt < max else cnt) # 마지막까지 계산한 개수가 max값보다 작다면 max값 출력. 그게 아니라면 cnt출력


'''
4 1 3 2 2 9 2 3
3

9
4 1 3 3 2 2 9 2 3
4

9
1 2 2 4 4 5 7 7 2
8

6
2 3 9 7 4 2
4

6
6 2 1 2 6 8
4
'''
```

> 2 1 3 3 2 와 같은 높아지다가 동일수가 오고 낮아지는 수열을 처리하지 못해서 몇 시간을 헤맸던 코드,,
>
> 결국 답을 볼까했지만 계속해서 풀릴 것 같은 느낌에 쉽사리 답을 못보고 결국 해결했다 ㅜㅜ



* 모범답안

  ```python
  128ms
  
  import sys
  sys.stdin = open("input.txt", 'r')
  
  N = int(input())
  arr = list(map(int, input().split()))
  cnt = 1
  max_l = 1
  for i in range(1, N):
      if arr[i-1] >= arr[i]:
          cnt += 1
      else:
          cnt = 1
      if max_l < cnt:
          max_l = cnt
  
  cnt = 1
  for i in range(1, N):
      if arr[i-1] <= arr[i]:
          cnt += 1
      else:
          cnt = 1
      if max_l < cnt:
          max_l = cnt
  print(max_l)
  ```
  
  > 미쳤다리,,,,,