# Python 

## pro level3 여행경로

https://programmers.co.kr/learn/courses/30/lessons/43164

> ![image-20210618154947471](md-images/image-20210618154947471.png)



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
'''
icn : b a
b : icn
a : d
d : a
'''
res = []
def solution(tickets):
    answer = [] # 중간 결과 저장값
    n, country = len(tickets), set()
    
    # 몇 개의 나라가 distinct하게 존재하는지 확인
    for i in range(n):
        for j in range(2):
            country.add(tickets[i][j])
            
    # stoe는 각 나라마다 도착할 나라가 몇 개있는지 측정하는 배열
    country, stoe = list(country), [[] for _ in range(len(country))]
    # 나라 방문 표시
    v = [[] for _ in range(len(country))]
    
    # 도착지 배열에 삽입
    for i in range(n):
        for j in range(len(country)):
            if country[j] == tickets[i][0]:
                stoe[j].append(tickets[i][1])
                break
    
    # 알파벳 작은 순서대로 정렬
    # stoe[i].sort(), stoe[i] = sorted(stoe[i])
    for i in range(len(stoe)):
        stoe[i].sort()
    
    # 맨출발지는 icn이니 첫번째에 있는 출발지와 순서를 바꿔줌.
    for i in range(len(country)):
        if country[i] == 'ICN':
            country[i], country[0] = country[0], country[i]
            stoe[i], stoe[0] = stoe[0], stoe[i]
            break
    
    # v도 stoe에 맞게 배열 만들어줌
    for i in range(len(stoe)):
        v[i] = [0] * len(stoe[i])
    
    # 방문탐색 하면서 아직 방문하지 않은 경로로 가는데
    # 만약 결과값이 티켓 길이의 +1만큼 채워졌다면
    # 정답이 나온 것이므로 return 하고 끝내기
    def dfs(c):
        global res
        for i in range(len(country)):
            if c == country[i]:
                for j in range(len(stoe[i])):
                    if not v[i][j]:
                        v[i][j] = 1
                        answer.append(stoe[i][j])
                        if len(answer) == n + 1:
                            res = answer[:]
                            return
                        dfs(answer[-1])
                        if not res:
                            answer.pop()
                            v[i][j] = 0
                        else:
                            return
    
    answer.append('ICN')
    dfs('ICN')
    
    return res
```

> 뭔데 푸는데 이렇게 오래걸렸지?
>
> sort와 sorted 헷갈렸다. 너무 오랜만에 정렬시켜봐서 그런듯.
>
> 그리고 바보 같이 sort를 계속 수정해 줄 거면서 v를 초기에 선언해 버렸다. (인덱스 에러)
>
> 또, 문제는 global이었다. global은 def 밖에 있는 변수를 불러오는 건데, 이중 def를 쓰다보니 헷갈림.. 그부분에서 시간좀 잡아 먹었다. (global로 선언한 거 not defined)



* 모범답안

  ```python
from collections import defaultdict
  
  def dfs(graph, N, key, footprint):
  
      if len(footprint) == N + 1:
          return footprint
  
      for idx, country in enumerate(graph[key]):
          graph[key].pop(idx)
  
          tmp = footprint[:]
          tmp.append(country)

          ret = dfs(graph, N, country, tmp)
  
          graph[key].insert(idx, country)
  
          if ret:
              return ret
  
  
  def solution(tickets):
      answer = []
  
      graph = defaultdict(list)
  
      N = len(tickets)
      for ticket in tickets:
          graph[ticket[0]].append(ticket[1])
          graph[ticket[0]].sort()
  
      print(graph)
  
      answer = dfs(graph, N, "ICN", ["ICN"])
  
      return answer
  ```
  
  > - `graph = defaultdict(list)`
  >   - 이게 진짜 개쩌는 구문인 게,, 내가 그간 열심히 찾아봤던 함수임. 이렇게 선언할 수 있구나 쩐다,, collections from 이구나
  > - `for idx, country in enumerate(graph[key])`
  >
  > 이 코드에서 약간 에러는 pop이랑 insert를 인덱스를 찾아서 한다는 건데, 그럼 시간 복잡도가 N이된다. 

