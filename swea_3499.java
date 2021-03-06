# java

## swea d3 3499 퍼펙트셔플

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW



> 



* 문제

  > 
  
* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
  >
  > 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
  >
  > 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다.
  >
  > ```bash
  > 3
  > 6
  > A B C D E F
  > 4
  > JACK QUEEN KING ACE
  > 5
  > ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA  
  > ```

* 출력

  > 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.
  >
  > ```bash
  > 
  > #1 A D B E C F
  > #2 JACK KING QUEEN ACE
  > #3 ALAKIR LORD-JARAXXUS ALEXSTRASZA AVIANA DR-BOOM
  > ```



```java
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_SWEA_3499_퍼펙트셔플 {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int testCase = Integer.parseInt(br.readLine());
		for (int i = 1; i <= testCase; i++) {
			sb.append("#").append(i);
			int N = Integer.parseInt(br.readLine());
			String[] str = br.readLine().split(" ");
			int index = N%2==0 ? N/2 : N/2+1;
			for (int j = 0; j < N/2; j++) {
				sb.append(" ").append(str[j]);
				sb.append(" ").append(str[index++]);
			}
			if(N%2 != 0) sb.append(" ").append(str[N/2]);
			sb.append('\n');
			
		}
		System.out.print(sb);
		
		
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringBuilder sb = new StringBuilder();
//		int testCase = Integer.parseInt(br.readLine());
//		for (int i = 0; i < testCase; i++) {
//			int N = Integer.parseInt(br.readLine());
//			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//			Queue<String> que1 = new LinkedList<>();
//			Queue<String> que2 = new LinkedList<>();
//			if(N%2 == 0) {
//				for (int j = 1; j <= N/2; j++) {
//					que1.offer(st.nextToken());
//			}
//			for(int j = N/2 + 1; j <= N; j++) {
//				que2.offer(st.nextToken());
//				} 
//			sb.append("#").append(i+1);
//			for (int j = 0; j < N; j++) {
//				if(j%2 == 0) {
//					sb.append(" ").append(que1.poll());
//				} else {
//					sb.append(" ").append(que2.poll());
//				}
//			}
//			sb.append('\n');
//			} else {
//				for (int j = 1; j <= N/2+1; j++) {
//					que1.offer(st.nextToken());
//			}
//			for(int j = N/2 + 2; j <= N; j++) {
//				que2.offer(st.nextToken());
//				} 
//			sb.append("#").append(i+1);
//			for (int j = 0; j < N; j++) {
//				if(j%2 == 0) {
//					sb.append(" ").append(que1.poll());
//				} else {
//					sb.append(" ").append(que2.poll());
//				}
//			}
//			sb.append('\n');
//			}
//			
//		}
//		System.out.print(sb);

	}

}
```

> 처음에는 큐로 풀고 두 번째는 재학님이 알려주신 배열로 풀었다. 큐로 풀었을 때는 2900자 나와서 최고 길이 갱신했는데 배열로 풀었을 때는 그래도 2200자 나왔던 것 같다. 그래도 다른 사람 보면 600자 정도 나오는 것 같은데,, 역시 for문이 문제라고 생각한다.





* 모범답안

  ```java
      for(int t = 1; t <= T; t++) {
          sb.append("#").append(t);
          int N = Integer.parseInt(br.readLine());
          
          String[] cards = br.readLine().split(" ");
          int i = 0;
          int end = N%2;
          int j = N/2 + end;
          do {
              sb.append(" ").append(cards[i++]);
              sb.append(" ").append(cards[j++]);
          }while(j < N);
          if(end == 1)
              sb.append(" ").append(cards[i]);
          
          sb.append("\n");
      }
  ```
  
  > 후,, 무시무시한 재학님의 최고 존엄 코드.. 기가 팍 죽어부럇다.