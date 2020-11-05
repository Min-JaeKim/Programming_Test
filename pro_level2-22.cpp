#include <string>
#include <vector>
#include <algorithm>

using namespace std;

char totoupper(char c){
    if(97 <= c && c <= 122) c-=32;
    return c;
}

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    vector<string> v;
    for(int i = 0; i < cities.size(); i++){
        if(cacheSize == 0)
            return 5*cities.size();
        for(int j = 0; j < cities[i].size(); j++)
            if(97 <= cities[i][j] && cities[i][j] <= 122) 
                cities[i][j] = totoupper(cities[i][j]);
        if(find(v.begin(), v.end(), cities[i]) == v.end()){
            answer+= 5;
            if(v.size() == cacheSize){
                v.erase(v.begin());
                v.push_back(cities[i]);
            }
            else v.push_back(cities[i]);
        }
        else {
            answer++;
            for(int j = 0; j < v.size(); j++){
                if(v[j] == cities[i]){
                    v.erase(v.begin() + j);
                    v.push_back(cities[i]);
                }
            }
        }
    }
    return answer;
}

/*
처음에 deque로도 풀어보다가 히든 테케에서 통과하지
못하는 것을 확인하고 vector로 고쳤다 헤헤 헷..
카카오 문제 푼 이래로 처음으로 답지 안보고 맞췄다. 
하지만 잘 짠 코드가 아니라고 생각했기 때문에 
다른 사람 풀이를 보았는데 iterator로 푼 풀이가 있었다.
아직 iterator는 이해가 잘 가지 않아서 내 풀이에 
만족하기로 하였다..
*/ 
