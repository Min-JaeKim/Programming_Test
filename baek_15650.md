# java

## 백준 15650 N과 M(2)

https://www.acmicpc.net/problem/15650



> 88ms



* 문제

  > - - 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
  >     - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
  >     - 고른 수열은 오름차순이어야 한다.

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
		dfs(N,M,0,0);
		System.out.println(sb);
		
	}

	public static void dfs(int n, int m, int depth, int bigger) {
		
		if(depth == m) {
			for(int i : arr) {
				sb.append(i).append(" ");
			}
			sb.append('\n');
			return;
		}
		for (int i = bigger; i < n; i++) {
			if(visited[i]) continue;
			visited[i] = true;
			arr[depth] = i + 1;
			dfs(n,m,depth + 1,i);
			visited[i] = false;
		}
	}
}

```

> 15649가 조합문제(순서, 수의 중복 허용)였다면 이번에는 순열 문제다. 배열에 값을 저장하되, 기존에 저장된 큰 값만 저장하면 되므로 쉽게 풀 수 있었다.



### 모범답안

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
 
public class Main {
 
	public static int[] arr;
	public static int N, M;
	public static StringBuilder sb = new StringBuilder();
 
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
 
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
 
		arr = new int[M];
        
		dfs(1, 0);
		System.out.println(sb);
 
	}
 
	public static void dfs(int at, int depth) {
 
		if (depth == M) {
			for (int val : arr) {
				sb.append(val).append(' ');
			}
			sb.append('\n');
			return;
		}
        
		for (int i = at; i <= N; i++) {
 
			arr[depth] = i;
			dfs(i + 1, depth + 1);
 
		}
	}
}
```

> 



