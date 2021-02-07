# java

## swea d4 1223 계산기2

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD



> 116ms



* 문제

  > 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
  >
  > 예를 들어
  >
  > “3+4+5*6+7”
  >
  > 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
  >
  > "34+56*+7+"
  >
  > 변환된 식을 계산하면 44를 얻을 수 있다.
  >
  > 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

* 입력

  > 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.
  >
  > 총 10개의 테스트 케이스가 주어진다.
  >
  > ```bash
  > 101
  > 9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3
  > 79
  > 4+4*3*4*9+2+7*4*7+7*7*9*5*2+8*8+2*6*7*3*7*9*3*4+8+8*9+3+9+6+9+4*1+6*3+5+1+7+5*1
  > ...
  > ```

* 출력

  > \#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
  >
  > ```bash
  > #1 28134
  > #2 195767
  > ...
  > ```



```java
import java.io.*;
import java.util.Stack;

public class Main_SWEA_1223_계산기2 {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for(int testCase = 1; testCase <= 10; testCase++) {
			sb.append("#").append(testCase).append(" ");
			int result = 0;
			int N = Integer.parseInt(br.readLine());
			String str = br.readLine();
			Stack<Integer> stack = new Stack<>();
			for (int i = 0; i < N; i++) {
				if(str.charAt(i) == '*') {
					stack.push(stack.pop() * Character.getNumericValue(str.charAt(++i)));
				} else if (str.charAt(i) == '+') {
					continue;
				} else {
					stack.push(Character.getNumericValue(str.charAt(i)));
				}
			}
			
			while(!stack.isEmpty()) {
				result += stack.pop();
			}
			sb.append(result).append('\n');
		}
		
		System.out.print(sb);
	}

}


/*
 * str문자열을 받는다
 * 문자열을 다 돌면서 스택에 넣는다
 * for 문자열을 다 도는 동안, 덧셈은 넣지 않는다
 * 
 * if 곱셈이 있으면
 * 스택에 마지막을 빼고
 * 다음에 들어올 숫자와 곱한다음 다시 스택에 넣는다
 * 다 돌고 끝났다.
 * 
 * while 스택이 비어있지 않는 동안
 * 빼면서 하나씩 더한다.
 * 
 */
```

> 바부 그 자체였는데,, 코드는 일찍 짜서 쉴 수 있겠다 해놓고 막상 결과값이 달라서 계속 헤맸던 문제,,,
>
> 문제는 다름이 아니라 str을 char로 바꾸고 char를 다시 int로 바꾸는 과정에서 있었다. 블로그에서 char형을 int형으로 바꾸는 방식이 두 가지 있다고 하며,
>
> Character.getNumericValue(str.charAt(0)와 (int)str.charAt(0) 두 가지를 설명했었다. 하지만 두 가지는 확연하게 답이 다르게 나왔고, 정확한 것은 Character.getNumericValue(str.charAt(0) 이렇게 출력해야 한다는 것이다...





* 모범답안

  ```java
   
  ```
  
  > 