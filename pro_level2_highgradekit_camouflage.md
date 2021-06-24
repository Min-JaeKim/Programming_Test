# Python 

## pro level2 위장

https://programmers.co.kr/learn/courses/30/lessons/42578

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
from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth = defaultdict(list)
    
    for c, k in clothes:
        cloth[k].append(c)
        
    for c in cloth:
        answer *= (len(cloth[c]) + 1)
    
    return answer-1
```

>처음에 옷 가짓수를 조합을 통해 결정하였다. 그러다 1번을 틀렸는데 내가 생각해도 통과 못 할 것이라고 생각했다. 왜냐하면 최대 옷 개수는 30개라고 했기 때문,, 휴,, ㅠㅠ
>
>저번에도 이 문제를 풀어 본 적 있는데 왜 틀렸지? 암튼 이렇게 푸는 게 아니라.. 전체 옷 분류에 따른 옷 개수를 모두 곱한 다음 공집합을 때인 1을 빼주는 것이다. 이제 잊지 말아야지



* 모범답안

  

  ```python
  def solution(clothes):
      from collections import Counter
      from functools import reduce
      cnt = Counter([kind for name, kind in clothes])
      print(cnt)
      answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
      return answer
  ```

  > 으아아아아앙 reduce모르겠다. 진심.. counter까진 어떻게 이해해 봤는데 파이써닉한 코드는 너무 어렵다.

