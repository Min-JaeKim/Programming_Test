# java

## 백준 1966 프린터 큐

https://www.acmicpc.net/problem/1966



> 108ms



* 문제

  > - 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
  >
  >   1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
  >   2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
  >
  >   예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
  >
  >   여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

* 입력

  > 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
  >
  > 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
  >
  > ```bash
  > 3
  > 1 0
  > 5
  > 4 2
  > 1 2 3 4
  > 6 0
  > 1 1 9 1 1 1
  > ```

* 출력

  > 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
  >
  > ```bash
  > 1
  > 2
  > 5
  > ```

```java
import java.io.*;
import java.util.Collections;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int tc = Integer.parseInt(br.readLine());
		for (int i = 0; i < tc; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int print = Integer.parseInt(st.nextToken()); 
			int index = Integer.parseInt(st.nextToken()); 
			int count = 1;
			Queue<Integer> que = new LinkedList<>(); // 프린터를 넣을 큐
			Queue<Integer> que_in = new LinkedList<>(); // 프린터의 인덱스를 넣을 큐
			PriorityQueue<Integer> pq = new PriorityQueue<> (Collections.reverseOrder()); // 프린터에 넣은 큐를 우선순위 큐로 정렬하는데 내림차순으로 정렬함.
			StringTokenizer st2 = new StringTokenizer(br.readLine()," ");
			for (int j = 0; j < print; j++) {
				int tmp_p = Integer.parseInt(st2.nextToken());
				que.offer(tmp_p);
				pq.offer(tmp_p);
				que_in.offer(j); // 인덱스 삽입
			}
			while(true) {
				if(que.peek() == pq.peek()) { // 우선순위 큐와 큐가 일치할 때
					if(index == que_in.peek()) {
						break; // 정답일 때
					} else { // 정답이 아닐때
						pq.poll(); // 우선순위 큐, 프린터 큐, 인덱스 큐를 모두 빼서 정답을 찾을 수 있게 해준다.
						que.poll();
						que_in.poll();
						count++; // 우선순위가 높은 프린터기로 출력을 했으니 횟수 상승.
					}
				} else {  // 일치하지 않을 때
					que.offer(que.poll()); // 프린터 큐와 인덱스 큐의 앞부분을 빼고 다시 뒤에 넣어준다.
					que_in.offer(que_in.poll());
				}
			}
			sb.append(count).append('\n');
		}
		System.out.println(sb);
	
	}
}
```

> 정말 침착하게 풀어야 하는 것만이 내 실력을 높일 수 있는 유일한 방법이라고 생각한다. 초반에 문제를 읽고 장황하게 머릿속에서 구현하려고 하니 잘 나오지 않았다. 그래서 선택한 방법이 내가 직접 푸는 코드에 주석으로 차근 차근 써내려 가는 것이다. 요즘은 종이를 사용할 수 없는 코테 시험도 종종 있기 때문에 최대한 종이를 사용하지 않고 키보드로 모든 것을 해결하려고 노력하고 있기 때문이다.
>
> * __PriorityQueue<Integer> pq = new PriorityQueue<> (Collections.reverseOrder());__ : 우선순위 큐 내림차순 정렬.



### 모범답안

```java
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int n, m, count; // m의 인덱스는 0부터
		for (int i = 0; i < t; i++) {
			LinkedList<int[]> queue = new LinkedList<>();
			count = 0;
			n = sc.nextInt();
			m = sc.nextInt();
			for (int j = 0; j < n; j++)
				queue.add(new int[] { j, sc.nextInt() });
// 인덱스, 중요도 입력받기
			while (!queue.isEmpty()) { // 큐가 빌 때까지
				int[] now = queue.poll();
				boolean able = true;
				for (int[] q : queue)
					if (q[1] > now[1])
						able = false;
				if (able) {
					count++;
					if (now[0] == m)
						break;
				} else
					queue.add(now);
			}
			System.out.println(count);
		}
	}
}
```

> 



