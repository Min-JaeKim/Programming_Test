#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> listen;
    map<string, map<int, int>> num;
    for(int i = 0; i < genres.size(); i++){
        listen[genres[i]] += plays[i];
        num[genres[i]][i] = plays[i];
    }
    while(listen.size() != 0){
        string song{};
        int max{0};
        for(auto a : listen){
            if(max < a.second){
                max = a.second;
                song = a.first;
            }
        }
        for(int i = 0; i < 2; i++){
            int val = 0, idx = -1;
            for(auto a : num[song]){
                if(val < a.second){
                    val = a.second;
                    idx = a.first;
                }
            }
            if(idx == -1) break;
            answer.push_back(idx);
            num[song].erase(idx);
        }
        listen.erase(song);
    }
    return answer;
}


/*
하진짜 어려웠다.
해시는 원래 다 이런 것인가,,
이 문제 덕에 해시 사용법을 조금 익힌 것 같다. 
카카오처럼 문자열이 손도 못댈 정도의 느낌은 아니었는데,
unordered_map하고 map하고 헷갈려서 시간이 지체되었다.
map은 자동으로 정렬해주지만 시간이 조금 더 오래 걸리고,
unordered_map은 정렬이 안되지만 시간은 짧게 ㅎㅎ
*/ 
