# python

## swea ? 1952 수영장

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq



> 143ms



* 문제

  > 
  
* 입력

  > 
  >
  > ```bash
  >
  > ```
  
* 출력

  > 
  >
  > ```bash
  > 
  > ```



* 제출

  ```python
  t = int(input())
  for tc in range(1, t+1):
      d, m, tm, y = map(int, input().split())
      swim = list(map(int, input().split()))
      result = y
      dp = [0 for _ in range(13)]
      for i in range(1, 13):
          if i >= 2:
              dp[i] = dp[i-1] + min(swim[i-1]*d, m, dp[i-3] + tm - dp[i-1])
          else:
              dp[i] = dp[i-1] + min(swim[i-1]*d, m)
      result = min(result, dp[-1])
      print('#%d %d' % (tc, result))
  ```
  
  > dp로 풀었다. 처음에 dp 비스무리하게 풀다가 계속 50개 중 47개만 맞길래 dp로 갈아엎었다. 덕분에 많이 발전할 수 있는 계기가 되었다. 구웃,,
  >
  > 그런데 나는 진짜로 swea 실행시간 측정은,, 형평성이 엄청나게 떨어진다고 생각한다. 백준은 안그러는데 swea는 같은 코드를 돌려도 시간이 천차만별이다.
  
  

* 모범답안

  ```python
  118
  
  def main():
      for t in range(1, int(input()) + 1):
          price = list(map(int, input().split()))
          plan = list(map(int, input().split()))
   
          dp = [0]*13
          for i in range(1, 13):
              dp[i] = min(dp[i-1] + plan[i-1] * price[0], dp[i-1] + price[1])
              if i >= 3:
                  dp[i] = min(dp[i-3] + price[2], dp[i])
   
          res = min(dp[12], price[3])
   
          print("#%d %d"%(t, res))
   
   
  if __name__ == '__main__':
      main()
  ```
  
  > 

