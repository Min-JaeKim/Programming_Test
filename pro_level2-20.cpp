#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int answer = 1;
    while(answer < n / 2){
        if(b % 2 == 0 && a == (b-1)) break;
        if(a % 2 == 0 && b == (a-1)) break;
        answer++;
        a = a / 2 + a%2;
        b = b / 2 + b%2;
    }
    return answer;
}

/*
뭔데 이문제를 이렇게 오래 풀었을까 ㅜ
거진 35분 걸린듯,,
하지만 다른 사람 풀이를 보지 않은 데에 의의를 둔다.
*/ 
