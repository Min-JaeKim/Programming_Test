# python

## swea d3 4831 전기버스

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do#none



> ms



* 문제

  > A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
  >
  > 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
  >
  > 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
  >
  > 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
  >  
  >
  > 
  > **[예시]**
  >
  > ![img](data:image/png;base64,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)
  >
  > 다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

* 입력

  > 첫 줄에 노선 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
  >
  >
  > 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
  >
  > ```bash
  > 3
  > 3 10 5
  > 1 3 5 7 9
  > 3 10 5
  > 1 3 7 8 9
  > 5 20 5
  > 4 7 9 14 17
  > ```

* 출력

  > \#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
  >
  > ```bash
  > #1 3
  > #2 0
  > #3 4
  > ```



```python
import sys # 파일입출력
sys.stdin = open('./sample_input.txt') # 입력값 받기

case = int(input()) # case 몇 개인지

for tc in range(1,case+1): # 케이스 for문
    k,n,m = map(int,input().split()) # 이동할 수 있는 거리, 버스정류장, 주유소 갯수
    bus = list(map(int, input().split())) # 버스정류소 받기
    result = 0 # 주유 충전 횟수
    i = 0 # while문을 중단할 수 있는 변수
    while i < n-k: # i가 주유를 충전해도 되지 않은 목적지 근처까지 가는 동안에
        if i+k in bus:  # 만약 bus 리스트에 최대치로 이동한다음 주유할 수 있는 곳이 있다면
            result += 1 # 결과값 더하고
            i += k # 버스는 그 최대치의 주유소로 이동
        else : # 없다면
            correct = False # 일단은 안됐다고 가정하고 false 준비
            for j in range(k,0,-1): # 최대치부터 생각해야 하니 k-1에서부터 하나씩 감소하는 반복문으로 
                if i+j in bus: # 만약 주유소가 존재한다면
                    result += 1 # 결과값 더하고
                    i += j # 역시 그 주유소로 이동
                    correct = True # 아까 안된다고 가정한 boolean을 true로 변경
                    break # 무사히 처리했으므로 for문을 나가도 좋음
            if correct == False: # 만약 끝까지 처리를 못해서 false라면
                result = 0 # 결과값은 0으로 처리해주고
                break # 반복문이 더 돌지 않게 break
    print("#%d %d" % (tc, result)) # 결과 출력
```

> 전기버스,,, 그리디로 꾸역꾸역 풀었지만 다른 사람의 풀이를 보아야 할 것 같다. 



* 모범답안

  ```python
  TC = int(input())
  for tc in range(1, TC+1):
      K,N,M = map(int,input().split())
      station = list(map(int, input().split()))
      station_lst = [0] * (N+1)
  
      for i in range(len(station)):
          station_lst[station[i]] += 1
  
      start = 0
      end = K
      cnt = 0
  
      while True:
          zero = 0
          for i in range(start+1, end+1):
              if station_lst[i] == 1:
                  start = i
              else:
                  zero += 1
  
          if zero == K:
              cnt = 0
              break
  
          cnt += 1
          end = start + K
  
          if end >= N:
              break
  
      print('#%s %d'%(tc, cnt))
  ```
  
  > 나는 그리디로 풀었는데 이분은 되게 정확하게 구현하려고 노력하신 것같다. 그래서 오히려 나보다는 더 많이 돌 수도 있지만 그래도 그 어느 반례에도 먹히지 않을 코드라고 생각이 된다.