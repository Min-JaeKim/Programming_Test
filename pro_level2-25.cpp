#include <string>
#include <vector>

using namespace std;


int solution(int n) {
    int answer = 0;
    int fibo[60001] = {0};
    fibo[1] = 1;
    fibo[2] = 2;
    for(int i = 3; i <= n; i++){
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007;
    }
    return fibo[n];
}

/*
나는 이런 허무맹랑하고 창의적인 것을 못풀어서 큰일이다 ㅜㅜ
좀만 더 생각 오래하고 풀어볼 것,,
*/ 
