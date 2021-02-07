# java

## 백준 15649 N과 M(1)

https://www.acmicpc.net/problem/15649



> 164ms



* 문제

  > - 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
  >   - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

* 입력

  > 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
  >
  > ```bash
  > 4 4
  > ```

* 출력

  > 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
  >
  > 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
  >
  > ```bash
  > 1 2 3 4
  > 1 2 4 3
  > 1 3 2 4
  > 1 3 4 2
  > 1 4 2 3
  > 1 4 3 2
  > 2 1 3 4
  > 2 1 4 3
  > 2 3 1 4
  > 2 3 4 1
  > 2 4 1 3
  > 2 4 3 1
  > 3 1 2 4
  > 3 1 4 2
  > 3 2 1 4
  > 3 2 4 1
  > 3 4 1 2
  > 3 4 2 1
  > 4 1 2 3
  > 4 1 3 2
  > 4 2 1 3
  > 4 2 3 1
  > 4 3 1 2
  > 4 3 2 1
  > ```

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main_백준_15469 {

	private static int[] arr;
	public static StringBuilder sb = new StringBuilder();
	private static int N;
	private static int M;
	private static boolean[] visited;

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[M];
		visited = new boolean[N];
		dfs(N,M,0);
		System.out.println(sb);
		
	}

	public static void dfs(int n, int m, int depth) {
		
		if(depth == m) {
			for(int i : arr) {
				sb.append(i).append(" ");
			}
			sb.append('\n');
			return;
		}
		for (int i = 0; i < n; i++) {
//			if(!visited[i]) {
//				visited[i] = true;
//				arr[depth] = i + 1;
//				dfs(n,m,depth + 1);
//				visited[i] = false;
//			}
			if(visited[i]) continue;
			visited[i] = true;
			arr[depth] = i + 1;
			dfs(n,m,depth + 1);
			visited[i] = false;
					
				
		}
	}
	

}

```

> 그냥 이대로 실행했을 시 164ms가 나오고, 주석 친 부분을 실행하고 밑에 부분을 주석했을 시 180ms가 나온다. 



### 모범답안

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
public class Main {
 
	public static int[] arr;
	public static boolean[] visit;
	public static StringBuilder sb = new StringBuilder();
 
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		StringTokenizer st = new StringTokenizer(br.readLine());
 
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
 
		arr = new int[M];
		visit = new boolean[N];
		dfs(N, M, 0);
		System.out.println(sb);
 
	}
 
	public static void dfs(int N, int M, int depth) {
		if (depth == M) {
			for (int val : arr) {
				sb.append(val).append(' ');
			}
			sb.append('\n');
			return;
		}
 
		for (int i = 0; i < N; i++) {
			if (!visit[i]) {
				visit[i] = true;
				arr[depth] = i + 1;
				dfs(N, M, depth + 1);
				visit[i] = false;
			}
		}
	}
 
}
```

> 



