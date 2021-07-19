# python

## baek 5021 왕위 계승 실버1

https://www.acmicpc.net/problem/5021

> python3 108ms

* 문제

  > 유토피아의 왕이 사망했다. 왕은 자손을 남기지 않고 사망했기 때문에, 왕위를 계승할 사람을 지목하지 않았다. 왕실 귀족은 왕위를 주장하기 시작했다. 유토피아의 법에는 왕의 계승자가 없는 경우에, 나라를 세운 사람과 혈통이 가까운 사람이 유토피아를 통치한다는 조항이 있다.
  >
  > 나라를 세운 사람과 혈통이 가장 가까운 사람은 그의 자손이 아닌 사람과 피가 덜 섞인 사람이다. 모든 사람은 아버지의 혈통과 어머니의 혈통을 반 씩 받게 된다. 나라를 세운 사람의 자식은 1/2 왕족이며, 그 아들이 왕족이 아닌 사람과 결혼한 경우에는 아들의 자식은 1/4 왕족이 된다.
  >
  > 가장 나라를 세운 사람과 혈통이 가까운 사람을 찾는 프로그램을 작성하시오. 

* 입력

  > 첫째 줄에 N과 M이 주어진다. (2 ≤ N, M ≤ 50)
  >
  > 둘째 줄에 유토피아를 세운 사람의 이름이 주어진다.
  >
  > 다음 N개 줄에는 가족 정보가 주어진다. 정보는 이름 세 개로 이루어져 있고, 공백으로 구분되어져 있다. 첫 번째 이름은 자식의 이름이고, 뒤의 두 이름은 부모의 이름이다.
  >
  > 다음 M개 줄에는 왕위를 계승받기를 주장하는 사람의 이름이 한 줄에 하나씩 주어진다.
  >
  > 모든 이름은 1~10글자이며, 알파벳 소문자로만 이루어져 있다. 나라를 세운 사람이 왕위를 계승하는 경우나, 누군가의 자식인 경우는 없다. 
  >
  > ```bash
  > 9 2
  > edwardi
  > charlesi edwardi diana
  > philip charlesi mistress
  > wilhelm mary philip
  > matthew wilhelm helen
  > edwardii charlesi laura
  > alice laura charlesi
  > helen alice bernard
  > henrii edwardii roxane
  > charlesii elizabeth henrii
  > charlesii
  > matthew
  > ```
  >
  
* 출력

  > 첫째 줄에 유토피아를 세운 사람과 가장 혈통이 가까운 사람의 이름을 출력한다. 항상 답이 유일한 경우만 입력으로 주어진다.
  >
  > 문제에 주어지는 가족 관계는 성별, 나이를 고려하지 않고 만들었기 때문에, 실제로는 말이 안되는 경우가 나올 수도 있다. 하지만, 모든 자식의 부모는 유일하며, 다시 자식이 부모의 부모가 되는 경우도 없다. 또, 한 사람이 여러 명의 자식이 될 수 도 없다.
  >
  > ```bash
  > matthew
  > ```



```python
from collections import defaultdict

def sol():

    def dfs(name):
        if name in parents and name not in royalty:
            for p in parents[name]:
                if p not in royalty:
                    if p in parents:
                    # 부모도 아직 기록 안된 누군가의 자손일 경우
                        dfs(p)

                if p in royalty:
                # 부모가 기록되어 있는 자손이라면
                    if name in royalty:
                    # 현재 본인이 이미 기록되어 이미 있다면
                    # 엄마나 아빠 한 명의 피만 물려받았으므로
                        royalty[name] += (royalty[p]/2)
                    else:
                    # 기록되어 있지 않다면
                        royalty[name] = (royalty[p]/2)

    n, m = map(int, input().split())
    king = input()
    parents = defaultdict(list)
    # '자식': [부모들], 자식 배열
    royalty, res, resname = {}, 0, ''
    # 자식들의 수 기록, 결과, 결과이름
    royalty[king] = 1

    for _ in range(n):
        c, p1, p2 = input().split()
        parents[c] = [p1, p2]

    for _ in range(m):
        c = input()
        dfs(c)
        if c in royalty and res < royalty[c]:
            res = royalty[c]
            resname = c

    print(resname)
    print(royalty)


sol()
```

> 아 진짜 오래 걸렸다;; 이게 이렇게 오래 풀 문제는 아닌데 진짜 ㅠ
>
> `if name in parents and name not in royalty:`
>
> 여기 and 뒷 부분을 추가 안해줘서 계속 틀렸었다. 아무래도 이미 누군가의 부모였던 name이면 방문한 name인데 계속 방문해 주면서 2로 나눠 주어서 그랬던 것 같다.
>
> `royalty[name] = (royalty[p]/2)`
>
> 그리고 이렇게 하지 않고 for문이 끝났을 때, 전체적으로 2를 나누어주었는데 그럼 keyerror가 난다. 왜냐면, 부모가 존재하는 자식이고 아직 방문하지 않은 아이인데, 만약 걔의 부모가 왕좌와 상관 없는 아이라면 royalty 딕셔너리에 담겨 있지 않으므로, keyerror가 나올 수 밖에 없다.



* 모범답안

  ```python
  76
  
  def find(l):
      if isinstance(l, float):
          return l
  
      x, y = d.get(l[0], 0.0), d.get(l[1], 0.0)
      return find(x) / 2 + find(y) / 2
  
  
  n, m = map(int, input().split())
  d = {input(): 1.0}
  
  for _ in range(n):
      a, b, c = input().split()
      d[a] = [b, c]
  
  print(max((input() for _ in range(m)), key=lambda x: find(d.get(x, 0.0))))
  ```
  
  > - `isinstance` : l이 float 자료형을 갖고 있는지 확인하는 것이다. 이미 실수형의 자료형을 갖고 있으면 볼 필요도 없이 return하는군.
  > - `x, y = d.get(l[0], 0.0), d.get(l[1], 0.0)` 미친 사람 같네.. 딕셔너리 이렇게 잘 활용하는 거였구나.. 너무 대단해서 할말이 없을 정도...
  > - `(input() for _ in range(m)), key=lambda x: find(d.get(x, 0.0))` 할말이 없다.. 람다식 이렇게 쓰는 거구나 ㅋㅋㅋ 대박이다... 대박이야 진짜.. 경이로워서 할말이 없음.. 반성 많이 해야겠다.

