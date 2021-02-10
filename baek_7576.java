# Java

## baek 7576 토마토

https://www.acmicpc.net/problem/7576



> 604ms



* 문제

  > 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 
  >
  > ![img](md-images/tmt.png)
  >
  > 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
  >
  > 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

* 입력

  > 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
  >
  > 토마토가 하나 이상 있는 경우만 입력으로 주어진다.
  >
  > ```bash
  > 6 4
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 1
  > ```

* 출력

  > 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
  >
  > ```bash
  > 8
  > ```



```java
package com.ssafy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_7576 {

	private static int[][] arr;
	static Queue<Integer> que_col = new LinkedList<Integer>();
	static Queue<Integer> que_row = new LinkedList<Integer>();
	private static int[] dx = {-1,1, 0, 0};
	private static int[] dy = {0, 0, -1, 1};
	private static int col;
	private static int row;

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		col = Integer.parseInt(st.nextToken()); // 열 입력
		row = Integer.parseInt(st.nextToken()); // 행입력
		arr = new int [row][col]; // 배열 정의
		for (int i = 0; i < row; i++) { // 배열 받을 for문
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < col; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 0; i < row; i++) { // 행과
			for (int j = 0; j < col; j++) { // 열을 지나면서 
				if (arr[i][j] == 1) { // 익은 토마토가 있다면
					que_row.offer(i); // que에 넣어줌 ({i,j}를 동시에 넣는 게 익숙치 않아서
					que_col.offer(j); // 행과 열을 넣는 que를 따로
				}
			}
		}
		bfs(); // bfs를 돌린다
		int max = Integer.MIN_VALUE; // 이전 익은 토마토의 값보다 1씩 증가하며 넣어줬으므로, 배열에서 max값을 찾아가야함.
ex:		for (int i = 0; i < row; i++) { // for문으로 토마토 농장 돌기
			for (int j = 0; j < col; j++) {
				if (arr[i][j] > max) { // 마지막에 익은 토마토의 값이 가장 클 것이므로,
					max = arr[i][j]; // max값에 넣어준다.
				}
				if (arr[i][j] == 0) { // 만약 안익은 토마토가 하나라도 있으면
					max = 0; // max를 0으로 설정하고 이중포문 나와줌
					break ex;
				}
			}
		}
		System.out.println(max-1); // 최대값에서 1을 빼준다.
	}

	public static void bfs() { 
		while(!que_row.isEmpty()) { // que가 비지 않았다면
			int r = que_row.poll(); // 행 꺼내고
			int c = que_col.poll(); // 열 꺼내서 변수에 저장한 뒤
			for (int i = 0; i < 4; i++) { // 방향키를 설정하는 for문
				int nx = r + dx[i]; // 상하좌우 순서
				int ny = c + dy[i];
				if(nx >= 0 && nx < row && ny >= 0 && ny < col && arr[nx][ny] == 0) { // 배열 안에 있는 값이면서 익지 않았다면
					arr[nx][ny] = arr[r][c] + 1; // 그대로 그 전에 더했던 익은 토마토에 1을 더함.
					que_row.offer(nx); // 그리고 que에 다시 넣어준다.
					que_col.offer(ny);
				}
			}
		}
	}
}

/*
 * 1 2 3 4 5 6
 * 2 3 4 5 6 7
 * 3 4 5 6 7 8
 * 4 5 6 7 8 9
 * bfs를 처리하면 위와 같은 배열이 완성될 것이다.
 * 
 * */
 */
```

> 



* 모범답안

  ```python
  
  ```

  > 