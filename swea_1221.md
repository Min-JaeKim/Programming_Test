# python

## swea d3 1221 GNS

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD



> 177ms ~ 301ms



* 문제

  > 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
  >
  > **"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"**
  >
  > 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
  >
  > 예를 들어 입력 문자열이 **"TWO NIN TWO TWO FIV FOR"** 일 경우 정렬한 문자열은 **"TWO TWO TWO FOR FIV NIN"** 이 된다.

* 입력

  > 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
  >
  > 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
  >
  > 그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.
  >
  > ```bash
  > 10
  > #1 7041
  > SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT FIV SVN SIX ONE EGT NIN TWO SVN NIN FIV FOR THR ONE TWO THR THR FOR ONE ONE THR EGT SVN FOR TWO SVN SVN NIN THR ONE NIN EGT SIX FIV ZRO TWO EGT SIX ZRO TWO FOR EGT SIX FIV ZRO NIN ZRO ZRO SIX ONE THR EGT NIN THR FOR FOR SIX ZRO SIX SIX ONE...
  > #2 7778
  > EGT ONE THR SIX ZRO ZRO NIN FIV FOR EGT SVN FOR NIN NIN EGT THR EGT FIV TWO ONE FIV THR ONE SIX SVN THR ZRO FIV TWO TWO ONE FIV ZRO TWO SIX TWO EGT THR SIX SVN FOR FIV THR SVN SVN EGT EGT FOR ZRO THR FIV EGT NIN THR ONE SVN ZRO NIN THR THR FIV SVN THR SIX FOR NIN FOR ZRO ZRO NIN SVN EGT SIX FIV TWO TWO THR FIV THR SVN NIN ONE ZRO FIV ZRO NIN THR SIX ...
  > ```

* 출력

  > \#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.
  >
  > ```bash
  > #1
  > ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ...
  > #2
  > ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ...
  > ```



* 제출

  ```python
  import sys
  sys.stdin = open('./GNS_test_input.txt')
  
  testc = int(input())
  eng = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
  for tc in range(1,testc+1):
      n = input()
      arr = input().split()
      sor = []
      for i in range(len(eng)):
          for j in range(len(arr)):
              if eng[i] == arr[j]:
                  sor.append(arr[j])
      print("#%d" % (tc))
      for i in sor:
          print(i, end = ' ')
  ```

  > 처음에는 너무나도 단순히 작성하고 제출했다. 이게 진짜 좋은 코드가 아니라는 증거는,, 입력된 arr를 10번이나 반복하기 때문이다. 정말 끔찍하다 코드가..

  

* 모범답안

  ```python
  177ms
  testc = int(input())
  eng = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
  for tc in range(1,testc+1):
      n = input()
      arr = input().split()
      sor = [0 for _ in range(10)]
      for i in arr:
          idx = eng.index(i)
          sor[idx] += 1
      result = []
      for i in range(len(eng)):
          result += [eng[i]] * sor[i]
           
      print("#%d" % (tc))
      print(' '.join(result))
  ```

  > 진짜 대단하다고 느꼈던 코드. 단순히 index 내장함수를 사용했을 뿐인데 arr를 한 번 밖에 안돌고도 결과를 구할 수 있었다. 대단하다.

  ```python
  177ms
  testc = int(input())
  for tc in range(1, testc+1):
      eng = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
      n = input()
      arr = input().split()
      for i in arr:
          eng[i] += 1
      res = ''
   
      for key, value in eng.items():
          tmp = ' '.join([key]*value)
          res += tmp + ' ' # zro 다음 one을 출력할 때 띄어쓰기
   
      print("#%d" % (tc))
      print(res[:len(res)-1]) # 마지막에 띄어쓰기가 포함되어 있으므로 삭제
  ```

  > 처음에 봤던 모범답안,, 딕셔너리를 사용했는데 나는 딕셔너리 사용법을 잘 몰라서 애를 먹었다. 
  >
  > * 키만 출력하고 싶은 경우
  >
  >   ```python
  >   >>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
  >   >>> for key in x.keys():
  >   ...     print(key, end=' ')
  >   ...
  >   a b c d
  >   ```
  >
  > * 값만 출력하는 경우
  >
  >   ```python
  >   >>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
  >   >>> for value in x.values():
  >   ...     print(value, end=' ')
  >   ...
  >   10 20 30 40
  >   ```
  >
  >   key와 value 내장함수를 사용.
  >
  > .
  >
  > 둘다 출력하고 싶은 경우 items()함수를 사용할 수 있었다.
  >
  > * __tmp = ' '.join([key]*value)__ : 키 값을 꼭 대괄호로 사용해야함.
  >
  >   ```python
  >   print(' '.join(['hello'] * 3))
  >   >>hello hello hello
  >   print(' '.join('hello'*3))
  >   >>h e l l o h e l l o h e l l o
  >   ```
  >
  >   

  

