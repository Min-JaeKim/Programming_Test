#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    string opr;
    int num;
    deque<int> dq;
    for(int i = 0; i<operations.size(); i++){
        opr = operations.at(i);
        num = stoi(opr.substr(2));
        if(opr[0] == 'I'){
            dq.push_back(num);
            sort(dq.begin(), dq.end());
        }
        else {
            if(dq.empty()) continue;
            if(num == 1) dq.pop_back();
            else dq.pop_front();
        }
    }
    if(dq.empty()){
        answer.push_back(0);
        answer.push_back(0);
    } else {
        answer.push_back(dq.back());
        answer.push_back(dq.front());
    }
    return answer;
}
