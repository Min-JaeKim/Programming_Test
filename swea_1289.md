# python

## swea 1289

https://swexpertacademy.com/main/solvingProblem/solvingProblem.do



> 



* 문제

  > ※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
  >
  > 원재가 컴퓨터를 만지다가 실수를 저지르고 말았다. 메모리가 초기화된 것이다.
  >
  > 다행히 원래 메모리가 무슨 값이었는지 알고 있었던 원재는 바로 원래 값으로 되돌리려고 했으나 메모리 값을 바꿀 때 또 문제가 생겼다.
  >
  > 메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.
  >
  > 예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.
  >
  > 원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스는 한 줄로 이루어져 있으며, 메모리의 원래 값이 주어진다.
  >
  > 메모리의 길이는 1이상 50이하이다.
  >
  > ```bash
  > 2
  > 0011
  > 100
  > ```

* 출력

  > 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
  >
  > 초기값(모든bit가 0)에서 원래 값으로 복구하기 위한 최소 수정 횟수를 출력한다.
  >
  > ```bash
  > #1 1
  > #2 2
  > ```



```python
T = int(input())
for test_case in range(1, T + 1):
    num = input()
    sig = 0
    result = 0
    for i in range(len(num)):
        if int(num[i]) != sig:
            result += 1
            sig = int(num[i])
    print("#" +str(test_case) + " " + str(result))
```

> 풀이는 쉬웠으나 print문 대문에 처음에 오답이 떴다.
>
> int형과 str형을 함께 print 할 수 없기 때문에 int를 str로 형 변환 시켜줘야 한다.





* 모범답안

  ```python
  T = int(input())
  
  for test_case in range(1, T + 1):
      count = 0
      flag = "0"
      num = input()
      
      for j in range(len(num)):
          if num[j] != flag:
              count += 1
              flag = num[j]
  
      print("#" + str(test_case) + " " + str(count))
  ```
  
  > 굿. 이분도 나처럼 flag를 쓰셨다. 하지만 flag 자체를 문자열로 두어서 훨씬 간편하게  푸셨다.