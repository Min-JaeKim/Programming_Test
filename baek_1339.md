# Python

## baek 1339

https://www.acmicpc.net/problem/1339



> 164ms



* 문제

  > 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
  >
  > 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
  >
  > 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.
  >
  > N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.
  >
  > ```python
  > 2
  > AAA
  > AAA
  > ```
  >

* 출력

  > 첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.
  >
  > ```python
  > 1998
  > ```



```python
alpha = [0 for _ in range(26)] # alpha의 배열을 지정
n = int(input()) # 몇 개의 문자열을 받을 건지,

for i in range(n):
    i = 0	# 가중치
    st = input() # 문자열.
    while len(st) > 0:	# 문자열의 길이가 0보다 크면
        s = st[-1]	# 문자열의 끝의 글자를 받아와서
        alpha[(ord(s) - ord('A'))] += pow(10,i) # 알파벳 배열에 가중치와 함께 저장.
        i+=1	# 자릿수를 높여갈 때 가중치도 up
        st = st[:-1]	# 마지막 문자열의 가중치를 계산했으므로 문자열에서 제외.
        
alpha.sort(reverse = True)	# 가중치의 내림차순으로 정렬
result = 0	# 결과 초기화
index = 9	# 높은 가중치를 갖고 있으면 앞자리 글자였으므로 9 곱셈

for i in alpha:	# 알파 배열 동안
    result += i * index	# 결과에 곱셈 * 가중치
    index -= 1	# 곱셈 수는 점점 내려가고,
    
print(result)
```

> 항상 느끼는 건데, 다른 모범적인 풀이를 보면 참 쉽게 풀린다는 것이다. 애초에 어렵게 생각하면 안되는데 아직 그게 좀 서툰 것 같다.
>
> * __ord('A')__ : 'A'를 숫자로 표현하기. EX) 65
> * __pow(10,i)__ : 제곱 표현, 10의 i승.
> * __alpha.sort(reverse = True)__ : alpha의 정렬.



* 모범답안

  ```python
  t = int(input())
  
  ss = []
  
  for _ in range(t):
      ss.append(input())
  
  alphabet = [0 for i in range(26)]
  
  for s in ss:
      i = 0
      while s:
          now = s[-1]
          alphabet[ord(now) - ord('A')] += pow(10, i)
          i += 1
          s = s[:-1]
  
  alphabet.sort(reverse=True)
  ans = 0
  for i in range(9, 0, -1):
      ans += i * alphabet[9 - i]
  print(ans)
  
  ```
  
  > 재미있는 문제였다.
  >
  > * __ss.append(input())__ : append와 입력값을 동시에.