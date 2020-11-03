#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(count < 0) return false;
        if(s[i] == '(') count++;
        if(s[i] == ')') count--;
    }
    if(count != 0) answer = false;
    return answer;
}

/*
처음에 stack을 사용해서 풀어서 좀 지저분해졌는데
다행히 통과는 되었다.
이후 다시 새롭게 풀었다. 
*/ 
