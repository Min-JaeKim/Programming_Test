# Python 

## pro level1 완주하지 못한 선수

https://programmers.co.kr/learn/courses/30/lessons/42576

> ![image-20210617095350273](md-images/image-20210617095350273.png)



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
def solution(participant, completion):
    dic = {}
    for c in completion:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    for p in participant:
        if p not in dic:
            return p
        dic[p] -= 1
    for key, value in dic.items():
        if value < 0:
            return key
```

> 근데 내가 훨빠르네;;



* 모범답안

  ![image-20210617082911527](md-images/image-20210617082911527.png)

  ```python
  from collections import Counter
  
  def solution(participant, completion):
      return list((Counter(participant)-Counter(completion)))[0]
  ```

  > counter만 썼을 시 출력은
  >
  > {'leo':1} 이렇게 나온다.

