# Python

## pro level1 신규 아이디 추천

https://programmers.co.kr/learn/courses/30/lessons/72410



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
def solution(new_id):
    answer = ''
    # 1단계
    new_id = list(new_id.lower())
    # 2단계
    i = 0
    while i < len(new_id):
        if new_id[i].isdigit() or new_id[i].isalpha() or \
        new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            pass
        else:
            new_id.remove(new_id[i])
            i -= 1
        i += 1
    # 3단계
    i = 0
    while i < len(new_id):
        if new_id[i] == '.' and new_id[i-1] == '.':
            for j in range(i,len(new_id)):
                new_id[j-1] = new_id[j]
            new_id.pop()
            i -= 1
        i += 1
    # 4단계
    while new_id and new_id[0] == '.':
        new_id.pop(0)
    while new_id and new_id[-1] == '.':
        new_id.pop()
    # 5단계
    if len(new_id) == 0:
        new_id.append('a')
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id and new_id[-1] == '.':
            new_id.pop()
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    print(''.join(new_id))
    answer = ''.join(new_id)
    return answer
```

> 



* 모범답안

  ```python
  import re
  
def solution(new_id):
      st = new_id
      st = st.lower()
      st = re.sub('[^a-z0-9\-_.]', '', st)
      st = re.sub('\.+', '.', st)
      st = re.sub('^[.]|[.]$', '', st)
      st = 'a' if len(st) == 0 else st[:15]
      st = re.sub('^[.]|[.]$', '', st)
      st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
      return st
  ```
  
  > 정규식으로 푸는 거라는데 이렇게 풀 자신은 없다.