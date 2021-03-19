# Python

## pro level1 비밀지도

https://programmers.co.kr/learn/courses/30/lessons/17681



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
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp1, tmp2, answertmp = deque([]), deque([]), ''
        while arr1[i] > 0:
            tmp1.appendleft(arr1[i] % 2)
            arr1[i] //= 2
        while arr2[i] > 0:
            tmp2.appendleft(arr2[i] % 2)
            arr2[i] //= 2
        while len(tmp1) < n:
            tmp1.appendleft(0)
        while len(tmp2) < n:
            tmp2.appendleft(0)
        for _ in range(n):
            answertmp +=  '#' if tmp1.popleft() | tmp2.popleft() else ' '
        answer.append(answertmp)
    return answer
```

> 



* 모범답안

  ```python
  def solution(n, arr1, arr2):
      answer = []
      for i in range(n):                              # 반복문을 돌면서
          tmp = str(int(bin(arr1[i] | arr2[i])[2:]))  # or연산 -> 이진법(문자열) -> 숫자로 바꾼 뒤 -> 문자로 바꿈 == 2|1 -> '0b11' -> 11 -> '11'
          tmp = tmp.rjust(n, '0')                     # 오른쪽정렬 == '00011'
          tmp = tmp.replace('0', ' ')                 # 0인 글자들은 모조리 공백처리 '   11'
          tmp = tmp.replace('1', '#')                 # 1인 글자들은 '#'처리 '   ##'
          answer.append(tmp)                          # 결과 배열에 삽입
  
      return answer
  
  
  '''
  9 / 2 = 4 ... 1
  4 / 2 = 2 ... 0
  2 / 2 = 1 ... 0
  1
  '''
  ```
  
  > bin : 이진법
  >
  > rjust : 오른쪽 정렬
  >
  > replace : 글자 변환