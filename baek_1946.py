# python

## baek 1946

https://www.acmicpc.net/problem/1946



> 6996ms



* 문제

  > 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.
  >
  > 그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
  >
  > 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.
  >
  > ```python
  > 2
  > 5
  > 3 2
  > 1 4
  > 4 1
  > 2 3
  > 5 5
  > 7
  > 3 6
  > 7 3
  > 4 2
  > 1 4
  > 5 7
  > 2 5
  > 6 12
  > 10
  > 15
  > ```
  >
  > 

* 출력

  > 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.
  >
  > ```python
  > 4
  > 3
  > ```



```python
case = int(input())
case_count = []

for i in range(case):
    count = 1
    people = int(input())
    arr = [[0] * 2 for _ in range(people)]
    
    for j in range(people):
        arr[j][0],arr[j][1] = map(int, input().split())
        
    arr = sorted(arr)
    min_v = arr[0][1]
    
    for j in range(people-1):
        j += 1
        if arr[j][1] > min_v:
            continue
        else :
            min_v = arr[j][1]
            count+=1
            
    case_count.append(count)
    
for i in range(len(case_count)):
    print(case_count[i])
```

> 말두 안된다... 이런 별 것도 아닌 것 같은 문제를 3시간이나 붙잡고 있는 게 정말 말도 말도 안된다..
>
> 그래도 답을 보지 않았다는 것에 위안을 삼아야겠다. 이문제를 통해 알아낸 것은,
>
> 1. 3중 for문은 웬만하면 시간초과 뜨니까 조금 더 효율적인 코드 작성을 해야 한다는 것.
> 2.  그리고 오히려 단순하게 생각할 수록 답이 더 금방나올 수 있다는 점. sort를 했기 때문에 else 구문을 쉽게 작성할 수 있었음에도 그것을 망각하고 있었다. 조금 더 쉽게 풀 수 있는 방법을 터득하는 것이 중요해 보인다.



* 계속 틀렸던 답안

  ```python
  case = int(input())
  
  for i in range(case):
      doc_list = []
      view_list = []
      people = int(input())
      d,v = map(int, input().split())
      doc_list.append(d)
      view_list.append(v)
      
      for j in range(people-1):
          d,v = map(int, input().split())
          for m in range(len(doc_list)):
              if doc_list[m] > d and view_list[m] > v:
                  doc_list[m] = d
                  view_list[m] = v
                  # print(len(doc_list))
                  break
              elif doc_list[m] < d and view_list[m] < v:
                  # print(len(doc_list))
                  break
              else:
                  if m == len(doc_list) - 1:
                      doc_list.append(d)
                      view_list.append(v)
                      # print(len(doc_list))
              
      print(len(doc_list))
      
      
  
   # 접근은 나쁘지 않았던 것 같다. 계속해서 앞 사람과 비교하며 해당 사람의 두 점수가 앞 사람들의 점수보다 미달된다면 가차없이 결과리스트에 넣지 않았다. 하지만 이렇게 하니 repl.it에서는 돌아갔지만 백준에서 시간초과로 돌아가지 않았다.
  ```

  

* 모범답안

  ```python
  import sys
  input = sys.stdin.readline
  t = int(input())
  for i in range(t):
      n = int(input())
      s = [0 for i in range(n + 1)]
      for j in range(n):
          a, b = map(int, input().split())
          s[a] = b
      min_n = s[1]
      cnt = 0
      for k in range(2, n + 1):
          if s[k] > min_n:
              cnt += 1
          else:
              min_n = s[k]        
      print(n - cnt)
  ```

  > 이분은 어떻게 이렇게 짧게 코드를 작성 했는지 궁금하다. 보다보면 나랑 접근 방식에는 크게 차이가 없는 것 같다.
  >
  > * sys.stdin.readline : 여러 줄을 입력 받는 건데, 지금 저 코드에는 저게 없어도 출력이 정상적으로 나온다. 다만, 매 케이스마다 결과값이 하나의 케이스가 끝날 때마다 나오는 것이 아닌, 내가 작성한 코드처럼 한 번에 나옴.
  > * 또 정말 충격적인 것은, 정렬과 2차원 배열을 사용하지 않고, 일차원 배열에 순위를 각각 넣었다는 것이다. 정말 효율적으로 풀었다고 생각한다.