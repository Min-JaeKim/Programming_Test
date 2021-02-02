# java

## swea d2 1954 달팽이 숫자

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



> 



* 문제

  > 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
  >
  > 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
  
* 입력

  > 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
  >
  > 각 테스트 케이스에는 N이 주어진다.
  >
  > ```bash
  >2    
  > 3   
  > 4      
  > ```
  
* 출력

  > 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
  >
  > (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
  >
  > ```bash
  > #1
  > 1 2 3
  > 8 9 4
  > 7 6 5
  > #2
  > 1 2 3 4
  > 12 13 14 5
  > 11 16 15 6
  > 10 9 8 7
  > ```



```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); // 테스트 케이스 입력
		for (int i = 0; i < T; i++) {
			int n = Integer.parseInt(br.readLine()); // 달팽이 숫자 입력
			int dir = n; // 방향이 아래와 위쪽으로 바뀔 수록 배열 입력 숫자가 줄어들기 때문에 달팽이 숫자로 초기화.
			int[][] array = new int[n+1][n+1]; // 이동할 때마다 행이나 열에 하나 씩 더해지는데, 배열을 초과할 수 있기 때문에 달팽이 숫자보다 1씩 크게 초기화.
			int num = 1; // 달팽이 칸에 넣을 증가되는 숫자
			int col = 0; // 행
			int row = 0; // 열
			int flag = 1; // 방향을 나타내는 숫자 1:오른쪽 2:아래 3:왼쪽 4:위
			for (int j = 0; j < n*2-1; j++) { // 달팽이숫자 * 2 - 1만큼 칸에 수를 입력.
				switch(flag) {
				case 1: // 오른쪽
					for(int k = 0; k < dir; k++) {
						array[col][row++] = num++; // 오른쪽으로 가며 수를 입력
					}
					col++; row--; dir--; // 마지막엔 초과하여 오른쪽으로 갔으므로 row를 하나 빼주고, 이제 달팽이 숫자의 -1만큼 입력하며 되므로 dir를 하나 줄인다.
					flag = 2; // 아래로 이동해야 하므로,
					break;
				case 2:
					for(int k = 0; k < dir; k++) {
						array[col++][row] = num++;
					}
					flag = 3;
					col--; row--;
					break;
				case 3:
					for(int k = 0; k < dir; k++) {
						array[col][row--] = num++;
					}
					col--;row++; dir--;
					flag = 4;
					break;
				case 4:
					for(int k = 0; k < dir; k++) {
						array[col--][row] = num++;
					}
					col++;row++;
					flag = 1;
					break;
				}
			}
			
			System.out.println("#" + (i+1));
			for(int j = 0; j < n; j++) {
				for(int k = 0; k < n; k++) {
					System.out.print(array[j][k] + " ");
				}
				System.out.println();
			}
		}
```

> 코드는 뭐 이렇게 장황하게 짰나 싶기도 한데, 명상을 하며 얻어낸 결과다. 우하하. 의외로 별 문제 아닌데 어떻게 효율적으로 풀어야 하나 고민을 했던 문제.





* 모범답안

  ```java
  import java.util.Arrays;
  import java.util.Scanner;
  
  public class Solution {
  
      static int[] dr = {0,1,0,-1}; // 방향
      static int[] dc = {1,0,-1,0}; // 방향
  
      public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          int T =  sc.nextInt();  //케이스 개수
          for (int tc = 1; tc <= T; tc++) { // 케이스 개수 만큼 반복
              int N = sc.nextInt(); // 사각형 크기 N
              int[][] map = new int[N][N]; //2차원 배열 생성
  
              int cr = 0; //행 숫자
              int cc = 0; //렬 숫자
  
              int input = 1; //첫번째로 입력하는 숫자
              map[cr][cc] = input; //해당하는 위치에 숫자 입력
              input++; //입력 후 숫자 올려주기
  
              for (int i = 0; i < 2*N-1; i++) { // 2N-1 만큼 반복. 방향이 바뀌는 횟수다.
                  while(true) { //한 방향이 유지될때까지 계속 반복
                      int nr = cr + dr[i%4]; // 처음은 +(0,1) -> 우측으로 진행
                      int nc = cc + dc[i%4]; // 두번째 +(1,0) v 아래로 방향 진행
                                             // 세번째 +(0,-1) <- 왼쪽으로 진행
                                             // 네번째 +(-1,0) ^ 위로 방향 진행
                      //System.out.println(nr + " " + nc);
                      if(nr >= 0 && nc >=0 && nr < N && nc < N && map[nr][nc] == 0) {
                          // nr 이 0보다 크면서 nc가 0보다 크고 -> 마이너스 까지 안가야하고
                          // nr<N, nc<N -> 최대값보단 작아야하고
                          // map[][]==0 -> 이미 뭔가 들어 있으면 안된다.
  
                          map[nr][nc] = input; // 위 세가지 조건이 되면 그 자리에 값을 넣고
                          //System.out.println(map[nr][nc]);
                          input++; //인풋 값 하나 올려주고
                      } else { //조건이 안되면 방향을 바꿔줘야하니깐 break로 와일문 나가주고
                          break;
                      }
                      cr = nr; //위치 업데이트
                      cc = nc;
                  }
  
  
              }
  
              System.out.println("#" + tc);
              StringBuilder sb = new StringBuilder();
              for (int i = 0; i < map.length; i++) {
                  for (int j = 0; j < map.length; j++) {
                      sb.append(map[i][j]).append(" ");
                  }
                  sb.append("\n");
              }
  
              sb.delete(sb.length()-1, sb.length());
              System.out.println(sb);
          }
  
  
      }
  }
  ```
  
  > 방향 배열을 이용하여 이동했다. 진짜 깔끔하게 짜셨다. 굿굿.