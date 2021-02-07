# java

## swea d2 2001 파리퇴치

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq



> 107ms



* 문제

  > N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
  >
  > 아래는 N=5 의 예이다.
  >
  > M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
  >
  > 죽은 파리의 개수를 구하라!
  >
  > 예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
  >
  > **[제약 사항]**
  >
  > \1. N 은 5 이상 15 이하이다.
  >
  > \2. M은 2 이상 N 이하이다.
  >
  > \3. 각 영역의 파리 갯수는 30 이하 이다.

* 입력

  > 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
  >
  > 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
  >
  > 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
  >
  > ```bash
  > 10
  > 5 2
  > 1 3 3 6 7
  > 8 13 9 12 8
  > 4 16 11 12 6
  > 2 4 1 23 2
  > 9 13 4 7 3
  > 6 3
  > 29 21 26 9 5 8
  > 21 19 8 0 21 19
  > 9 24 2 11 4 24
  > 19 29 1 0 21 19
  > 10 29 6 18 4 3
  > 29 11 15 3 3 29
  > ...
  > ```

* 출력

  > 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
  >
  > (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
  >
  > ```bash
  > #1 49
  > #2 159
  > ...
  > ```



```java
//완료

package com.ssafy;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int i = 1; i <= T; i++) {
			sb.append("#").append(i).append(" ");
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int[][] arr = new int [N][N];
			for(int j = 0; j < N; j++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int j2 = 0; j2 < arr.length; j2++) {
					arr[j][j2] = Integer.parseInt(st.nextToken());
				}
			}
			int max = Integer.MIN_VALUE;
			for(int j = 0;  j <= N-M; j++) {
				for(int k = 0; k <= N-M; k++) {
					int sq_result = 0;
					for (int tmp = 0; tmp < M; tmp++) {
						for (int tmp2 = 0; tmp2 < M; tmp2++) {
							sq_result += arr[j+tmp][k+tmp2];
						}
					}
					if (max < sq_result) max = sq_result;
				}
			}
			sb.append(max).append('\n');
		}
		System.out.println(sb);

	}

}

/*
 * for M까지
 * 	for M까지
 * 
 * 
 */

```

> 한 번 틀렸던 부분은 for문 네 개를 돌릴 때, n-m 보다 미만일 때까지만 도는 걸로 설정해 놓아서 한 번 틀렸다. 미만이 아니라 이하로 설정해 놓았어야 한다. d2다 보니 무난하게 통과할 수 있었던 문제.
>
> 그런데 왜인지 내 코드길이가 항상 어마어마하게 길다... hmmmm,,,,
>
> 방금 알아냈는데 그 이유는 단순한,, 주석 때문이었다. 기본 주석들을 삭제하고 다시 제출하니 1/2나 줄여졌다.



* 모범답안

  ```java
   import java.io.BufferedReader;
  import java.io.IOException;
  import java.io.InputStreamReader;
  import java.util.Arrays;
  import java.util.StringTokenizer;
   
  public class Solution{
      public static void main(String[] args) throws IOException{
          BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
          StringBuilder sb=new StringBuilder();
          int tn=Integer.parseInt(br.readLine());
          for(int i=1;i<=tn;i++) {
              String[] str=br.readLine().split(" ");
              int N=Integer.parseInt(str[0]);
              int M=Integer.parseInt(str[1]);
              int[][] nArray=new int[N][N];
              int [] max=new int[(N-M+1)*(N-M+1)];
              int count=0;
               
              for(int j=0;j<N;j++) {
                  StringTokenizer st=new StringTokenizer(br.readLine());
                  for(int k=0;k<N;k++) {
                      nArray[j][k]=Integer.parseInt(st.nextToken());
                  }
              }
               
              for(int j=0;j<=(N-M);j++) {
                  for(int k=0;k<=(N-M);k++) {
                      for(int l=0;l<M;l++) {
                          for(int m=0;m<M;m++){
                              max[count]=max[count]+nArray[j+l][k+m];
                          }
                      }
                      count++;
                  }
              }
              Arrays.sort(max);
              System.out.println("#"+i+" "+max[(N-M+1)*(N-M+1)-1]);
               
               
          }
           
      }
  }
  ```
  
  > 69ms짜리,, 대박이다 내가 if문을 썼지만 이분은 더한 수를 또다른 배열에 넣고 sort를 통해 최고값을 출력해 냈다.