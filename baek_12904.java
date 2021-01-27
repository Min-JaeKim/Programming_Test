# Java

## baek 12904

https://www.acmicpc.net/problem/12904



> 540ms



* 문제

  > 수빈이는 A와 B로만 이루어진 영어 단어가 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.
  >
  > 이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
  >
  > - 문자열의 뒤에 A를 추가한다.
  > - 문자열을 뒤집고 뒤에 B를 추가한다.
  >
  > 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

* 입력

  > 첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 999, 2 ≤ T의 길이 ≤ 1000, S의 길이 < T의 길이)
  >
  > ```python
  > B
  > ABBA
  > ```
  > 
  >
  
* 출력

  > S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
  >
  > ```python
  > 1
  > ```



```java
import java.io.*;

class Main {  
  public static void main(String args[]) throws IOException { 
      
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String s = br.readLine();
		String t = br.readLine();
		
		while (s.length() != t.length()) {
			int tlen = t.length();
			if(t.charAt(tlen-1) == 'A') {
				t = t.substring(0, tlen-1);
			}
			else {
				t = t.substring(0, tlen-1);
				String tmp = "";
				for (int i = t.length()-1; i > -1; i--) {
					tmp += t.charAt(i);
				}
				t = tmp;
			}
		}
		
		if(t.equals(s)) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
      
  } 
}
```



> java에서는 해결방법이 곧잘 생각나지 않았는데 파이썬으로 금방 끝내버린 문제,,
>
> * __import java.io.*;__ : bufferedReader를 쓰기 위해 import
> * __BufferedReader br = new BufferedReader(new InputStreamReader(System.in));__ : scanner보다 좋음.
> * __String s = br.readLine();__ : buffer로 입력받을 때는 readLine()





* 모범답안

  ```java
  import java.io.*;
  
  class Main {  
    public static void main(String args[]) throws IOException { 
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  
  		String s = br.readLine();
  		String t = br.readLine();
  		
  		while (s.length() != t.length()) {
  			int tlen = t.length();
  			if(t.charAt(tlen-1) == 'A') {
  				t = t.substring(0, tlen-1);
  			}
  			else {
  				t = t.substring(0, tlen-1);
  				t = new StringBuffer(t).reverse().toString();
  			}
  		}
  		
  		if(t.equals(s)) {
  			System.out.println(1);
  		} else {
  			System.out.println(0);
  		}
        
    } 
  }
```
  
  > 내가 푼 풀이에서 좀 변형한 건데, 내 실행시간이 다른 분들보다 5배는 더 되길래 for문을 없애보았다.
  >
  > * __t = new StringBuffer(t).reverse().toString();__ : new StringBuffer를 통해 t문자열을 뒤집을 수 있었다. 여기서 중요 포인트는 __StringBuffer()__

