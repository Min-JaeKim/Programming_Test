# Python

## pro level2 순위검색

https://programmers.co.kr/learn/courses/30/lessons/72412



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

```

> 



* 모범답안

  ```python
  def solution(info, query):
      data = dict()
      for a in ['cpp', 'java', 'python', '-']:
          for b in ['backend', 'frontend', '-']:
              for c in ['junior', 'senior', '-']:
                  for d in ['chicken', 'pizza', '-']:
                      data.setdefault((a, b, c, d), list())
      for i in info:
          i = i.split()
          for a in [i[0], '-']:
              for b in [i[1], '-']:
                  for c in [i[2], '-']:
                      for d in [i[3], '-']:
                          data[(a, b, c, d)].append(int(i[4]))
  
      for k in data:
          data[k].sort()
  
          # print(k, data[k])
  
      answer = list()
      for q in query:
          q = q.split()
  
          pool = data[(q[0], q[2], q[4], q[6])]
          find = int(q[7])
          l = 0
          r = len(pool)
          mid = 0
          while l < r:
              mid = (r+l)//2
              if pool[mid] >= find:
                  r = mid
              else:
                  l = mid+1
              # print(l, r, mid, answer)
          # answer.append((pool, find, mid))
          answer.append(len(pool)-l)
  
      return answer
  ```
  
  > 덕분에 이분탐색을 배웠다..
  >
  > - **data.setdefault((a, b, c, d), list())** : 이거는 딕셔너리를 초기화하는 내장 함수
  > - **data[(a, b, c, d)].append(int(i[4]))** : 딕셔너리는 append가 아니기 때문에 초반부터 list로 초기화해줬다.
  > - **for k in data:
  >           data[k].sort()** : 이렇게만 해도 딕셔너리 키값을 통해 정렬가능 ;;
  > - **l = 0
  >           r = len(pool)
  >           mid = 0
  >           while l < r:
  >               mid = (r+l)//2
  >               if pool[mid] >= find:
  >                   r = mid
  >               else:
  >                   l = mid+1** : 이분탐색이거 right값은 길이의 -1이 아닌 길이 그자체로 변수를 줘야 한다. 그리고 else에 걸리면 l을 하나씩 더하는 것이 아닌 mid값에서 1을 더해야함

