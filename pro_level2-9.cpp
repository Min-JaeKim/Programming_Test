#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<int> temp;
    vector<pair<int, vector<int>>> v;
    int num = 0;
    for(int i = 1; i < s.length() - 1; i++){
        if( s[i] == '{') continue;
        else if (s[i] == '}'){
            temp.push_back(num);
            v.push_back(make_pair(temp.size(), temp));
            temp.clear();
            num = 0;
        }
        else if (s[i] == ','){
            if(s[i - 1] == '}') continue;
            temp.push_back(num);
            num = 0;
        }
        else {
            num *= 10;
            num += s[i] - '0';
        }
    }
    set<int> set_temp;
    sort(v.begin(), v.end());
    for(pair<int, vector<int>> vt : v){
        for(int num : vt.second){
            if(set_temp.find(num) == set_temp.end()){
                set_temp.insert(num);
                answer.push_back(num);
            }
        }
    }
    return answer;
}


/*
어떻게 풀어야 하는지 모르겠다.
이유는 각 숫자들이 벡터로 주어진 게 아니라 S라는 문자열에 다같이 담겨있기 때문.

-> s문자열을 하나씩 보면서 숫자일 경우에는 
벡터에 넣고 숫자가 아닐 경우에는 어떤 문자열인지에 따라
처리하는 구문을 만들어줌.

set_temp를 안하고
answer를 set으로 만들어서  처리하려고 했더니
반환이 안되는 것 같음.
그리고 set은 push_back이 아니라
insert로 삽입해줘야 됨. 
*/
