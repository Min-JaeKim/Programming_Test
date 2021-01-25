# Java

## baek 1946

https://www.acmicpc.net/problem/1946



> 2932ms



* 문제

  > 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.
  >
  > 그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
  >
  > 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.
  >
  > ```python
  > 2
  > 5
  > 3 2
  > 1 4
  > 4 1
  > 2 3
  > 5 5
  > 7
  > 3 6
  > 7 3
  > 4 2
  > 1 4
  > 5 7
  > 2 5
  > 6 12
  > 10
  > 15
  > ```
  >
  > 

* 출력

  > 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.
  >
  > ```python
  > 4
  > 3
  > ```



```python
import java.util.Scanner;

class Main {  
  public static void main(String args[]) { 
      Scanner sc = new Scanner(System.in);
      int test = sc.nextInt();
      for (int i = 0; i < test; i++){
          int count = 1;
          int num = sc.nextInt();
          int[] arr = new int[num+1];
          for (int j = 1; j < arr.length; j++){
              int d = sc.nextInt();
              int v = sc.nextInt();
              arr[d] = v;
          }
          int min_v = arr[1];
          for(int j = 2; j < arr.length; j++){
              if(min_v < arr[j]) continue;
              else {
                  min_v = arr[j];
                  count++;
              }
          }
          System.out.println(count);
      }
      
  } 
}
```

> python에서 java로 푸는 건 괜찮았다. 파이썬보다 시간이 얼마 안걸려서 신기했다.



* 모범답안

  ```python
    public static void main(String[] args) throws NumberFormatException, IOException {
          BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
          int tc = Integer.parseInt(reader.readLine());
   
          while(tc-- > 0) {
              int n = Integer.parseInt(reader.readLine());
              int [] a= new int[n+1];
   
              for(int i=0; i<n; i++) {
                  StringTokenizer st = new StringTokenizer(reader.readLine());
                  int x = Integer.parseInt(st.nextToken());
                  int y = Integer.parseInt(st.nextToken());
                  a[x] = y;
              }
              
              int cnt = 1; //x가 1일때는 무조건 가능하므로 1로 시작
              int standard = a[1]; //기준 값, 처음에는 x가 1일 때의 y값
              for(int i=2; i<=n; i++) {
                  if(standard > a[i]) { //기준 값보다 a[i]의 y값이 작다면 
                      cnt++; //추가
                      standard = a[i]; //기준 값 a[i]의 y값으로 변경
                  }
              }
              System.out.println(cnt);
          }
      }
  
  ```

  > ooops 넘 어렵다. 자바 모범답안도 파이썬 모범답안처럼 readline을 썼다.  처음보는 매서드가 많다.