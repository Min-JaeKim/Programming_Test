# python

## swea d2 1966 숫자를 정렬하자

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq



> ms



* 문제

  > 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
  >
  > **[제약 사항]**
  >
  > N 은 5 이상 50 이하이다.

* 입력

  > 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
  >
  > 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.
  >
  > ```bash
  > 10
  > 5
  > 1 4 7 8 0
  > ...
  > ```

* 출력

  > 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
  >
  > (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
  >
  > ```bash
  > #1 0 1 4 7 8
  > ...
  >  
  > ```



* 버블정렬

  ```python
  155ms
  import sys
  sys.stdin = open('./input.txt')
  
  testCase = int(input())
  for tc in range(1,testCase+1):
      n = int(input())
      arr = list(map(int, input().split()))
      for i in range(n-1):
          for j in range(n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j],arr[j+1] = arr[j+1],arr[j]
      print("#{}".format(tc), end = ' ')
      for i in range(n):
          print(arr[i], end = ' ')
      print()
  
  
  # 14780
  # 14708
  
  ```

  > 꾸역 꾸역 포문으로 풀었다.. 출력까지 for문으로,,,,, 이제 for문을 줄이는 습관을 가져야겠다.

* 정렬함수

  ```python
  147ms
  import sys
  sys.stdin = open('./input.txt')
  
  testCase = int(input())
  for tc in range(1,testCase+1):
      n = int(input())
      arr = list(map(int, input().split()))
      arr.sort()
      print("#{}".format(tc), end = ' ')
      for i in range(n):
          print(arr[i], end = ' ')
      print()
  ```

  > 역시 난 정렬함수가 편해 ... ㅜㅜ
  >
  > 



* 모범답안

  ```python
  131ms
  
  T = int(input())
   
  def sorting(x):
      for i in range(len(x)-1, 0, -1):
          for j in range(0, i):
              if x[j] > x[j+1]:
                  x[j], x[j + 1] = x[j+1], x[j]
      return x
   
   
  for t in range(1, T+1):
      N = int(input())
      N_list = list(map(int, input().split()))
      str_N = map(str, sorting(N_list))
   
      print('#{} {}'.format(t, ' '.join(str_N)))
  ```
  
  > 함수로 푸신 분은 시간이 짧게 나왔다 신기하다,, 그리고 str로 바꿔서 join으로 출력한 것도 시간 단축에 한 몫한 것이라고 생각한다.
  >
  > 엥 희한하다 ㅋㅋㅋㅋㅋ 방금 버블 정렬 + str출력했는데 시간이 훨씬 더나왔다. 그럼 시간 단축의 이유는 오로지 함수 때문인듯