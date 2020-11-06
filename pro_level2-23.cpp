#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int,double>& a, pair<int,double>& b){
    if(a.second == b.second) return a.first < b.first;
    return a.second > b.second;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<int,double>> fail;
    float people = stages.size();
    sort(stages.begin(), stages.end());
    for(int i = 1; i <= N; i++){
        int count = 0;
        for(int j = 0; j < stages.size(); j++){
            if(stages[j] == i){
                count++;
            }
        }
        if(count == 0) fail.push_back(make_pair(i,0));
        else fail.push_back(make_pair(i,count/people));
        people -= count;
    }
    sort(fail.begin(), fail.end(), compare);
    for(auto a : fail) answer.push_back(a.first);
    return answer;
}

/*
처음에 좀 헤매서 스테이지 수 대로 개수 세는 것은
다른 사람을 좀 모방했다...
조금 더 시간을 줄일 수 있을 것 같은데 잘 안되어서
그냥 시간 줄이는 건 포기 ㅠㅠ
*/ 
