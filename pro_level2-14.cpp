#include <iostream>
#include<string>
#include <vector>
#include <stack>
using namespace std;

int solution(string s)
{
    int answer = 0;
    stack<char> even;
    for(int i = 0; i < s.size(); i++){
        if(even.empty()){
            even.push(s[i]);
            continue;
        }
        if(even.top() == s[i]) even.pop();
        else even.push(s[i]);
    }
    if(even.empty()) answer = 1;
    return answer;
}


/*
처음에는 아래와 같이 풀었는데 시간초과가 떴다. 
#include <iostream>
#include<string>
#include <vector>
using namespace std;

int solution(string s)
{
    int answer = 0;
    vector<char> even;
    for(auto n : s) even.push_back(n);
    for(int i = 0; i < even.size(); i++){
        if(even[i] == even[i+1]){
            even.erase(even.begin() + i + 1);
            even.erase(even.begin() + i);
            i = -1;
        }
    }
    if(even.size() == 0) answer = 1;
    return answer;
}

스택을 써보라고 해서 어거지로 썼다,, 부족해 보였다.
그런데 가장 잘 푼 풀이가 내 풀이랑 똑같았다. 다행이다. 
*/
