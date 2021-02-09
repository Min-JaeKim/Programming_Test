# python

## swea d3 5789 현주의 상자 바꾸기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm&categoryId=AWYygN36Qn8DFAVm&categoryType=CODE&problemTitle=5789&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



> 599ms



* 문제

  > 현주는 1번부터 N번까지 N개의 상자를 가지고 있다. 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.
  >
  > 숫자가 너무 단조로웠던 현주는 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다. 변경하는 방법은 다음과 같다.
  >
  >   · i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
  >
  > 현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.
  >
  > 다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.
  >
  > ```bash
  > 
  > 1
  > 5 2
  > 1 3
  > 2 4	// Test Case 개수
  > // 첫 번째 Test Case, N=5, Q=2
  > // i = 1일 때, L=1, R=3
  > // i = 2일 때, L=2, R=4
  > ```

* 출력

  > 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
  >
  > 각 테스트 케이스마다 Q개의 작업을 수행한 다음 1번부터 N번까지의 상자에 적혀있는 값들을 순서대로 출력한다.
  >
  > ```bash
  > 
  > #1 1 2 2 2 0	//첫 번째 테스트케이스 결과
  > ```



```python
import sys
sys.stdin = open('./sample_input.txt')

case = int(input())

for tc in range(1,case+1):
    box,change = map(int, input().split())
    boxes = [0 for _ in range(box)]
    number = 1
    for i in range(change):
        left,right = map(int, input().split())
        for j in range(left-1,right):
            boxes[j] = number
        number += 1
    print("#{}".format(tc), end = " ")
    for i in boxes:
        print(i, end = " ")
    print()
```

> 별로 리뷰할 문제도 아닌데 리뷰하는 이유는 출력하는 방법에 대해 배웠기 때문이다.
>
> **print("#{}".format(tc), end = " ")
>     for i in boxes:
>         print(i, end = " ")
>     print()** 
>
> 이렇게 하면 출력값이 
>
> #케이스번호 배열0 배열 1 배열2 ..
>
> 이런식으로 나온다.



* 모범답안

  ```python
  for idx in range(int(input())):
      n,q = map(int,input().split())
      
      # 박스들 초기화
      boxes = []
      for n_ in range(n):
          boxes.append([n_+1,0])
      # 번호 바꾸기
      for i in range(q):
          l,r = map(int,input().split())
          for box in boxes:
              if l<=box[0]<=r:
                  box[1] = i+1
                  
      # 출력
      print("#{0}".format(idx+1),end=" ")
      for box in boxes:
          print(box[1],end=" ")
      print()
  ```
  
  > 이사람것 출력 값만 보고 제출했는데 보다보니 괜찮아서 가져옴. 너무 불필요하게 반복문을 돌려서 시간이 과하게 나오는 부분만 빼면 배울점이 참 많은 코드라고 생각한다.
  >
  > **for n_ in range(n):
  >         boxes.append([n_+1,0])**
  >
  > **for box in boxes:
  >             if l<=box[0]<=r:
  >                 box[1] = i+1**
  >
  > 이렇게 풀 수도 있구나라는 것을 깨닫게 되었다.