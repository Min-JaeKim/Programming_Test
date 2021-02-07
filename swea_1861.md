# java

## swea d4 1861 정사각형방

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc



> 140ms



* 문제

  > N2개의 방이 N×N형태로 늘어서 있다.
  >
  > 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
  >
  > 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
  >
  > 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
  >
  > 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.
  >
  > 다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.
  >
  > Ai, j는 모두 서로 다른 수이다.
  >
  > ```bash
  > 2
  > 2
  > 1 2
  > 3 4
  > 3
  > 9 3 4
  > 6 1 5
  > 7 8 2
  >  
  > ```

* 출력

  > 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
  >
  > 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.
  >
  > 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.
  >
  > ```bash
  > #1 1 2
  > #2 3 3
  > ```



```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
	
	private static int[] dx = {-1, 1, 0, 0};
	private static int[] dy = {0, 0, -1, 1};
	private static int size;
	private static int[][] arr;
	private static int[][] memo;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int tc = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= tc; testCase++) {
			sb.append("#").append(testCase).append(" ");
			size = Integer.parseInt(br.readLine());
			arr = new int[size][size];
			memo = new int[size][size];
			for(int i = 0; i < size; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				for (int j = 0; j < size; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int max = Integer.MIN_VALUE;
			int array_num = Integer.MAX_VALUE;
			for (int i = 0; i < size; i++) {
				for (int j = 0; j < size; j++) {
					int num = go(i,j); // 결과값
					System.out.print(num + " ");
					if(max <num || max == num && arr[i][j] < array_num ) {
						max = num;
						array_num = arr[i][j];
					}
				}
				System.out.println();
			}
			sb.append(array_num).append(" ").append(max).append('\n');
					}
		System.out.println(sb);
	}
	
	public static int go(int r, int c) {
		if(memo[r][c] != 0) {
			return memo[r][c];
		}
		memo[r][c] = 1;
		
		for (int i = 0; i < 4; i++) {
			int nr = r + dx[i];
			int nc = c + dy[i];
			
			if(0 <= nr && nr < size && 0 <= nc && nc < size && arr[r][c] + 1 == arr[nr][nc]) {
				memo[r][c] += go(nr,nc);
				break;
			}
		}
		return memo[r][c];
	}

}

```

> 진짜,, 바보인가 싶었던 문제,,, 메모이제이션과 재귀를 사용했던 문제다.
>
> 이중에서 내가 엄청 바보 같이 풀었던 부분은
>
> **if(max <num || max == num && arr[ i ] [ j ] < array_num )**
>
> 이부분인데 
>
> **if(max <= num && arr[ i ] [ j ] < array_num )**
>
> 이것과 혼동을 하는 바람에 헷갈렸었다. 아래는 두가지 조건을 충족해야 하므로 내가 원하는 답이 나오지 않았을 것이다.
>
> 위에는 num이 max보다 커야하고, 만약 두 수가 같다면 array 수를 판별하는 것이다.
>
> 아 그리고 한가지 더, 재귀부분에서 
>
> __memo[r] [c] = 1;__
>
> 이거 안해줘서 답이 또 안나옴 ㅜㅜ ㅡㅡ...;;;



* 모범답안

  ```java
  
  ```
  
  > 