# Java

## baek 1260 DFS와 BFS

https://www.acmicpc.net/problem/1260



> 288ms



* 문제

  > 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

* 입력

  > 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
  >
  > ```bash
  > 4 5 1
  > 1 2
  > 1 3
  > 1 4
  > 2 4
  > 3 4
  > ```

* 출력

  > 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
  >
  > ```bash
  > 1 2 4 3
  > 1 2 3 4
  > ```



```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_1260 {

	private static boolean[] visit;
	private static int n;
	private static int[][] arr;

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		visit = new boolean[n+1];
		arr = new int [n+1][n+1];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int list1 = Integer.parseInt(st.nextToken());
			int list2 = Integer.parseInt(st.nextToken());
			arr[list1][list2] = 1;
			arr[list2][list1] = 1;
		}
		dfs(v);
		System.out.println();
		bfs(v);
	}

	public static void bfs(int v) { // BFS 시작
		Queue<Integer> que = new LinkedList<Integer>();
		que.offer(v); // 첫 시작을 QUE에 넣어줌
		visit[v] = false; //그리고 방문표시는 0로 표시, DFS와 차별점을 둠
		while(!que.isEmpty()) { // QUE에 인자가 있다면
			int temp = que.poll(); // 임시 변수에 QUE를 넣어주고
			System.out.print(temp + " "); // 방금 POP한 것을 출력
			for (int i = 0; i < n+1; i++) { // 인접해있는지 확인
				if(visit[i] && arr[temp][i] == 1) { // 방문도 하지 않았고, 인접해 있다면
					que.offer(i); // QUE에 넣어주고
					visit[i] = false; // 방문표시
				}
			}
		}
		
	}

	public static void dfs(int v) { //DFS 시작
		visit[v] = true; //시작지점 방문 표시 1
		System.out.print(v + " "); //FOR문으로 인접해 있나 확인
		for (int i = 0; i < n+1; i++) { // FOR문으로 인접해 있나 확인
			if(!visit[i] && arr[v][i] == 1) { //방문하지도 않고 인접해있다면
				dfs(i); //재귀로 DFS 돌려줌
			}
		}
		
	}
}
```

> 



* 모범답안

  ```python
  
  ```

  > 