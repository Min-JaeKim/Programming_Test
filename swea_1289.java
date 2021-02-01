# java

## swea 1289

https://swexpertacademy.com/main/solvingProblem/solvingProblem.do



> 



* 문제

  > ※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
  >
  > 원재가 컴퓨터를 만지다가 실수를 저지르고 말았다. 메모리가 초기화된 것이다.
  >
  > 다행히 원래 메모리가 무슨 값이었는지 알고 있었던 원재는 바로 원래 값으로 되돌리려고 했으나 메모리 값을 바꿀 때 또 문제가 생겼다.
  >
  > 메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.
  >
  > 예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.
  >
  > 원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.

* 입력

  > 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  >
  > 각 테스트 케이스는 한 줄로 이루어져 있으며, 메모리의 원래 값이 주어진다.
  >
  > 메모리의 길이는 1이상 50이하이다.
  >
  > ```bash
  > 2
  > 0011
  > 100
  > ```

* 출력

  > 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
  >
  > 초기값(모든bit가 0)에서 원래 값으로 복구하기 위한 최소 수정 횟수를 출력한다.
  >
  > ```bash
  > #1 1
  > #2 2
  > ```



```java
import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            String s = sc.next();
			String[] strArr = s.split("");
            int sig = 0;
            int result = 0;
            for (int i = 0; i < strArr.length; i++){
                if (Integer.parseInt(strArr[i]) != sig){
                    sig = Integer.parseInt(strArr[i]);
                    result++;
                }
            }
            System.out.println("#"+test_case+" "+result);
        }
                 
    }
}
```

> string을 배열로 쪼갤 수 없기 때문에 string을 받고 쪼갤 수 있는 배열에 넣는 방법 밖에 없다.
>
> 그리고 sig를 애초에 문자열로 두었으면 편했겠지만 문자열로 변환하지 않았을 시에는 intger.parseInt로 문자열을 int형으로 형변환할 수 있다.





* 모범답안

  ```python
  import java.util.Scanner;
  
  class Solution {
  
  	public static void main(String[] args) {
  		//System.setIn(new FileInputStream("1289.txt"));
  		Scanner sc = new  Scanner(System.in);
  		int T;
  		T=sc.nextInt();
  		for(int test_case = 1; test_case <= T; test_case++)
  		{
  			String[] tmp = sc.next().split("");
  			String pre = tmp[0];
  			int cnt = (pre.equals("1"))? 1:0;
  			for(String data : tmp) {
  				if(!pre.equals(data)) {
					++cnt;
  				}
  				pre = data;
  			}
  			System.out.printf("#%d %d\n",test_case,cnt);
  		}
  		
  	}
  }
  ```
  
  > equal을 쓰셨다.