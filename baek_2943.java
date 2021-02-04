# java

## 백준 2493 탑

https://www.acmicpc.net/problem/2493



> 664ms



* 문제

  > - KOI 통신연구소는 레이저를 이용한 새로운 비밀 통신 시스템 개발을 위한 실험을 하고 있다. 실험을 위하여 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치하였다. 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다. 
  >
  >   예를 들어 높이가 6, 9, 5, 7, 4인 다섯 개의 탑이 수평 직선에 일렬로 서 있고, 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사한다고 하자. 그러면, 높이가 4인 다섯 번째 탑에서 발사한 레이저 신호는 높이가 7인 네 번째 탑이 수신을 하고, 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다. 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.
  >
  >   탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라. 

* 입력

  > 첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. N은 1 이상 500,000 이하이다. 둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다. 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.
  >
  > ```bash
  > 5
  > 6 9 5 7 4
  > ```

* 출력

  > 첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.
  >
  > ```bash
  > 0 0 2 2 4
  > ```

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;


class Main {  
  public static void main(String args[]) throws Exception { 
      
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int[] top = new int[N];
		int[] result = new int[N];
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < N; i++) {
			top[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < N; i++) {
			while(!stack.isEmpty()) { // stack이 비어있지 않는 동안
				if(top[stack.peek()] <= top[i]) { // stack에 있던 수보다 현재 제시된 수가 더 크다면,
					stack.pop(); // stack을 가차없이 pop
				}
				else { // stack에 있던 수가 더 크다면
					result[i] = stack.peek() + 1; // stack에 있는 수 인덱스를 출력하는데 1씩 증가하여 출력해야 함. 
					break; // 결과를 냈으니 break
				}
			}
			
			stack.push(i); // 항상 반복문이 돌기 직전에 현재 제시된 수 역시 스택에 넣어줘야 함.
		}
		for(int i = 0; i < N; i++) {
			sb.append(result[i]).append(" ");
		}
		System.out.print(sb);
  } 
}
```

> 하............................. 진짜 이 문제 하나로 두 세시간은 날린 것 같다. 결국 답은 메디테이션,, 명상... 명상만이 답이다. 왜인지 모르게 침대에 누워 명상하기 시작하면 답이 금방 나온다..
>
> 두 번째 for문에서 계속 막혔는데 예시 69574 중에서 9를 챙기면 7을 못챙기고 7을 살피면 9를 노히게 되었다. 정말 계속 꼬여서 머리에 쥐가 날 지경이었는데, 누워서 명상 시작하니 바로 답이 나왔다.
>
> 그리고 한 가지 내가 놓쳤던 건, 입력 받는 부분을 계속해서 charAt으로 연습하다 보니 이번에도 그렇게 하게 되었다. 그래서 두 자리수를 입력 받는 데에 오류가 있었기 때문에 계속해서 틀렸습니다가 나왔다. 좀 꼼꼼히 푸는 습관을 들여야겠다.



### 모범답안

```java
package Exam;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception, IOException {
		Stack<int[]> st = new Stack<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer stt = new StringTokenizer(br.readLine());

		for (int i = 1; i <= n; i++) {
			int v = Integer.parseInt(stt.nextToken());
			while (!st.isEmpty()) {
				if (st.peek()[1] >= v) {
					System.out.print(st.peek()[0] + " ");
					break;
				}
				st.pop();
			}
			if (st.isEmpty()) {
				System.out.print("0 ");
			}
			st.push(new int[] { i, v });
		}
	}
}
```





