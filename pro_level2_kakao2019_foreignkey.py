# Python

## pro level2 후보키

https://programmers.co.kr/learn/courses/30/lessons/42890#qna



> ![image-20210531235009536](md-images/image-20210531235009536.png)



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
[(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

'''

from itertools import combinations
# 조합을 통한 계산


def solution(relation):
    answer = []
    n = list(i for i in range(len(relation[0])))
    # 테이블의 속성 개수.
    cnt = 1
    while len(n) >= cnt:
    # 속성의 개수를 갖고 조합을 돌린다.
        for comb in combinations(n, cnt):
        # 현재의 속성 조합을 for문으로 돌리면서
            count = 0
            # 현재 뽑아낸 조합 중
            flag = True
            dicgttwo, dicone = [], {}
            # 여러 개의 속성값을 비교할 때와 하나의 속성값만을 비교할 때,
            # []는 초기화를 해줘야 하지만, {}는 초기화를 안해줘도 됨.
            for idx in comb:
            # 속성값을 idx로
                if cnt == 1:
                    # 만약 현재 비교할 속성값이 1개라면
                    for i in range(len(relation)):
                        if relation[i][idx] in dicone:
                            flag = False
                            break
                        else:
                            dicone[relation[i][idx]] = 1
                else:
                    count += 1
                    for i in range(len(relation)):
                        if len(dicgttwo) == len(relation):
                            if count == len(comb):
                                if dicgttwo[i] + str(relation[i][idx]) in dicgttwo:
                                    flag = False
                                    break
                                else:
                                    dicgttwo[i] += str(relation[i][idx])
                            else:
                                dicgttwo[i] += str(relation[i][idx])
                        else:
                            dicgttwo.append(str(relation[i][idx]))
                if not flag:
                    break
            if not flag:
                continue
            answer.append(comb)
        cnt += 1

    print(answer)
    result = []
    for i in range(len(answer)):
        tmp, tmpflag = ''.join(map(str, answer[i])), True
        for j in range(len(result)):
            cnt = 0
            for k in range(len(result[j])):
                if result[j][k] in tmp:
                    cnt += 1
            if cnt == len(result[j]):
                tmpflag = False
                break
        if tmpflag:
            result.append(tmp)
    print(result)

    return len(result)
```

> 



* 모범답안

  ```python
  from itertools import combinations
  def solution(relation):
      n_row=len(relation)
      n_col=len(relation[0])  #->runtime error 우려되는 부분
  
      candidates=[]
      for i in range(1,n_col+1):
          candidates.extend(combinations(range(n_col),i))
  
      final=[]
      for keys in candidates:
          tmp=[tuple([item[key] for key in keys]) for item in relation]
          if len(set(tmp))==n_row:
            final.append(keys)
  
      answer=set(final[:])
      for i in range(len(final)):
          for j in range(i+1,len(final)):
              if set(final[i])==set(final[i]).intersection(set(final[j])):
                  answer.discard(final[j])
  
      return len(answer)
  ```
  
  > - extend
  >   - append와 유사한 함수인데 또 다르다
  >   - 만약 x = [1,2,3], y=[4,5] 있을 때. x에 y를 append하면 [1,2,3,[4,5]]처럼 나오지만 extend를 쓰면 [1,2,3,4,5]로 출력됨
  > - intersection
  >   - 교집합을 찾아내는 함수
  > - discard
  >   - remove와 유사한 함수인데 다르다.
  >   - a=[10] 일 때, a.remove(10), a.remove(10)하면 오류 발생하나, a.discard하면 오류발생하지 않는다. 
  >   - 엄청 잘 활용될 함수일듯..

