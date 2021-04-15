# python

## swea 4366 d4 정식이의 은행업무

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd



> 

* 문제

  > 
  
* 입력

  > 
  >
  > ```bash
  >
  > ```
  
* 출력

  > 
  >
  > ```bash
  >
  > ```



```python
for tc in range(1, int(input())+1):
    arr, flag = [], False
    # flag는 이미 맞았으면 더이상 반복문을 돌 필요 없으므로
    # 반복문을 빠져나올 flag.
    for _ in range(2):
        arr.append(input())
        # 2진수와 3진수를 넣어줌
    for i in range(len(arr[0])):
    # 3진수는 복잡하기 때문에 2진수 숫자를 변형해 줄 거임.
        tmp = list(arr[0][:])
        # list형태로 바꿔줘야 0->1로 바꿀 수 있음
        tmp[i] = str(int(not int(tmp[i])))
        # 0이면 1로 1이면 0으로 바꿔주고
        # str형태로 다시 제자리에 넣어줌
        decnum = int('0b'+''.join(tmp), 2)
        # 현재 바뀐 2진수를 10진수로 변형.
        dectoth = ''
        # 10 to 3 => 바뀐 10진수를 3진수로 바꿔줌
        while decnum > 0: # 3진수로 바꾸는 과정
            dectoth += str(decnum % 3)
            decnum //= 3
        dectoth = dectoth[::-1]
        diff = 0
        if len(arr[1]) == len(dectoth):
        # 기존의 3진수와 바뀐 3진수의 자릿수가 같다면
            for j in range(len(arr[1])):
                if arr[1][j] != dectoth[j]:
                # 숫자 다른 거 세기
                    diff += 1
                if diff > 1:
                # 하나 이상 다르다면 볼 필요 없으니 break
                    break
        if diff == 1:
        # 한 개 다르다면
            flag = True
            print('#%d %d' % (tc, int('0b'+''.join(tmp), 2)))
            # 출력하고
            break
            # 종료
        else:
            continue
    if flag:
        continue
```

> - `decnum = int('0b'+''.join(tmp), 2)` : 헐.. 0b빼도 됨. 암튼 첫번째 인자(2진수)를 10진수로 바꾸는 코드



* 모범답안

  ```python
  T = int(input())
  for tc in range(1, T+1):
      B = input()
      T = input()
      listB = []
      for i in range(len(B)):
          Temp = list(B)
          Temp[i] = str((int(B[i]) + 1) % 2)
          listB.append(int(''.join(Temp), 2))
   
      result = -1
      for i in range(len(T)):
          Temp = list(T)
          for j in range(1, 3):
              Temp[i] = str((int(T[i]) + j) % 3)
              if int(''.join(Temp), 3) in listB:
                  result = int(''.join(Temp), 3)
                  break
          if result > -1:
              break
      print('#{} {}'.format(tc, result))
  ```
  
  > 헐??
  >
  > `Temp[i] = str((int(T[i]) + j) % 3)`
  >
  > 이거 3진수도 된다. 왜 안해봤지? 이것만 했었어도 코드 대폭 줄였을 텐데..