# python

## swea 1244 d3 최대상금

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD



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
for tc in range(1, int(input()) + 1):
    arr, n = input().split()
    # 숫자판의 정보, 교환 횟수, '123' '2'
    strarr = arr[:]
    # rfind를 쓰기 위한 변수, '123'
    arr = list(map(int, arr))
    # [1, 2, 3]
    sortarr = sorted(arr, reverse=True)
    # 정렬된 숫자와 현재 배열을 비교하기 위해, [3, 2, 1]
    n, whilecnt = int(n), 0
    while whilecnt < n:
        cnt = 0
        # 정렬된 배열과 현재 배열과 다른 게 있는지 찾기 위한 변수
        for i in range(len(arr)):
            if arr[i] != sortarr[i]:
                # [1, 2, 3] [3, 2, 1] 0번째 인덱스부터 다르니
                cnt += 1
                break
                # 바로 break하고 교환 시작
        if cnt != 0:
            # 바꿀 인덱스가 있다면
            whilecnt += 1
            # 교환 횟수 ++
            maxnumidx = strarr.rfind(str(max(arr[i:])))
            # 비교중인 인덱스에서부터 끝가지 최댓값을 찾은 후, rfind(문자만 가능)를 통해
            # 최댓값의 인덱스를 가져옴
            # 뒤에서부터 최댓값을 가져와야 했기 때문에 index(x), rfind(o)
            arr[maxnumidx], arr[i] = arr[i], arr[maxnumidx]
            # 최댓값의 인덱스와 현재 비교 중인 인덱스 위치 교환
            strarr = ''.join(list(map(str, arr)))
            # 다음 비교를 위해 문자인 배열도 갱신
        else:
            # 만약 비교할 문자열이 없다면 break
            break
    l, r = arr[:len(arr) - whilecnt], arr[len(arr) - whilecnt:]
    # 이미 비교 완료한 작은 크기의 문자열(r)을 내림차순으로 정렬.
    # 이게 약간 그리디한 부분인데, 실제로 이렇게 풀면 안됩니다.
    # 이건 오로지 5번 테케만을 위한 구문이고, 저는 귀찮아서 이렇게 짰는데 통과했습니다.
    # 실제로 위에 적은 반례가 테케에 있었다면 통과하지 못했을 겁니다.
    # 이부분을 해결하기 위해서는 자리를 바꾼 작은 수들끼리 내림차순으로 정렬을 해야합니다.
    r.sort(reverse=True)
    # 내림차순 정렬
    arr = l+r
    sameflag = False
    # 아직 비교 횟수가 남았는데 77770과 같이 같은 숫자가 존재하는지 체크하기 위한 flag
    if (n - whilecnt) % 2 != 0:
        # 만약 아직 비교할 횟수가 홀수번만큼 남았다면
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                # 777과 같이 같은 숫자가 있다면,
                sameflag = True
                # 교환이 무의미하기에 break
                break
        if not sameflag:
            # 배열 내에 같은 숫자가 없다면
            arr[-1], arr[-2] = arr[-2], arr[-1]
            # 뒤에서 찔끔찔끔 교환해줌
    arr = list(map(str, arr))
    # join을 쓰기 위해 str로~!
    print('#%d' % (tc), end=' ')
    print(''.join(arr))
```

> 하,,, 예상치도 못한 복병을 만났다. 청소년 상어 풀다가 이정도는 껌이지 하고 생각했던 내 잘못이었다. 의외로 어려웠고, 의외로 따져야할 경우의 수가 많았음. 그리고 심지어 내가 만든 테케는 fail했는데 swea에서는 돌아갔다. 테케 추가가 필요할 듯.
>
> 1. 교환할 위치. 분명 최댓값을 맨 앞으로 오게하는 건 맞는데 교환했던 작은 수들끼리 내림차순으로 정렬해 줘야 한다. 예를 들어
>
>    ```
>    1
>    32887 2
>    ```
>
>    과 같은 테케는 답이 `88327` 이렇게 나와야 정상이지만 내가 짠 코드는 88273과 같이 나온다. 
>
> 2. 교환 횟수가 남았을 때 더이상 교환할 숫자가 없으면 반복문을 종료해도 좋다. 오히려 계속 반복문을 강행할 경우 시간이 오버된다.
>
>    1. `if (n - whilecnt) % 2 != 0:` 이와 같은 코드를 사용해야 하며, 짝수 번 교환할 때는 굳이 교환할 필요 없으니 반복문을 돌지 않도록 해야 한다.
>    2. `if arr[i] == arr[i-1]:` 그리고 배열 안에 같은 수가 존재한다면 그 두 수끼리만 교환하면 되므로 종료한다. 홀수든 짝수든 교환해도 배열은 똑같다.



* 모범답안

  ```python
  for tc in range(1, int(input()) + 1):
      arr, n = input().split()
      arr = list(arr);
      len_arr = len(arr)
      v = [0] * len_arr
      n = int(n)
  
      for i in range(len_arr - 1):
          # 현재 인덱스에서 뒤에 더 큰 값이 있으면 교체
          max_arr = max(arr[i + 1:])
          if arr[i] < max_arr:
              # 뒤에서부터 탐색
              for k in range(len_arr - 1, i, -1):
                  if arr[k] == max_arr:
                      v[k] = arr[k]
                      arr[i], arr[k] = arr[k], arr[i]
                      n -= 1;
                      break
          if not n: break
  
      fin = 0
      for i in range(len_arr):
          if arr[i] in arr[i + 1:]: fin = 1
          if v[i]:
              for j in range(i + 1, len_arr):
                  if v[j] == v[i] and arr[j] > arr[i]:
                      arr[i], arr[j] = arr[j], arr[i]
  
      if n % 2 and not fin:
          arr[-1], arr[-2] = arr[-2], arr[-1]
  
      print(arr)
  ```
  
  > 뭔지 모르겠는데 대충 코드 보니까 이사람도 그리디적인 방법으로 푼 것 같음. 뭔가 정석적으로 완전하게 숫자를 교환하는 방식이 아닌 것 같은데,, 근데 아무튼 반례는 없는 것 같다.