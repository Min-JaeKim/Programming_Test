# python

## 코드업 1120

https://codeup.kr/problem.php?id=1120



### 입력

세 정수가 입력된다.

#### 입력 예시

1 2 3



### 출력

세 수의 평균을 **소수 둘째자리**까지 출력하시오.

####  출력 예시

2.00

```python
import numpy as np

a,b,c = map(float, input().split())
print('%.2f' % np.mean([a,b,c]))
```

> 쉽게 풀 수 있었지만 일부러 numpy 쓰고 싶어서 문제를 풀었는데 문제는 numpy가 아니라 소수 둘째자리까지 출력하는 것이었다.
>
> c랑 다를 바 없지만 python에서 처음 쓰다 보니까 낯설다.
>
> ''%.?f' % 출력결과 <= 기억할것