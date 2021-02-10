# python

## swea d3 6485 삼성시의 버스 노선

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn



> ms



* 문제

  > 삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
  >
  > 그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
  >
  > Bi이하인 모든 정류장만을 다니는 버스 노선이다.
  >
  > P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.
  >
  > 다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.
  >
  > 다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.
  >
  > 다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다.
  >
  > ```bash
  > 
  > 1
  > 2
  > 1 3
  > 2 5
  > 5
  > 1
  > 2
  > 3
  > 4
  > 5	//테스트 케이스 개수
  > //첫 번째 테스트 케이스, N=2
  > // A1 = 1, B1 = 3
  > // A2 = 2, B2 = 5
  > // P = 5
  > // 이하 C1 = 1, C2 = 2, C3 = 3, C4 = 4, C5 = 5
  > ```

* 출력

  > 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후,
  >
  > 한 줄에 P개의 정수를 공백 하나로 구분하여 출력한다.
  >
  > j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수여야 한다.
  >
  > ```bash
  > #1 1 2 2 1 1	//첫 번째 테스트 케이스 결과
  > ```



* 제출

  ```python
  # import sys
  # sys.stdin = open('./s_input.txt')
  
  testCase = int(input())
  for tc in range(1,testCase+1):
      n = int(input())
      arr = {}
      for i in range(1,5001):
          arr[i] = 0
      for i in range(n):
          a,b = map(int, input().split())
          for j in range(a,b+1):
              arr[j] += 1
      p = int(input())
      print("#{}".format(tc), end=" ")
      for i in range(p):
          c = int(input())
          print(arr[c], end = ' ')
      print()
  ```

  > arr 선언 시에 배열( [0] for _ in range(5001) )을 쓰다보니 컴파일 에러가 걸리길래 dict를 사용했더니 돌아갔다. 찾아보니 확연히 시간차이가 많이 난다더라. 앞으로 dict를 써야겠다.

  ```python
  388ms
  
  testCase = int(input())
  for tc in range(1,testCase+1):
      n = int(input())
      arr = [0] * 5001
      for i in range(n):
          a,b = map(int, input().split())
          for j in range(a,b+1):
              arr[j] += 1
      p = int(input())
      print("#{}".format(tc), end=" ")
      for i in range(p):
          c = int(input())
          print(arr[c], end = ' ')
      print()
  ```

  > 그래서 위와 같이 [0]*5001을 해보았는데 살짝 빨라지는 수준이었다. 대체 왜지?



* 모범답안

  ```python
  201ms
  
  T = int(input())
  for tc in range(1, T+1):
      N = int(input())
      station = [0]*5001
      for i in range(N):
          Ai, Bi = map(int, input().split())
          for j in range(Ai, Bi+1):
              station[j] += 1
      P = int(input())
      P_list = []
      for i in range(P):
          P_list.append(int(input()))
   
      for i in range(len(P_list)):
          P_list[i] = str(station[P_list[i]])
      print('#{} {}'.format(tc, ' '.join(P_list)))
  ```
  
  > 내가 봤던 역대급 시간 적게 나온 답변,
  >
  > 하나 하나 실험을 해보면서 느낀 것은, p_list를 따로 선언해서 구현하는 게 가장 빠르다는 것이다. 나는 for문이 적으면 시간이 단축되는 줄 알고 있었지만, 꼭 그런 것만은 아니라고 느낀 문제.
  >
  > * **' '.join()** : 그리고 이것도 중요함. 띄어쓰기를 두고 문자열 모아서 출력

