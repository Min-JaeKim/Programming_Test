# python

## baek 1148 단어 만들기 실버1

https://www.acmicpc.net/problem/1148

> python3 496ms

* 문제

  > 어떤 신문엔 이러한 퍼즐이 있다. 3x3의 표에 영문자가 하나씩 있으며, 이 영문자들을 사용해서 최대한 많은 영단어를 만드는 것이 목표이다. 예를 들면, 아래의 퍼즐판에서는 'LINT', 'TILL', 'BRILLIANT' 등을 만들 수 있다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/1.png)
  >
  > 
  > 단어는 최소 4글자 이상이어야 하며, 한 글자당 최대 1번만 사용할 수 있다. 따라서 10글자 이상의 단어는 만들 수 없다. 또한, 표의 정중앙에 있는 글자는 반드시 사용해야 한다. 위 퍼즐판의 경우 'I'는 반드시 사용해야 한다.
  >
  > 따라서 어떤 글자가 가운데에 있느냐에 따라 퍼즐의 난이도는 천차만별일 것이다. 퍼즐 제작자 남규는 퍼즐판에 어떤 글자를 배치할지는 결정했으나 멍청해서 어떤 글자를 가운데에 놓을지까지는 정하지 못했다.
  >
  > 보다 못한 조수 재혁이가 어떤 글자를 놓아야 퍼즐이 가장 쉬워지는지(즉, 만들 수 있는 단어의 개수가 가장 많음), 또 어떤 글자를 놓아야 퍼즐이 가장 어려워지는지(즉, 만들 수 있는 단어의 개수가 가장 적음)를 알려주려고 한다. 그러나 재혁이가 망각한 사실이 있으니 자신도 멍청하다는 것이었다. 따라서 당신이 이 문제를 대신 풀어주어야 한다.
  >
  > 또한 문제 속 세상의 사람들은 우리보다도 멍청해서, 우리보다 훨씬 적은 수의 영단어를 사용한다. 이 단어들을 모두 담고 있는 사전과 퍼즐판에 배치할 9개의 문자가 주어졌을 때, 문제를 푸는 프로그램을 작성하시오.

* 입력

  > 입력의 처음에는 사전을 이루는 최대 20만 개의 단어가 주어진다. 각 단어는 4~9글자의 영어 대문자로 이루어져 있으며, 한 줄에 하나씩 주어진다. 또한 사전순으로 정렬되어 있다. 사전 입력의 끝에는 한 줄에 걸쳐 '-' 한 글자가 주어진다.
  >
  > 그 다음부터 여러 개의 퍼즐판이 주어진다. 각 퍼즐판은 9개의 영어 대문자로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 맨 끝에는 한 줄에 걸쳐 '#' 한 글자가 주어진다.
  >
  > ```bash
  > APPLE
  > BANANA
  > BANE
  > BRILLIANT
  > LINT
  > PALE
  > PROBLEM
  > TILL
  > TRILL
  > -
  > LARBITNLI
  > LEPAPBNNA
  > LEPAPBNAM
  > #
  > ```
  >
  
* 출력

  > 각 퍼즐판마다 정답을 예제 형식에 맞게 한 줄에 하나씩 출력한다.
  >
  > 각 문제마다 정답의 개수를 가장 적게 하기 위해 정중앙에 놓아야 할 문자들과 그때의 정답 개수, 정답의 개수를 가장 많게 하기 위해 정중앙에 놓아야 할 문자들과 그 때의 정답 개수를 공백으로 구분하여 출력한다.
  >
  > 한 개 이상의 문자가 답을 만족할 경우 문자들을 알파벳순으로 정렬하여 출력하며, 중복된 문자는 출력하지 않는다. 첫 번째 예제 출력에서 보듯이 I나 L은 여러 번 등장하지만 한 번씩만 출력하였다.
  >
  > ```bash
  > AB 1 ILT 4
  > BN 1 AE 3
  > M 0 AE 3
  > ```



```python
import sys
input = sys.stdin.readline


def sol():

    arr = []
    # 일단 문자열들 담는다.

    while 1:
        tmp = input().strip()
        if tmp == '-':
            break
        arr.append(tmp)

    while 1:
        tmp = input().strip()

        if tmp == '#':
            break

        dic, resdic = {}, {}
        # 현재 퍼즐판의 각 알파벳의 개수 기록,
        # 최종적으로 퍼즐판의 각 알파벳이 쓰이는 횟수
        for t in tmp:
            if t in dic:
                dic[t] += 1
            else:
                dic[t] = 1
            resdic[t] = 0

        # 주어진 단어들을 돌면서
        for word in arr:
            # 일단 퍼즐판에 허용되는 단어,
            # 현재 단어의 알파벳 개수
            flag, tmpdic = 1, {}
            for m in word:
                # 퍼즐판에 존재하는 단어가 아니거나,
                # 현재 알파벳이 퍼즐판의 해당 알파벳보다 개수가 더 많다면, 다음 단어
                if m not in dic or (m in tmpdic and tmpdic[m] == dic[m]):
                    flag = 0
                    break

                if m in tmpdic:
                    tmpdic[m] += 1
                else:
                    tmpdic[m] = 1

            if not flag:
                continue

            # 현재 퍼즐판으로 만들 수 있는 단어라면
            if flag:
                # 중복되더라도 하나만 체크할 수 있도록 하는 해쉬맵
                checkdic = {}
                for m in word:
                    if m not in checkdic:
                        resdic[m] += 1
                        checkdic[m] = 1
        
        # 결과 해쉬에서 최대 최소 계산.
        min_v, min_a = min(resdic.values()), []
        max_v, max_a = max(resdic.values()), []

        for r in resdic:
            if resdic[r] == min_v:
                min_a.append(r)
            if resdic[r] == max_v:
                max_a.append(r)

        min_a.sort()
        max_a.sort()

        print(''.join(min_a), end=' ')
        print(min_v, end=' ')
        print(''.join(max_a), end=' ')
        print(max_v)


sol()
```

> 따져야 할 게 많았지만 예제만 풀었다면 통과할 수 있다.



* 모범답안

  ```python
  
  ```

  > 내가 제일 빠르네
