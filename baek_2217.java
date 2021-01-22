# Java

## baek 2217

https://www.acmicpc.net/problem/2217



> 256ms



* 문제

  > N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
  >
  > 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
  >
  > 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

* 입력

  > 첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.
  >
  > ```python
  > 2
  > 10
  > 15
  > ```
  >
  > 

* 출력

  > 첫째 줄에 답을 출력한다.
  >
  > ```python
  > 20
  > ```



```python
import java.util.Scanner;
import java.util.Arrays;

class Main {  
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr = new int [n];
    for (int i = 0; i < n; i++){
        int k = sc.nextInt();
        arr[i] = k;
    }
    Arrays.sort(arr);
    int max = Integer.MIN_VALUE;
    int j = 1;
    for(int i = n-1; i >= 0; i--){
        int k = arr[i] * j;
        if(max < k){
            max = k;
        }
        j++;
    }
    System.out.println(max);
  } 
}
```

> java로 코테를 치기에는 역시 아직 약세임을 느꼈다.
>
> 문제는 코테를 치는 대다수의 기업이 java의 ide 툴을 제공안한다는 것인데, 그렇기 때문에 java로 코테를 보기 위해서는 import를 외워야 할 것 같다,, 
>
> 그리고 믕층한걸로 시간 낭비하지 말것!!! 꼼꼼히 코딩하기!





* 모범답안

  ```python
  import java.io.BufferedReader;
  import java.io.IOException;
  import java.io.InputStreamReader;
  import java.util.Arrays;
  import java.util.StringTokenizer;
   
  public class B_2217 {
   
      public static void main(String[] args) throws IOException {
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          StringTokenizer st = new StringTokenizer(br.readLine());
          
          int cnt = Integer.parseInt(st.nextToken());
          int arr[] = new int[cnt];
          for(int i=0; i < cnt; i++) {
              st = new StringTokenizer(br.readLine());
              arr[i] = Integer.parseInt(st.nextToken());
          }
          Arrays.sort(arr);
          
          long max = 0;
          for(int i = cnt-1; i >= 0; i--) {
              arr[i] = arr[i] * (cnt-i);
              if(max < arr[i]) max = arr[i];
          }
          System.out.println(max);
      }
  }
  ```

  > 처음 보는 메서드가 많다. 다음에 공부히기.