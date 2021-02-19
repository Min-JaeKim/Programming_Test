# python

## swea d3 5356 의석이의 세로로 말해요

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO



> 184ms



* 문제

  > 아직 글을 모르는 의석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.
  >
  > 이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
  >
  > 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래에 의석이가 칠판에 붙여 만든 단어들의 예가 있다.
  >  
  >
  > A A B C D Da f z z0 9 1 2 1a 8 E W g 6P 5 h 3 k x
  >
  >  
  >
  > 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.
  >  
  >
  > 심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
  >
  > 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.
  >
  > 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.
  >
  > 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
  >
  > 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.
  >
  > 위에서 의석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:
  >
  >  
  >
  > Aa0aPAf985Bz1EhCz2W3D1gkD6x
  >
  >  
  >
  > 칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >  
  >
  > 각 테스트 케이스는 총 다섯 줄로 이루어져 있다.
  >
  > 각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.
  >
  > ```bash
  > 
  > 2
  > ABCDE
  > abcde
  > 01234
  > FGHIJ
  > fghij
  > AABCDD
  > afzz
  > 09121
  > a8EWg6
  > P5h3kx
  > ```

* 출력

  > 각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.
  >
  > ```bash
  > 
  > #1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
  > #2 Aa0aPAf985Bz1EhCz2W3D1gkD6x
  > ```



* 제출

  ```python
  import sys
  sys.stdin = open('./sample_input.txt')
  
  t = int(input()) # 테스트케이스 입력
  for tc in range(1, t+1): # 테스트 케이스를 돌면서
      arr = [list(input()) for _ in range(5)] # 5개의 입력을 받고
      result = []
  
      idx= 0 # 열의 인덱스 
      while True: # 무한루프로 돌리고
          count = False # 일단 false로 두고
          for i in range(5): # 행의 개수는 5개 고정.
              if idx < len(arr[i]): # 만약 인덱스가 문자열의 길이보다 커진다면 그 한 줄은 더이상 접근하면 안된다.
                  result.append(arr[i][idx]) # 결과 리스트에 존재하는 문자열을 삽입
                  count = True # 그리고 구분 flag를 true로 만들어 줌.
          if count == False: # 만약 5개 행을 다 돌면서 idx보다 다 길이가 작은 배열들 밖에 없다면, 
              break # 무한루프를 빠져나와야 함.
          idx += 1
  
      print('#%d' % (tc), end = ' ')
      print(''.join(result))
  ```
  
  > 내 한계를 체감한 코드
  >
  > 난 아직도 잘하려면 한참을 더 등반해야 하는 것 같다. 내가 범했던 오류는 뭐냐면, 매 행이 시작될 때마다 count변수를 새로 고침해줌으로써 ,, 마지막 행이 짧을 경우에 바로 결과가 출력되는 것이었다. 엉망진창 그자체,,
  
  
  
* 모범답안

  ```python
  151ms
  
  def func(arr):
      sol= ""
      l_max = [] # 각 행별 배열 길이
      for l in range(len(arr)):
          l_max.append(len(arr[l]))
      loop_max = max(l_max) # 최대 배열 길이만큼 loop
      for i in range(loop_max):
          if i < l_max[0]:
              sol += arr[0][i]
          else:
              pass
          if i < l_max[1]:
              sol += arr[1][i]
          else:
              pass
          if i < l_max[2]:
              sol += arr[2][i]
          else:
              pass
          if i < l_max[3]:
              sol += arr[3][i]
          else:
              pass
          if i < l_max[4]:
              sol += arr[4][i]
          else:
              pass
      return sol
   
  T = int(input()) # test_case
  for test_case in range(1, T+1):
      arr = []
      for i in range(5):
          s = input() # 2차원 배열로 입력
          arr.append(list(s))
      result = ""
      result = func(arr)
      print("#"+str(test_case), result)
  ```

  > 내가 처음에 생각했던 방식,, 문자열 길이 중 가장 긴 것을 기준으로, 모든 문자열 비교해 가며 결과 값에 추가하는 방법,, 어차피 행의 개수는 5개 밖에 되지 않으니 간단한 방법이다. 난 좀 더 고차원적으로 풀고 싶었는데 오히려 이렇게 하니 더 빠른 시간 내에 끝난다. 신기

