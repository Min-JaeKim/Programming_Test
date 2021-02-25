# python

## swea d2 1859 백만 장자 프로젝트

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8



> 1576ms 의미 없음 진짜



* 문제

  > 25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
  >
  > 다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
  >
  > 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
  >
  >   \1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
  >   \2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
  >   \3. 판매는 얼마든지 할 수 있다.
  >
  > 예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.

* 입력

  > 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 이익을 출력한다.
  >
  > ```bash
  > 3
  > 3
  > 10 7 6
  > 3
  > 3 5 9
  > 5
  > 1 1 3 1 2
  > ```

* 출력

  > 1번째 케이스는 아무 것도 사지 않는 것이 최대 이익이다.
  >
  > 2번째 케이스는 1,2일에 각각 한 개씩 사서 세 번째 날에 두 개를 팔면 10의 이익을 얻을 수 있다.
  >
  > ```bash
  > #1 0
  > #2 10
  > #3 5
  > ```



* 제출

  ```python
  t = int(input())
  for tc in range(1, t+1):
      n = int(input())
      result, cnt = 0, 0
      arr = list(map(int, input().split()))
      maxvalue = arr[-1]
      for i in range(len(arr) - 2, -1, -1):
          if maxvalue < arr[i]:
              result += cnt * maxvalue
              maxvalue, cnt = arr[i], 0
          else:
              cnt += 1
              result -= arr[i]
      result += cnt * maxvalue
      print('#%d %d' % (tc, result))
  ```

  > d2짜리 문제 주제에 날 고민하게 만들었다.. 보통 20분 컷이면 끝나는 d2짜리 문제들인데,, 날 이렇게 오랫동안 고민하게 만든 애는 얘가 처음이다...
  >
  > 뒤에서부터 계산해줬는데 현재 값을 마지막 값으로 설정해두고 리스트 앞까지 거슬러 올라갔다. 중간에 현재 최댓값보다 큰 값을 만나면 result 값에 수익을 더해주고 최댓값을 갱신하였다.

  

* 모범답안

  ```python
  1501
  
  T = int(input())
   
  for i in range(T):
      N = int(input())
      mylist = list(map(int, input().split(' ')))[::-1]  # 뒤에서부터 탐색
      answer = 0
      now_max = mylist[0]  # 현재 가장 큰 값
   
      for j in range(1, N):
          if now_max > mylist[j]:
              answer += now_max - mylist[j]
          else:
              now_max = mylist[j]
   
      print('#{} {}'.format(i+1, answer))
  ```

  > 오,, 나랑 똑같이 풀었다 생각했는데 오늘 또 하나 배워간다.
  >
  > 나는 for문을 뒤에서부터 하는 거로 했는데 이사람은 애초에 입력 받을 때 [::-1]이라고 코드를 짜주면서 배열을 거꾸로 만들었다 신기 신기

