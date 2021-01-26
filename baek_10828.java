# Java

## baek 10828

https://www.acmicpc.net/problem/10828



> 344ms



* 문제

  > 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
  >
  > 명령은 총 다섯 가지이다.
  >
  > - push X: 정수 X를 스택에 넣는 연산이다.
  > - pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  > - size: 스택에 들어있는 정수의 개수를 출력한다.
  > - empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
  > - top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

* 입력

  > 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
  >
  > ```python
  > 14
  > push 1
  > push 2
  > top
  > size
  > empty
  > pop
  > pop
  > pop
  > size
  > empty
  > pop
  > push 3
  > empty
  > top
  > ```
  >

* 출력

  > 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
  >
  > ```python
  > 2
  > 2
  > 0
  > 2
  > 1
  > -1
  > 0
  > 1
  > -1
  > 0
  > 3
  > ```



```python
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Stack;

class Main {  
  public static void main(String args[]) throws IOException { 
      
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st;
      int count = Integer.parseInt(br.readLine());
      Stack<Integer> stack = new Stack<>();
      
      for(int i = 0; i < count; i++){
          st = new StringTokenizer(br.readLine(), " ");
          
          switch(st.nextToken()) {
              case "push" :
                    stack.push(Integer.parseInt(st.nextToken()));
                    break;
            case "pop":
                System.out.println(stack.empty()? -1:stack.pop());
                break;
            case "size":
                System.out.println(stack.size());
                break;
            case "empty":
                System.out.println(stack.empty()? 1:0);
                break;
            case "top":
                System.out.println(stack.empty()? -1:stack.peek());
          }
         
      }
  } 
}
```

> 여러 가지 방법 끝에 도저히 시간 초과를 해결할 수 없음을 느끼게 되었다. 그래서 buffer로 입력 받는 부분을 다른 사람 코드에서 보고 배우고 베꼈다.
>



* 시간초과했던 답안

  ```java
  import java.util.Scanner;
  
  class Main {  
    public static void main(String args[]) { 
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
      int size = 0;
      int[] stack = new int[size];
      for (int i = 0; i < count; i++) {
  	    String order = sc.next();
  	    if(order.equals("push")) {
  		    int num = sc.nextInt();
  	        int[] tmp = new int[++size];
  	        for(int j = 0; j < stack.length; j++){
  	            tmp[j] = stack[j];
  	        }
  		    tmp[size-1] = num;
  		    stack = tmp;
  	    } else if (order.equals("pop")) {
  	        if(stack.length == 0) {
  			System.out.println(-1);
  			continue;
  		    }
  		    System.out.println(stack[size-1]);
  	        int[] tmp = new int[--size];
  	        for(int j = 0; j < tmp.length; j++){
  	            tmp[j] = stack[j];
  	        }
  	        stack = tmp;
  		
  	    } else if (order.equals("top")) {
  		    if(size == 0) {
  			System.out.println(-1);
  			continue;
  		    }
  		  System.out.println(stack[size-1]);
  	       } else if (order.equals("size")){
  	           System.out.println(stack.length);
  	       } else if (order.equals("empty")){
  	           if(size == 0) System.out.println(1);
  	           else System.out.println(0);
  	       }
      }
    } 
  }
  ```

  > 무슨 바람이 불어 stack 자료구조를 사용하지 않고 직접 구현해서 성공해내고 싶었는데, 역시 문제가 자료구조 사용을 원했던 것인지 계속 시간초과를 하였다.



* 모범답안

  ```python
  import java.io.BufferedReader;
  import java.io.InputStreamReader;
  import java.io.IOException;
  import java.util.StringTokenizer;
   
  public class Main {
   
  	public static int[] stack;
  	public static int size = 0;
   
   
  	public static void main(String[] args) throws IOException {
   
  		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  		StringBuilder sb = new StringBuilder();
  		
  		
  		StringTokenizer st;
  		
  		int N = Integer.parseInt(br.readLine());
   
  		stack = new int[N];
  		
  		while (N-- > 0) {
  			st = new StringTokenizer(br.readLine(), " ");
   
  			switch (st.nextToken()) {
  			
  			case "push":
				push(Integer.parseInt(st.nextToken()));
  				break;
  				
  			case "pop":
  				sb.append(pop()).append('\n');
  				break;
  				
  			case "size":
  				sb.append(size()).append('\n');
  				break;
  				
  			case "empty":
  				sb.append(empty()).append('\n');
  				break;
  				
  			case "top":
  				sb.append(top()).append('\n');
  				break;
  			}
   
  		}
  		System.out.println(sb);
  	}
   
  	public static void push(int item) {
  		stack[size] = item;
  		size++;
  	}
  	
  	public static int pop() {
  		if(size == 0) {
  			return -1;
  		}
  		else {
  			int res = stack[size - 1];
  			stack[size - 1] = 0;
  			size--;
  			return res;
  		}
  	}
  	
  	public static int size() {
  		return size;
  	}
  	
  	public static int empty() {
  		if(size == 0) {
  			return 1;
  		}
  		else {
  			return 0;
  		}
  	}
  	
  	public static int top() {
  		if(size == 0) {
  			return -1;
  		}
  		else {
  			return stack[size - 1];
  		}
  	}
  	
  }
   
  ```
  
  > 처음 보는 메서드가 많다. 다음에 공부히기.