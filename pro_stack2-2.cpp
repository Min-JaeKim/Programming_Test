#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    for(int i = 0; i < progresses.size(); i++){
        int day = 0;
        int temp = 100 - progresses[i];
        while(temp > 0){
            temp -= speeds[i];
            day++;
        }
        q.push(day);
    }
    while(!q.empty()){
        int count = 1;
        int num = q.front();
        q.pop();
        cout<< num << ' ';
        while(q.size() >= 1){
            if(num >= q.front()){   
                q.pop();
                count++;
            }
            else break;
        }        
        answer.push_back(count);
    }
    return answer;
}

/*
내 방식대로 새롭게 풀어봤다 . 헤헤
*/ 
