# python

## baek 9466 텀 프로젝트 골드4

https://www.acmicpc.net/problem/9466

> python3 4180ms

* 문제

  > 이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다. 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.
  >
  > 학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.
  >
  > 예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.
  >
  > | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
  > | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
  > | 3    | 1    | 3    | 7    | 3    | 4    | 6    |
  >
  > 위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.
  >
  > 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

* 입력

  > 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)
  >
  > ```bash
  >2
  > 7
  >3 1 3 7 3 4 6
  > 8
  >1 2 3 4 5 6 7 8
  > ```
  >
  
* 출력

  > 각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.
  >
  > ```bash
  > 3
  > 0
  > ```



```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)


def sol():

    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.insert(0, 0)
        group = n

        v = [0] * (n+1)

        #####################함수#######################

        def recursion(student, stack, dic):
            nonlocal group
            
            # 지금 그룹에 존재하는 학생이라면
            if student in dic:
                while 1:
                    # 그 학생을 만날 때까지 pop 해줌.
                    if stack[-1] == student:
                        stack.pop()
                        group -= 1
                        # 그리고 이 그룹은 종료.
                        return
                    else:
                        stack.pop()
                        group -= 1
            
            # 아직 방문하지 않은 학생이라면 재귀 계속 돌림
            if not v[student]:
                v[student] = 1
                dic[student] = 1
                stack.append(student)
                recursion(arr[student], stack, dic)

        #############################################

        for i in range(1, n+1):
            # 이미 확인한 학생이면 지나침
            if v[i] or v[arr[i]]:
                continue
            v[i] = 1
            recursion(arr[i], [i], {i: 1})

        print(group)


sol()
```

> 도대체가,,, 학생 수가 100000이라 재귀 제한을 100001로 줬는데.. 왜 런타임 에러 나는 걸까... 결국 111111로 주고 나서야 성공했는데 원인을 밝혀내지 못했음...



* 모범답안

  ```python
  def solution(n, students):
      visited = [False] * (n + 1)
      count = 0
  
      for i in range(1, n+1):
          if not visited[i]:
              
              # From current student, move forward until it detects a cycle.
              current = i
              while not visited[current]:
                  visited[current] = True
                  current = students[current]
              
              # When former loop detects a cycle,
              # current value indicates a student from who a cycle formed.
              # So, from i'th student to the student, they cannot belong to any team.
              backtrack = i
              while backtrack != current:
                  backtrack = students[backtrack]
                  count += 1
              
      return count
  
  T = int(input())
  
  for _ in range(T):
      n = int(input())
      students = [0] + list(map(int, input().split()))
  
      print(solution(n, students))
  ```

  > 와 진짜 천재다... dfs 재귀를 안 쓰고도 이렇게 풀 수 있구나.. 대박 하,, 이런 사람들 보면 내가 왜 알고리즘 문제를 푸나 싶어진다.. 대박..
  >
  > 첫번째 while문을 통해 같이 팀을 하고 싶은 학생들을 타고 타고 들어간다(단, 아직 방문하지 않은 학생들이어야 함.) 그리고 맨처음 시작한 학생과 마지막 끝나는 학생이 똑같지 않다면, 외면당하고 있는 학생이 있다는 뜻이므로, 외면 당하는 학생 모두 카운트해줌... 끝.

