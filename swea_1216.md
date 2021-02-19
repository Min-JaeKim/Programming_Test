# python

## swea d3 1216 회문1

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi



> 3255ms



* 문제

  > "기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
  >
  > 주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
  >  
  >
  >  ![img](md-images/fileDownload.do)
  >
  > 
  > 위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.
  >
  > 예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.
  >
  > **[제약사항]**
  >
  > 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
  >
  > 글자 판은 무조건 정사각형으로 주어진다.
  >
  > ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
  >
  > 가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다. 
  >  
  >
  > ![img](md-images/fileDownload.do)

* 입력

  > 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
  >
  > 총 10개의 테스트케이스가 주어진다.
  >
  > ```bash
  > 1
  > CCBBCBAABCCCBABCBCAAAACABBACCCCACAABCBBACACAACABCBCCB...
  > ACBAAAACCACCCBAACAAABACACCABCBCBABBBACBABCAACCBCCACBC...
  > CCCACCBCBACBACBCABAABABCCAAAACCCCCBBAABBCCBCCCABBACAC...
  > CABACBCBBCBABACABBBBBBABBCABCBCBCAABCBCCCBABACCCCABBA...
  > BCCBCCACCBCBCABBBCCABAACACCBCCCBCCACCBBCBCCCBBCCBACBC...
  > BBBBCBBAACABACCBCBCCABBBBCCAABCBBCACCBBCAAAABABABBABB...
  > ABBAACCCACBBABBABCCCABABCACABABACCCBACACABCBCCCBABCCC...
  > ABBBBAABCAACCBACBBAACACABCABACBAABCAABBCCCCCCACBCCCCA...
  > ACCACABABBACBBAACCBBACBBCCACCACCABCCBABABBBACBACBAABC...
  > BABACACCABCAACBAABCCACCACBCCAABBCBAABABAACAAAAAACCCBC...
  > ...
  > 2
  > CBBABBACCAACCCAABABAACCABCBBCCABABBBBBCCACBCCCCBBBAAC...
  > BBBCBACAAABAACACBCAABBAAABCABBBCAAACBAABCAAAAACBABBAB...
  > CAAAABCAABAACCBBABCCCACABABACBCCBCCBABABBCCCBCBACAAAC...
  > BBBACBBBBBAACBBCBABBCBAABACCCBBBBCCCBBBCABCABCAABCBCA...
  > ABBBBAABCBACCACBBCBBAABABCBCCAAABBCAAABBAABBCACABAABA...
  > ABCBACAAACCCAAABCACABBAABBCAACCBABCCACBABBBABAABAACBB...
  > ACACABCBAAACCACABABBCABCBABAAABCBCCABABCCAACACBCBABCA...
  > ACCBACACCAAAABABACABABBBBABBAABABBBBACBACABABACACACAA...
  > AAACCCCCBCAACCCCCAAAACBCACBBABBBBBABABBCCCCBBAACCBBCB...
  > CCABCCBBCAAAACACBBBBAAAACABACABCCCBACBABBACCAABAAACAB...
  > ```

* 출력

  > \#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
  >
  > ```bash
  > #1 18
  > #2 17
  > ```



* 제출

  ```python
  for tc in range(1,11): # 10 개의 테스트 케이스
      n = int(input()) # 몇 번째 테케인지 입력
      arr = [] # 문자열 저장 리스트
      for i in range(100): # 100칸을 돌면서 
          tmp = list(input()) # 문자열을 임시 변수에 저장
          arr.append(tmp) # 배열에 저장
      count = 0 # 최고 회문의 길이
      m = 2 # 회문을 계산할 임시 변수
      for i in range(100): # 100줄을 돌면서
          for j in range(100 - count + 1): # 최고 길이 이하는 구할 필요가 없으므로,
              while j+m <= 100: # 슬라이스를 고려한 <=
                  if arr[i][j:j + m] == list(reversed(arr[i][j:j + m])): # 만약 전체 길이를 따졌을 때 회문이라면
                      if count < m: # 또한 최고길이가 현재 회문인 길이보다 작다면 
                          count = m # 최고 길이를 바꿔줌
                          m += 1 # 그리고 현재 진행 중인 회문의 길이를 늘려 더 긴 회문을 찾으러 떠난다.
                      else: # else없이 걍 break으로 빠져나가면 됨 이코드는 불필요한 코드.
                          break
                  else: # 만약 회문이 아니라면
                      m += 1 # 현재 비교중인 길이를 늘려 회문을 구한다.
              if count != 0: # 회문인 것을 찾고, 다음 행으로 넘어가야 한다면,
                  m = count # 최고길이를 m에 넣어줌
              else: # 회문인 것을 하나도 찾지 못했는데 넘어 가야 한다면,
                  m = 2 #  기본 값 2를 넣어줌
      for i in range(100): # 행과 열을 뒤집어서 비교해 주기 위해 
          for j in range(100): # 행 100칸 열 100칸
              if i > j: # 만약 대각선으로 긋고 밑에 있는 배열들이라면
                  arr[i][j], arr[j][i] = arr[j][i], arr[i][j] # 위에 있는 칸들과 교환
              else: # 그게 아니라면 더 비교해 볼 필요 없으니
                  break # 시간 줄이기 위해 break
      for i in range(100): # 이번에는 행과 열을 바꾼 뒤 회문 찾기
          for j in range(100 - count + 1): # 인덱스를 초과하지 않기 위해
              while j+m <= 100:  # 슬라이스를 고려한 <=
                  if arr[i][j:j + m] == list(reversed(arr[i][j:j + m])):
                      if count < m:
                          count = m
                          m += 1
                      else:
                          break
                  else:
                      m += 1
              if count != 0:
                  m = count
              else:
                  m = 2
      print('#%d %d' % (tc, count))
  ```

  > 효율적이게 짜는 방법을 고려해야겠다.
  >
  > 나도 좀 더 영리하고 혁신적인 방법으로 풀 수 있었으면 좋겠다. 그러기 위해선 파이썬 문법을 꼼꼼히 알아가는 게 중요하다

  

* 모범답안

  ```python
  1700ms
  
  import sys
  sys.stdin = open('./input.txt')
  
  def my_func(n):
      for i in range(100):
          for j in range(100-n+1):
              tmp = arr[i][j:j+n]
              tmp2 = rearr[i][j:j+n]
              if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                  return n
      return 0
  
  
  for tc in range(1,11):
      n = int(input())
      arr = [input() for _ in range(100)]
      rearr = list(zip(*arr))
  
      for i in range(99, 1, -1):
          ans = my_func(i)
          if ans != 0:
              break
      print("#%d %d" % (tc, ans))
  ```
  
  > 높은 숫자부터 내려 가는 함수.. 대박대박
  >
  > * __zip(*a)__ : 하나로 압축할 수 있는 내장함수 

