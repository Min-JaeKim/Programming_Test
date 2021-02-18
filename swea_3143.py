# python

## swea d4 3143 가장 빠른 문자열 타이핑

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS



> 187ms



* 문제

  > 어떤 문자열 A를 타이핑하려고 한다.
  >
  > 그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.
  >
  > 여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
  >
  > 이미 타이핑 한 문자를 지우는 것은 불가능하다.
  >
  > 예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이 B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.
  >  
  > ![img](data:image/png;base64,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)
  >
  > A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스마다 첫 번째 줄에 두 문자열 A, B가 주어진다. A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하이다.
  >
  > ```bash
  > 2
  > banana bana
  > asakusa sa	//Test Case의 개수
  > //A=”banana”, B=”bana”
  > //A=”asakusa”, B=”sa”
  > ```

* 출력

  > 각 테스트 케이스마다 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 출력한다.
  >
  > ```bash
  > 
  > #1 3
  > #2 5	//Test Case 1번의 답
  > //Test Case 2번의 답
  > ```



* 제출

  ```python
  TC = int(input()) # 테케 입력
  for tc in range(1, TC+1): # for문
      a, b = input().split() # 문자열 입력받고
      aidx, bidx, result = 0, 0, 0 # 인덱스와 결과를 0으로 초기화
      while aidx < len(a): # a인덱스가 a문자 길이보다 작은 동안에,
          if a[aidx:aidx + len(b)] == b[:] # 만약 문자열이 겹친다면 
              result += 1  # 결과는 하나만 증가
              aidx += len(b) # 그리고 인덱스도 그만큼 증가
          else: # 일치하지 않는다면
              result += 1 # 결과 증가
              aidx += 1 # 인덱스도 한 칸 이동
  
      print('#%d %d' % (tc, result)) # 결과 출력
  ```

  > 헷갈렸더니 테케가 하나도 맞지 못한채로 fail 떴다.
  >
  > 그 이유는 b의 일부만 a에 맞아도 그 문자열에게 특혜를 줬기 때문,
  >
  > b의 온전한 문자열 모든 게 a에 들어 있어야 함.

  

* 모범답안

  ```python
  tc = int(input())
   
  for i in range(tc):
      A,B = input().split()
      print(f'#{i+1} {len(A)-(len(B)-1)*A.count(B)}')
  ```

  > 대박 
  >
  > a문자열 길이에서 b문자열이 들어간 길이만 빼면 된다. 
  >
  > * __a.count(b)__ : a에서 b 문자열이 들어간 개수

