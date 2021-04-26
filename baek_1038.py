# python

## baek 1038 감소하는 수 골드5

https://www.acmicpc.net/problem/1038

> python3 72ms
>
> pypy3 116ms



* 문제

  > 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

* 입력

  > 첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.
  >
  > ```python
  > 18
  > ```
  >
  > 

* 출력

  > 첫째 줄에 N번째 감소하는 수를 출력한다.
  >
  > ```python
  > 42
  > ```



```python
'''
[('0',), ('1',), ('2',), ('3',), ('4',), ('5',), ('6',), ('7',), ('8',), ('9',)]
[('1', '0'), ('2', '0'), ('2', '1'), ('3', '0'), ('3', '1'), ('3', '2'), ('4', '0'), ('4', '1'), ('4', '2'), ('4', '3'), ('5', '0'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4'), ('6', '0'), ('6', '1'), ('6', '2'), ('6', '3'), ('6', '4'), ('6', '5'), ('7', '0'), ('7', '1'), ('7', '2'), ('7', '3'), ('7', '4'), ('7', '5'), ('7', '6'), ('8', '0'), ('8', '1'), ('8', '2'), ('8', '3'), ('8', '4'), ('8', '5'), ('8', '6'), ('8', '7'), ('9', '0'), ('9', '1'), ('9', '2'), ('9', '3'), ('9', '4'), ('9', '5'), ('9', '6'), ('9', '7'), ('9', '8')]
[('2', '1', '0'), ('3', '1', '0'), ('3', '2', '0'), ('3', '2', '1'), ('4', '1', '0'), ('4', '2', '0'), ('4', '2', '1'), ('4', '3', '0'), ('4', '3', '1'), ('4', '3', '2'), ('5', '1', '0'), ('5', '2', '0'), ('5', '2', '1'), ('5', '3', '0'), ('5', '3', '1'), ('5', '3', '2'), ('5', '4', '0'), ('5', '4', '1'), ('5', '4', '2'), ('5', '4', '3'), ('6', '1', '0'), ('6', '2', '0'), ('6', '2', '1'), ('6', '3', '0'), ('6', '3', '1'), ('6', '3', '2'), ('6', '4', '0'), ('6', '4', '1'), ('6', '4', '2'), ('6', '4', '3'), ('6', '5', '0'), ('6', '5', '1'), ('6', '5', '2'), ('6', '5', '3'), ('6', '5', '4'), ('7', '1', '0'), ('7', '2', '0'), ('7', '2', '1'), ('7', '3', '0'), ('7', '3', '1'), ('7', '3', '2'), ('7', '4', '0'), ('7', '4', '1'), ('7', '4', '2'), ('7', '4', '3'), ('7', '5', '0'), ('7', '5', '1'), ('7', '5', '2'), ('7', '5', '3'), ('7', '5', '4'), ('7', '6', '0'), ('7', '6', '1'), ('7', '6', '2'), ('7', '6', '3'), ('7', '6', '4'), ('7', '6', '5'), ('8', '1', '0'), ('8', '2', '0'), ('8', '2', '1'), ('8', '3', '0'), ('8', '3', '1'), ('8', '3', '2'), ('8', '4', '0'), ('8', '4', '1'), ('8', '4', '2'), ('8', '4', '3'), ('8', '5', '0'), ('8', '5', '1'), ('8', '5', '2'), ('8', '5', '3'), ('8', '5', '4'), ('8', '6', '0'), ('8', '6', '1'), ('8', '6', '2'), ('8', '6', '3'), ('8', '6', '4'), ('8', '6', '5'), ('8', '7', '0'), ('8', '7', '1'), ('8', '7', '2'), ('8', '7', '3'), ('8', '7', '4'), ('8', '7', '5'), ('8', '7', '6'), ('9', '1', '0'), ('9', '2', '0'), ('9', '2', '1'), ('9', '3', '0'), ('9', '3', '1'), ('9', '3', '2'), ('9', '4', '0'), ('9', '4', '1'), ('9', '4', '2'), ('9', '4', '3'), ('9', '5', '0'), ('9', '5', '1'), ('9', '5', '2'), ('9', '5', '3'), ('9', '5', '4'), ('9', '6', '0'), ('9', '6', '1'), ('9', '6', '2'), ('9', '6', '3'), ('9', '6', '4'), ('9', '6', '5'), ('9', '7', '0'), ('9', '7', '1'), ('9', '7', '2'), ('9', '7', '3'), ('9', '7', '4'), ('9', '7', '5'), ('9', '7', '6'), ('9', '8', '0'), ('9', '8', '1'), ('9', '8', '2'), ('9', '8', '3'), ('9', '8', '4'), ('9', '8', '5'), ('9', '8', '6'), ('9', '8', '7')]
[('3', '2', '1', '0'), ('4', '2', '1', '0'), ('4', '3', '1', '0'), ('4', '3', '2', '0'), ('4', '3', '2', '1'), ('5', '2', '1', '0'), ('5', '3', '1', '0'), ('5', '3', '2', '0'), ('5', '3', '2', '1'), ('5', '4', '1', '0'), ('5', '4', '2', '0'), ('5', '4', '2', '1'), ('5', '4', '3', '0'), ('5', '4', '3', '1'), ('5', '4', '3', '2'), ('6', '2', '1', '0'), ('6', '3', '1', '0'), ('6', '3', '2', '0'), ('6', '3', '2', '1'), ('6', '4', '1', '0'), ('6', '4', '2', '0'), ('6', '4', '2', '1'), ('6', '4', '3', '0'), ('6', '4', '3', '1'), ('6', '4', '3', '2'), ('6', '5', '1', '0'), ('6', '5', '2', '0'), ('6', '5', '2', '1'), ('6', '5', '3', '0'), ('6', '5', '3', '1'), ('6', '5', '3', '2'), ('6', '5', '4', '0'), ('6', '5', '4', '1'), ('6', '5', '4', '2'), ('6', '5', '4', '3'), ('7', '2', '1', '0'), ('7', '3', '1', '0'), ('7', '3', '2', '0'), ('7', '3', '2', '1'), ('7', '4', '1', '0'), ('7', '4', '2', '0'), ('7', '4', '2', '1'), ('7', '4', '3', '0'), ('7', '4', '3', '1'), ('7', '4', '3', '2'), ('7', '5', '1', '0'), ('7', '5', '2', '0'), ('7', '5', '2', '1'), ('7', '5', '3', '0'), ('7', '5', '3', '1'), ('7', '5', '3', '2'), ('7', '5', '4', '0'), ('7', '5', '4', '1'), ('7', '5', '4', '2'), ('7', '5', '4', '3'), ('7', '6', '1', '0'), ('7', '6', '2', '0'), ('7', '6', '2', '1'), ('7', '6', '3', '0'), ('7', '6', '3', '1'), ('7', '6', '3', '2'), ('7', '6', '4', '0'), ('7', '6', '4', '1'), ('7', '6', '4', '2'), ('7', '6', '4', '3'), ('7', '6', '5', '0'), ('7', '6', '5', '1'), ('7', '6', '5', '2'), ('7', '6', '5', '3'), ('7', '6', '5', '4'), ('8', '2', '1', '0'), ('8', '3', '1', '0'), ('8', '3', '2', '0'), ('8', '3', '2', '1'), ('8', '4', '1', '0'), ('8', '4', '2', '0'), ('8', '4', '2', '1'), ('8', '4', '3', '0'), ('8', '4', '3', '1'), ('8', '4', '3', '2'), ('8', '5', '1', '0'), ('8', '5', '2', '0'), ('8', '5', '2', '1'), ('8', '5', '3', '0'), ('8', '5', '3', '1'), ('8', '5', '3', '2'), ('8', '5', '4', '0'), ('8', '5', '4', '1'), ('8', '5', '4', '2'), ('8', '5', '4', '3'), ('8', '6', '1', '0'), ('8', '6', '2', '0'), ('8', '6', '2', '1'), ('8', '6', '3', '0'), ('8', '6', '3', '1'), ('8', '6', '3', '2'), ('8', '6', '4', '0'), ('8', '6', '4', '1'), ('8', '6', '4', '2'), ('8', '6', '4', '3'), ('8', '6', '5', '0'), ('8', '6', '5', '1'), ('8', '6', '5', '2'), ('8', '6', '5', '3'), ('8', '6', '5', '4'), ('8', '7', '1', '0'), ('8', '7', '2', '0'), ('8', '7', '2', '1'), ('8', '7', '3', '0'), ('8', '7', '3', '1'), ('8', '7', '3', '2'), ('8', '7', '4', '0'), ('8', '7', '4', '1'), ('8', '7', '4', '2'), ('8', '7', '4', '3'), ('8', '7', '5', '0'), ('8', '7', '5', '1'), ('8', '7', '5', '2'), ('8', '7', '5', '3'), ('8', '7', '5', '4'), ('8', '7', '6', '0'), ('8', '7', '6', '1'), ('8', '7', '6', '2'), ('8', '7', '6', '3'), ('8', '7', '6', '4'), ('8', '7', '6', '5'), ('9', '2', '1', '0'), ('9', '3', '1', '0'), ('9', '3', '2', '0'), ('9', '3', '2', '1'), ('9', '4', '1', '0'), ('9', '4', '2', '0'), ('9', '4', '2', '1'), ('9', '4', '3', '0'), ('9', '4', '3', '1'), ('9', '4', '3', '2'), ('9', '5', '1', '0'), ('9', '5', '2', '0'), ('9', '5', '2', '1'), ('9', '5', '3', '0'), ('9', '5', '3', '1'), ('9', '5', '3', '2'), ('9', '5', '4', '0'), ('9', '5', '4', '1'), ('9', '5', '4', '2'), ('9', '5', '4', '3'), ('9', '6', '1', '0'), ('9', '6', '2', '0'), ('9', '6', '2', '1'), ('9', '6', '3', '0'), ('9', '6', '3', '1'), ('9', '6', '3', '2'), ('9', '6', '4', '0'), ('9', '6', '4', '1'), ('9', '6', '4', '2'), ('9', '6', '4', '3'), ('9', '6', '5', '0'), ('9', '6', '5', '1'), ('9', '6', '5', '2'), ('9', '6', '5', '3'), ('9', '6', '5', '4'), ('9', '7', '1', '0'), ('9', '7', '2', '0'), ('9', '7', '2', '1'), ('9', '7', '3', '0'), ('9', '7', '3', '1'), ('9', '7', '3', '2'), ('9', '7', '4', '0'), ('9', '7', '4', '1'), ('9', '7', '4', '2'), ('9', '7', '4', '3'), ('9', '7', '5', '0'), ('9', '7', '5', '1'), ('9', '7', '5', '2'), ('9', '7', '5', '3'), ('9', '7', '5', '4'), ('9', '7', '6', '0'), ('9', '7', '6', '1'), ('9', '7', '6', '2'), ('9', '7', '6', '3'), ('9', '7', '6', '4'), ('9', '7', '6', '5'), ('9', '8', '1', '0'), ('9', '8', '2', '0'), ('9', '8', '2', '1'), ('9', '8', '3', '0'), ('9', '8', '3', '1'), ('9', '8', '3', '2'), ('9', '8', '4', '0'), ('9', '8', '4', '1'), ('9', '8', '4', '2'), ('9', '8', '4', '3'), ('9', '8', '5', '0'), ('9', '8', '5', '1'), ('9', '8', '5', '2'), ('9', '8', '5', '3'), ('9', '8', '5', '4'), ('9', '8', '6', '0'), ('9', '8', '6', '1'), ('9', '8', '6', '2'), ('9', '8', '6', '3'), ('9', '8', '6', '4'), ('9', '8', '6', '5'), ('9', '8', '7', '0'), ('9', '8', '7', '1'), ('9', '8', '7', '2'), ('9', '8', '7', '3'), ('9', '8', '7', '4'), ('9', '8', '7', '5'), ('9', '8', '7', '6')]
[('4', '3', '2', '1', '0'), ('5', '3', '2', '1', '0'), ('5', '4', '2', '1', '0'), ('5', '4', '3', '1', '0'), ('5', '4', '3', '2', '0'), ('5', '4', '3', '2', '1'), ('6', '3', '2', '1', '0'), ('6', '4', '2', '1', '0'), ('6', '4', '3', '1', '0'), ('6', '4', '3', '2', '0'), ('6', '4', '3', '2', '1'), ('6', '5', '2', '1', '0'), ('6', '5', '3', '1', '0'), ('6', '5', '3', '2', '0'), ('6', '5', '3', '2', '1'), ('6', '5', '4', '1', '0'), ('6', '5', '4', '2', '0'), ('6', '5', '4', '2', '1'), ('6', '5', '4', '3', '0'), ('6', '5', '4', '3', '1'), ('6', '5', '4', '3', '2'), ('7', '3', '2', '1', '0'), ('7', '4', '2', '1', '0'), ('7', '4', '3', '1', '0'), ('7', '4', '3', '2', '0'), ('7', '4', '3', '2', '1'), ('7', '5', '2', '1', '0'), ('7', '5', '3', '1', '0'), ('7', '5', '3', '2', '0'), ('7', '5', '3', '2', '1'), ('7', '5', '4', '1', '0'), ('7', '5', '4', '2', '0'), ('7', '5', '4', '2', '1'), ('7', '5', '4', '3', '0'), ('7', '5', '4', '3', '1'), ('7', '5', '4', '3', '2'), ('7', '6', '2', '1', '0'), ('7', '6', '3', '1', '0'), ('7', '6', '3', '2', '0'), ('7', '6', '3', '2', '1'), ('7', '6', '4', '1', '0'), ('7', '6', '4', '2', '0'), ('7', '6', '4', '2', '1'), ('7', '6', '4', '3', '0'), ('7', '6', '4', '3', '1'), ('7', '6', '4', '3', '2'), ('7', '6', '5', '1', '0'), ('7', '6', '5', '2', '0'), ('7', '6', '5', '2', '1'), ('7', '6', '5', '3', '0'), ('7', '6', '5', '3', '1'), ('7', '6', '5', '3', '2'), ('7', '6', '5', '4', '0'), ('7', '6', '5', '4', '1'), ('7', '6', '5', '4', '2'), ('7', '6', '5', '4', '3'), ('8', '3', '2', '1', '0'), ('8', '4', '2', '1', '0'), ('8', '4', '3', '1', '0'), ('8', '4', '3', '2', '0'), ('8', '4', '3', '2', '1'), ('8', '5', '2', '1', '0'), ('8', '5', '3', '1', '0'), ('8', '5', '3', '2', '0'), ('8', '5', '3', '2', '1'), ('8', '5', '4', '1', '0'), ('8', '5', '4', '2', '0'), ('8', '5', '4', '2', '1'), ('8', '5', '4', '3', '0'), ('8', '5', '4', '3', '1'), ('8', '5', '4', '3', '2'), ('8', '6', '2', '1', '0'), ('8', '6', '3', '1', '0'), ('8', '6', '3', '2', '0'), ('8', '6', '3', '2', '1'), ('8', '6', '4', '1', '0'), ('8', '6', '4', '2', '0'), ('8', '6', '4', '2', '1'), ('8', '6', '4', '3', '0'), ('8', '6', '4', '3', '1'), ('8', '6', '4', '3', '2'), ('8', '6', '5', '1', '0'), ('8', '6', '5', '2', '0'), ('8', '6', '5', '2', '1'), ('8', '6', '5', '3', '0'), ('8', '6', '5', '3', '1'), ('8', '6', '5', '3', '2'), ('8', '6', '5', '4', '0'), ('8', '6', '5', '4', '1'), ('8', '6', '5', '4', '2'), ('8', '6', '5', '4', '3'), ('8', '7', '2', '1', '0'), ('8', '7', '3', '1', '0'), ('8', '7', '3', '2', '0'), ('8', '7', '3', '2', '1'), ('8', '7', '4', '1', '0'), ('8', '7', '4', '2', '0'), ('8', '7', '4', '2', '1'), ('8', '7', '4', '3', '0'), ('8', '7', '4', '3', '1'), ('8', '7', '4', '3', '2'), ('8', '7', '5', '1', '0'), ('8', '7', '5', '2', '0'), ('8', '7', '5', '2', '1'), ('8', '7', '5', '3', '0'), ('8', '7', '5', '3', '1'), ('8', '7', '5', '3', '2'), ('8', '7', '5', '4', '0'), ('8', '7', '5', '4', '1'), ('8', '7', '5', '4', '2'), ('8', '7', '5', '4', '3'), ('8', '7', '6', '1', '0'), ('8', '7', '6', '2', '0'), ('8', '7', '6', '2', '1'), ('8', '7', '6', '3', '0'), ('8', '7', '6', '3', '1'), ('8', '7', '6', '3', '2'), ('8', '7', '6', '4', '0'), ('8', '7', '6', '4', '1'), ('8', '7', '6', '4', '2'), ('8', '7', '6', '4', '3'), ('8', '7', '6', '5', '0'), ('8', '7', '6', '5', '1'), ('8', '7', '6', '5', '2'), ('8', '7', '6', '5', '3'), ('8', '7', '6', '5', '4'), ('9', '3', '2', '1', '0'), ('9', '4', '2', '1', '0'), ('9', '4', '3', '1', '0'), ('9', '4', '3', '2', '0'), ('9', '4', '3', '2', '1'), ('9', '5', '2', '1', '0'), ('9', '5', '3', '1', '0'), ('9', '5', '3', '2', '0'), ('9', '5', '3', '2', '1'), ('9', '5', '4', '1', '0'), ('9', '5', '4', '2', '0'), ('9', '5', '4', '2', '1'), ('9', '5', '4', '3', '0'), ('9', '5', '4', '3', '1'), ('9', '5', '4', '3', '2'), ('9', '6', '2', '1', '0'), ('9', '6', '3', '1', '0'), ('9', '6', '3', '2', '0'), ('9', '6', '3', '2', '1'), ('9', '6', '4', '1', '0'), ('9', '6', '4', '2', '0'), ('9', '6', '4', '2', '1'), ('9', '6', '4', '3', '0'), ('9', '6', '4', '3', '1'), ('9', '6', '4', '3', '2'), ('9', '6', '5', '1', '0'), ('9', '6', '5', '2', '0'), ('9', '6', '5', '2', '1'), ('9', '6', '5', '3', '0'), ('9', '6', '5', '3', '1'), ('9', '6', '5', '3', '2'), ('9', '6', '5', '4', '0'), ('9', '6', '5', '4', '1'), ('9', '6', '5', '4', '2'), ('9', '6', '5', '4', '3'), ('9', '7', '2', '1', '0'), ('9', '7', '3', '1', '0'), ('9', '7', '3', '2', '0'), ('9', '7', '3', '2', '1'), ('9', '7', '4', '1', '0'), ('9', '7', '4', '2', '0'), ('9', '7', '4', '2', '1'), ('9', '7', '4', '3', '0'), ('9', '7', '4', '3', '1'), ('9', '7', '4', '3', '2'), ('9', '7', '5', '1', '0'), ('9', '7', '5', '2', '0'), ('9', '7', '5', '2', '1'), ('9', '7', '5', '3', '0'), ('9', '7', '5', '3', '1'), ('9', '7', '5', '3', '2'), ('9', '7', '5', '4', '0'), ('9', '7', '5', '4', '1'), ('9', '7', '5', '4', '2'), ('9', '7', '5', '4', '3'), ('9', '7', '6', '1', '0'), ('9', '7', '6', '2', '0'), ('9', '7', '6', '2', '1'), ('9', '7', '6', '3', '0'), ('9', '7', '6', '3', '1'), ('9', '7', '6', '3', '2'), ('9', '7', '6', '4', '0'), ('9', '7', '6', '4', '1'), ('9', '7', '6', '4', '2'), ('9', '7', '6', '4', '3'), ('9', '7', '6', '5', '0'), ('9', '7', '6', '5', '1'), ('9', '7', '6', '5', '2'), ('9', '7', '6', '5', '3'), ('9', '7', '6', '5', '4'), ('9', '8', '2', '1', '0'), ('9', '8', '3', '1', '0'), ('9', '8', '3', '2', '0'), ('9', '8', '3', '2', '1'), ('9', '8', '4', '1', '0'), ('9', '8', '4', '2', '0'), ('9', '8', '4', '2', '1'), ('9', '8', '4', '3', '0'), ('9', '8', '4', '3', '1'), ('9', '8', '4', '3', '2'), ('9', '8', '5', '1', '0'), ('9', '8', '5', '2', '0'), ('9', '8', '5', '2', '1'), ('9', '8', '5', '3', '0'), ('9', '8', '5', '3', '1'), ('9', '8', '5', '3', '2'), ('9', '8', '5', '4', '0'), ('9', '8', '5', '4', '1'), ('9', '8', '5', '4', '2'), ('9', '8', '5', '4', '3'), ('9', '8', '6', '1', '0'), ('9', '8', '6', '2', '0'), ('9', '8', '6', '2', '1'), ('9', '8', '6', '3', '0'), ('9', '8', '6', '3', '1'), ('9', '8', '6', '3', '2'), ('9', '8', '6', '4', '0'), ('9', '8', '6', '4', '1'), ('9', '8', '6', '4', '2'), ('9', '8', '6', '4', '3'), ('9', '8', '6', '5', '0'), ('9', '8', '6', '5', '1'), ('9', '8', '6', '5', '2'), ('9', '8', '6', '5', '3'), ('9', '8', '6', '5', '4'), ('9', '8', '7', '1', '0'), ('9', '8', '7', '2', '0'), ('9', '8', '7', '2', '1'), ('9', '8', '7', '3', '0'), ('9', '8', '7', '3', '1'), ('9', '8', '7', '3', '2'), ('9', '8', '7', '4', '0'), ('9', '8', '7', '4', '1'), ('9', '8', '7', '4', '2'), ('9', '8', '7', '4', '3'), ('9', '8', '7', '5', '0'), ('9', '8', '7', '5', '1'), ('9', '8', '7', '5', '2'), ('9', '8', '7', '5', '3'), ('9', '8', '7', '5', '4'), ('9', '8', '7', '6', '0'), ('9', '8', '7', '6', '1'), ('9', '8', '7', '6', '2'), ('9', '8', '7', '6', '3'), ('9', '8', '7', '6', '4'), ('9', '8', '7', '6', '5')]
[('5', '4', '3', '2', '1', '0'), ('6', '4', '3', '2', '1', '0'), ('6', '5', '3', '2', '1', '0'), ('6', '5', '4', '2', '1', '0'), ('6', '5', '4', '3', '1', '0'), ('6', '5', '4', '3', '2', '0'), ('6', '5', '4', '3', '2', '1'), ('7', '4', '3', '2', '1', '0'), ('7', '5', '3', '2', '1', '0'), ('7', '5', '4', '2', '1', '0'), ('7', '5', '4', '3', '1', '0'), ('7', '5', '4', '3', '2', '0'), ('7', '5', '4', '3', '2', '1'), ('7', '6', '3', '2', '1', '0'), ('7', '6', '4', '2', '1', '0'), ('7', '6', '4', '3', '1', '0'), ('7', '6', '4', '3', '2', '0'), ('7', '6', '4', '3', '2', '1'), ('7', '6', '5', '2', '1', '0'), ('7', '6', '5', '3', '1', '0'), ('7', '6', '5', '3', '2', '0'), ('7', '6', '5', '3', '2', '1'), ('7', '6', '5', '4', '1', '0'), ('7', '6', '5', '4', '2', '0'), ('7', '6', '5', '4', '2', '1'), ('7', '6', '5', '4', '3', '0'), ('7', '6', '5', '4', '3', '1'), ('7', '6', '5', '4', '3', '2'), ('8', '4', '3', '2', '1', '0'), ('8', '5', '3', '2', '1', '0'), ('8', '5', '4', '2', '1', '0'), ('8', '5', '4', '3', '1', '0'), ('8', '5', '4', '3', '2', '0'), ('8', '5', '4', '3', '2', '1'), ('8', '6', '3', '2', '1', '0'), ('8', '6', '4', '2', '1', '0'), ('8', '6', '4', '3', '1', '0'), ('8', '6', '4', '3', '2', '0'), ('8', '6', '4', '3', '2', '1'), ('8', '6', '5', '2', '1', '0'), ('8', '6', '5', '3', '1', '0'), ('8', '6', '5', '3', '2', '0'), ('8', '6', '5', '3', '2', '1'), ('8', '6', '5', '4', '1', '0'), ('8', '6', '5', '4', '2', '0'), ('8', '6', '5', '4', '2', '1'), ('8', '6', '5', '4', '3', '0'), ('8', '6', '5', '4', '3', '1'), ('8', '6', '5', '4', '3', '2'), ('8', '7', '3', '2', '1', '0'), ('8', '7', '4', '2', '1', '0'), ('8', '7', '4', '3', '1', '0'), ('8', '7', '4', '3', '2', '0'), ('8', '7', '4', '3', '2', '1'), ('8', '7', '5', '2', '1', '0'), ('8', '7', '5', '3', '1', '0'), ('8', '7', '5', '3', '2', '0'), ('8', '7', '5', '3', '2', '1'), ('8', '7', '5', '4', '1', '0'), ('8', '7', '5', '4', '2', '0'), ('8', '7', '5', '4', '2', '1'), ('8', '7', '5', '4', '3', '0'), ('8', '7', '5', '4', '3', '1'), ('8', '7', '5', '4', '3', '2'), ('8', '7', '6', '2', '1', '0'), ('8', '7', '6', '3', '1', '0'), ('8', '7', '6', '3', '2', '0'), ('8', '7', '6', '3', '2', '1'), ('8', '7', '6', '4', '1', '0'), ('8', '7', '6', '4', '2', '0'), ('8', '7', '6', '4', '2', '1'), ('8', '7', '6', '4', '3', '0'), ('8', '7', '6', '4', '3', '1'), ('8', '7', '6', '4', '3', '2'), ('8', '7', '6', '5', '1', '0'), ('8', '7', '6', '5', '2', '0'), ('8', '7', '6', '5', '2', '1'), ('8', '7', '6', '5', '3', '0'), ('8', '7', '6', '5', '3', '1'), ('8', '7', '6', '5', '3', '2'), ('8', '7', '6', '5', '4', '0'), ('8', '7', '6', '5', '4', '1'), ('8', '7', '6', '5', '4', '2'), ('8', '7', '6', '5', '4', '3'), ('9', '4', '3', '2', '1', '0'), ('9', '5', '3', '2', '1', '0'), ('9', '5', '4', '2', '1', '0'), ('9', '5', '4', '3', '1', '0'), ('9', '5', '4', '3', '2', '0'), ('9', '5', '4', '3', '2', '1'), ('9', '6', '3', '2', '1', '0'), ('9', '6', '4', '2', '1', '0'), ('9', '6', '4', '3', '1', '0'), ('9', '6', '4', '3', '2', '0'), ('9', '6', '4', '3', '2', '1'), ('9', '6', '5', '2', '1', '0'), ('9', '6', '5', '3', '1', '0'), ('9', '6', '5', '3', '2', '0'), ('9', '6', '5', '3', '2', '1'), ('9', '6', '5', '4', '1', '0'), ('9', '6', '5', '4', '2', '0'), ('9', '6', '5', '4', '2', '1'), ('9', '6', '5', '4', '3', '0'), ('9', '6', '5', '4', '3', '1'), ('9', '6', '5', '4', '3', '2'), ('9', '7', '3', '2', '1', '0'), ('9', '7', '4', '2', '1', '0'), ('9', '7', '4', '3', '1', '0'), ('9', '7', '4', '3', '2', '0'), ('9', '7', '4', '3', '2', '1'), ('9', '7', '5', '2', '1', '0'), ('9', '7', '5', '3', '1', '0'), ('9', '7', '5', '3', '2', '0'), ('9', '7', '5', '3', '2', '1'), ('9', '7', '5', '4', '1', '0'), ('9', '7', '5', '4', '2', '0'), ('9', '7', '5', '4', '2', '1'), ('9', '7', '5', '4', '3', '0'), ('9', '7', '5', '4', '3', '1'), ('9', '7', '5', '4', '3', '2'), ('9', '7', '6', '2', '1', '0'), ('9', '7', '6', '3', '1', '0'), ('9', '7', '6', '3', '2', '0'), ('9', '7', '6', '3', '2', '1'), ('9', '7', '6', '4', '1', '0'), ('9', '7', '6', '4', '2', '0'), ('9', '7', '6', '4', '2', '1'), ('9', '7', '6', '4', '3', '0'), ('9', '7', '6', '4', '3', '1'), ('9', '7', '6', '4', '3', '2'), ('9', '7', '6', '5', '1', '0'), ('9', '7', '6', '5', '2', '0'), ('9', '7', '6', '5', '2', '1'), ('9', '7', '6', '5', '3', '0'), ('9', '7', '6', '5', '3', '1'), ('9', '7', '6', '5', '3', '2'), ('9', '7', '6', '5', '4', '0'), ('9', '7', '6', '5', '4', '1'), ('9', '7', '6', '5', '4', '2'), ('9', '7', '6', '5', '4', '3'), ('9', '8', '3', '2', '1', '0'), ('9', '8', '4', '2', '1', '0'), ('9', '8', '4', '3', '1', '0'), ('9', '8', '4', '3', '2', '0'), ('9', '8', '4', '3', '2', '1'), ('9', '8', '5', '2', '1', '0'), ('9', '8', '5', '3', '1', '0'), ('9', '8', '5', '3', '2', '0'), ('9', '8', '5', '3', '2', '1'), ('9', '8', '5', '4', '1', '0'), ('9', '8', '5', '4', '2', '0'), ('9', '8', '5', '4', '2', '1'), ('9', '8', '5', '4', '3', '0'), ('9', '8', '5', '4', '3', '1'), ('9', '8', '5', '4', '3', '2'), ('9', '8', '6', '2', '1', '0'), ('9', '8', '6', '3', '1', '0'), ('9', '8', '6', '3', '2', '0'), ('9', '8', '6', '3', '2', '1'), ('9', '8', '6', '4', '1', '0'), ('9', '8', '6', '4', '2', '0'), ('9', '8', '6', '4', '2', '1'), ('9', '8', '6', '4', '3', '0'), ('9', '8', '6', '4', '3', '1'), ('9', '8', '6', '4', '3', '2'), ('9', '8', '6', '5', '1', '0'), ('9', '8', '6', '5', '2', '0'), ('9', '8', '6', '5', '2', '1'), ('9', '8', '6', '5', '3', '0'), ('9', '8', '6', '5', '3', '1'), ('9', '8', '6', '5', '3', '2'), ('9', '8', '6', '5', '4', '0'), ('9', '8', '6', '5', '4', '1'), ('9', '8', '6', '5', '4', '2'), ('9', '8', '6', '5', '4', '3'), ('9', '8', '7', '2', '1', '0'), ('9', '8', '7', '3', '1', '0'), ('9', '8', '7', '3', '2', '0'), ('9', '8', '7', '3', '2', '1'), ('9', '8', '7', '4', '1', '0'), ('9', '8', '7', '4', '2', '0'), ('9', '8', '7', '4', '2', '1'), ('9', '8', '7', '4', '3', '0'), ('9', '8', '7', '4', '3', '1'), ('9', '8', '7', '4', '3', '2'), ('9', '8', '7', '5', '1', '0'), ('9', '8', '7', '5', '2', '0'), ('9', '8', '7', '5', '2', '1'), ('9', '8', '7', '5', '3', '0'), ('9', '8', '7', '5', '3', '1'), ('9', '8', '7', '5', '3', '2'), ('9', '8', '7', '5', '4', '0'), ('9', '8', '7', '5', '4', '1'), ('9', '8', '7', '5', '4', '2'), ('9', '8', '7', '5', '4', '3'), ('9', '8', '7', '6', '1', '0'), ('9', '8', '7', '6', '2', '0'), ('9', '8', '7', '6', '2', '1'), ('9', '8', '7', '6', '3', '0'), ('9', '8', '7', '6', '3', '1'), ('9', '8', '7', '6', '3', '2'), ('9', '8', '7', '6', '4', '0'), ('9', '8', '7', '6', '4', '1'), ('9', '8', '7', '6', '4', '2'), ('9', '8', '7', '6', '4', '3'), ('9', '8', '7', '6', '5', '0'), ('9', '8', '7', '6', '5', '1'), ('9', '8', '7', '6', '5', '2'), ('9', '8', '7', '6', '5', '3'), ('9', '8', '7', '6', '5', '4')]
[('6', '5', '4', '3', '2', '1', '0'), ('7', '5', '4', '3', '2', '1', '0'), ('7', '6', '4', '3', '2', '1', '0'), ('7', '6', '5', '3', '2', '1', '0'), ('7', '6', '5', '4', '2', '1', '0'), ('7', '6', '5', '4', '3', '1', '0'), ('7', '6', '5', '4', '3', '2', '0'), ('7', '6', '5', '4', '3', '2', '1'), ('8', '5', '4', '3', '2', '1', '0'), ('8', '6', '4', '3', '2', '1', '0'), ('8', '6', '5', '3', '2', '1', '0'), ('8', '6', '5', '4', '2', '1', '0'), ('8', '6', '5', '4', '3', '1', '0'), ('8', '6', '5', '4', '3', '2', '0'), ('8', '6', '5', '4', '3', '2', '1'), ('8', '7', '4', '3', '2', '1', '0'), ('8', '7', '5', '3', '2', '1', '0'), ('8', '7', '5', '4', '2', '1', '0'), ('8', '7', '5', '4', '3', '1', '0'), ('8', '7', '5', '4', '3', '2', '0'), ('8', '7', '5', '4', '3', '2', '1'), ('8', '7', '6', '3', '2', '1', '0'), ('8', '7', '6', '4', '2', '1', '0'), ('8', '7', '6', '4', '3', '1', '0'), ('8', '7', '6', '4', '3', '2', '0'), ('8', '7', '6', '4', '3', '2', '1'), ('8', '7', '6', '5', '2', '1', '0'), ('8', '7', '6', '5', '3', '1', '0'), ('8', '7', '6', '5', '3', '2', '0'), ('8', '7', '6', '5', '3', '2', '1'), ('8', '7', '6', '5', '4', '1', '0'), ('8', '7', '6', '5', '4', '2', '0'), ('8', '7', '6', '5', '4', '2', '1'), ('8', '7', '6', '5', '4', '3', '0'), ('8', '7', '6', '5', '4', '3', '1'), ('8', '7', '6', '5', '4', '3', '2'), ('9', '5', '4', '3', '2', '1', '0'), ('9', '6', '4', '3', '2', '1', '0'), ('9', '6', '5', '3', '2', '1', '0'), ('9', '6', '5', '4', '2', '1', '0'), ('9', '6', '5', '4', '3', '1', '0'), ('9', '6', '5', '4', '3', '2', '0'), ('9', '6', '5', '4', '3', '2', '1'), ('9', '7', '4', '3', '2', '1', '0'), ('9', '7', '5', '3', '2', '1', '0'), ('9', '7', '5', '4', '2', '1', '0'), ('9', '7', '5', '4', '3', '1', '0'), ('9', '7', '5', '4', '3', '2', '0'), ('9', '7', '5', '4', '3', '2', '1'), ('9', '7', '6', '3', '2', '1', '0'), ('9', '7', '6', '4', '2', '1', '0'), ('9', '7', '6', '4', '3', '1', '0'), ('9', '7', '6', '4', '3', '2', '0'), ('9', '7', '6', '4', '3', '2', '1'), ('9', '7', '6', '5', '2', '1', '0'), ('9', '7', '6', '5', '3', '1', '0'), ('9', '7', '6', '5', '3', '2', '0'), ('9', '7', '6', '5', '3', '2', '1'), ('9', '7', '6', '5', '4', '1', '0'), ('9', '7', '6', '5', '4', '2', '0'), ('9', '7', '6', '5', '4', '2', '1'), ('9', '7', '6', '5', '4', '3', '0'), ('9', '7', '6', '5', '4', '3', '1'), ('9', '7', '6', '5', '4', '3', '2'), ('9', '8', '4', '3', '2', '1', '0'), ('9', '8', '5', '3', '2', '1', '0'), ('9', '8', '5', '4', '2', '1', '0'), ('9', '8', '5', '4', '3', '1', '0'), ('9', '8', '5', '4', '3', '2', '0'), ('9', '8', '5', '4', '3', '2', '1'), ('9', '8', '6', '3', '2', '1', '0'), ('9', '8', '6', '4', '2', '1', '0'), ('9', '8', '6', '4', '3', '1', '0'), ('9', '8', '6', '4', '3', '2', '0'), ('9', '8', '6', '4', '3', '2', '1'), ('9', '8', '6', '5', '2', '1', '0'), ('9', '8', '6', '5', '3', '1', '0'), ('9', '8', '6', '5', '3', '2', '0'), ('9', '8', '6', '5', '3', '2', '1'), ('9', '8', '6', '5', '4', '1', '0'), ('9', '8', '6', '5', '4', '2', '0'), ('9', '8', '6', '5', '4', '2', '1'), ('9', '8', '6', '5', '4', '3', '0'), ('9', '8', '6', '5', '4', '3', '1'), ('9', '8', '6', '5', '4', '3', '2'), ('9', '8', '7', '3', '2', '1', '0'), ('9', '8', '7', '4', '2', '1', '0'), ('9', '8', '7', '4', '3', '1', '0'), ('9', '8', '7', '4', '3', '2', '0'), ('9', '8', '7', '4', '3', '2', '1'), ('9', '8', '7', '5', '2', '1', '0'), ('9', '8', '7', '5', '3', '1', '0'), ('9', '8', '7', '5', '3', '2', '0'), ('9', '8', '7', '5', '3', '2', '1'), ('9', '8', '7', '5', '4', '1', '0'), ('9', '8', '7', '5', '4', '2', '0'), ('9', '8', '7', '5', '4', '2', '1'), ('9', '8', '7', '5', '4', '3', '0'), ('9', '8', '7', '5', '4', '3', '1'), ('9', '8', '7', '5', '4', '3', '2'), ('9', '8', '7', '6', '2', '1', '0'), ('9', '8', '7', '6', '3', '1', '0'), ('9', '8', '7', '6', '3', '2', '0'), ('9', '8', '7', '6', '3', '2', '1'), ('9', '8', '7', '6', '4', '1', '0'), ('9', '8', '7', '6', '4', '2', '0'), ('9', '8', '7', '6', '4', '2', '1'), ('9', '8', '7', '6', '4', '3', '0'), ('9', '8', '7', '6', '4', '3', '1'), ('9', '8', '7', '6', '4', '3', '2'), ('9', '8', '7', '6', '5', '1', '0'), ('9', '8', '7', '6', '5', '2', '0'), ('9', '8', '7', '6', '5', '2', '1'), ('9', '8', '7', '6', '5', '3', '0'), ('9', '8', '7', '6', '5', '3', '1'), ('9', '8', '7', '6', '5', '3', '2'), ('9', '8', '7', '6', '5', '4', '0'), ('9', '8', '7', '6', '5', '4', '1'), ('9', '8', '7', '6', '5', '4', '2'), ('9', '8', '7', '6', '5', '4', '3')]
[('7', '6', '5', '4', '3', '2', '1', '0'), ('8', '6', '5', '4', '3', '2', '1', '0'), ('8', '7', '5', '4', '3', '2', '1', '0'), ('8', '7', '6', '4', '3', '2', '1', '0'), ('8', '7', '6', '5', '3', '2', '1', '0'), ('8', '7', '6', '5', '4', '2', '1', '0'), ('8', '7', '6', '5', '4', '3', '1', '0'), ('8', '7', '6', '5', '4', '3', '2', '0'), ('8', '7', '6', '5', '4', '3', '2', '1'), ('9', '6', '5', '4', '3', '2', '1', '0'), ('9', '7', '5', '4', '3', '2', '1', '0'), ('9', '7', '6', '4', '3', '2', '1', '0'), ('9', '7', '6', '5', '3', '2', '1', '0'), ('9', '7', '6', '5', '4', '2', '1', '0'), ('9', '7', '6', '5', '4', '3', '1', '0'), ('9', '7', '6', '5', '4', '3', '2', '0'), ('9', '7', '6', '5', '4', '3', '2', '1'), ('9', '8', '5', '4', '3', '2', '1', '0'), ('9', '8', '6', '4', '3', '2', '1', '0'), ('9', '8', '6', '5', '3', '2', '1', '0'), ('9', '8', '6', '5', '4', '2', '1', '0'), ('9', '8', '6', '5', '4', '3', '1', '0'), ('9', '8', '6', '5', '4', '3', '2', '0'), ('9', '8', '6', '5', '4', '3', '2', '1'), ('9', '8', '7', '4', '3', '2', '1', '0'), ('9', '8', '7', '5', '3', '2', '1', '0'), ('9', '8', '7', '5', '4', '2', '1', '0'), ('9', '8', '7', '5', '4', '3', '1', '0'), ('9', '8', '7', '5', '4', '3', '2', '0'), ('9', '8', '7', '5', '4', '3', '2', '1'), ('9', '8', '7', '6', '3', '2', '1', '0'), ('9', '8', '7', '6', '4', '2', '1', '0'), ('9', '8', '7', '6', '4', '3', '1', '0'), ('9', '8', '7', '6', '4', '3', '2', '0'), ('9', '8', '7', '6', '4', '3', '2', '1'), ('9', '8', '7', '6', '5', '2', '1', '0'), ('9', '8', '7', '6', '5', '3', '1', '0'), ('9', '8', '7', '6', '5', '3', '2', '0'), ('9', '8', '7', '6', '5', '3', '2', '1'), ('9', '8', '7', '6', '5', '4', '1', '0'), ('9', '8', '7', '6', '5', '4', '2', '0'), ('9', '8', '7', '6', '5', '4', '2', '1'), ('9', '8', '7', '6', '5', '4', '3', '0'), ('9', '8', '7', '6', '5', '4', '3', '1'), ('9', '8', '7', '6', '5', '4', '3', '2')]
[('8', '7', '6', '5', '4', '3', '2', '1', '0'), ('9', '7', '6', '5', '4', '3', '2', '1', '0'), ('9', '8', '6', '5', '4', '3', '2', '1', '0'), ('9', '8', '7', '5', '4', '3', '2', '1', '0'), ('9', '8', '7', '6', '4', '3', '2', '1', '0'), ('9', '8', '7', '6', '5', '3', '2', '1', '0'), ('9', '8', '7', '6', '5', '4', '2', '1', '0'), ('9', '8', '7', '6', '5', '4', '3', '1', '0'), ('9', '8', '7', '6', '5', '4', '3', '2', '0'), ('9', '8', '7', '6', '5', '4', '3', '2', '1')]
[('9', '8', '7', '6', '5', '4', '3', '2', '1', '0')]
'''

from itertools import combinations
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    for i in range(1, 11):
        num = list(combinations('9876543210', i))[::-1]
        # 우ㅣ와 같이 조합의 수가 나열된다.
        if n <= len(num)-1:
            print(''.join(num[n]))  # 값에 해당하면 출력
            exit()
        else:
            n -= len(num)
    print(-1)   # 조합 수에서도 찾지 못했다면 -1 출력


sol()
```

> 참나루,,, 도저히 어떻게 풀어야할지 감이 안와서 찾아봄.
>
> 이걸 어떻게 이렇게 씽크빅 가능한 풀이로 푸는지 너무 신기하다.
>
> 98 97 96 95 94 --- 이런식으로 출력되는걸
>
> [::-1]로 뒤집으면서 감소하는 수를 찾음,, 천재다 만재다



* 모범답안

  ```python
  
  ```

  > 

