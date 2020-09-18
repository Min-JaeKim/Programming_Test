/* //처음에 했던 것,, 보기 싫을 정도로 되게 복잡하다. 
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <stack>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int weight = 0;
    vector<pair<int, bool>> v;
    for(int i =0; i<people.size(); i++)
        v.push_back({people[i],false});
    for(int i =0; i<v.size(); i++){
        weight = limit;
        if(weight >= v[i].first && v[i].second == false) {
            answer ++;
            v[i].second = true;
            weight -= v[i].first;
            for(int j = i+1; j<v.size(); j++){
                if(weight >= v[j].first && v[j].second == false) {
                    v[j].second = true;
                    cout<<weight<<endl;
                    weight-= v[j].first;
                }
            }
        }
            }
            cout<<answer;
    return answer;
}

int main(void){
	solution({10,20,30,40,50,60,70,80,90}, 100);
	return 0;
}

*/


//greedy의 특성을 잘 파악하고 풀 것. 
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0, big = 0, small =people.size()-1, cnt = 0;
    sort(people.begin(), people.end(), greater<>());
    while(1){
            int first = people[big++];
            cnt++;
        if(people[small]<=limit - first){
            small--;
            cnt++;
        }
        answer++;
        if(cnt >= people.size()) break;
    }
    return answer;
}
