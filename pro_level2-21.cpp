#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    stringstream ss;
    string id, action, nick;
    vector<string> uid;
    map<string, string> info;
    for(int i = 0; i < record.size(); i++){
        ss.str(record[i]);
        ss >> action;
        if(action == "Enter"){
            ss >> id;
            ss >> nick;
            uid.push_back(id);
            info[id] = nick;
            answer.push_back("님이 들어왔습니다.");
        }
        else if(action == "Leave"){
            ss >> id;
            uid.push_back(id);
            answer.push_back("님이 나갔습니다.");
        }
        else {
            ss >> id;
            ss >> nick;
            info[id] = nick;
        }
        ss.clear();
    }
    for(int i = 0; i < answer.size(); i++){
        answer[i] = info[uid[i]] + answer[i];
    }
    return answer;
}

/*
휴.. 어찌어찌 풀다가 도저히 띄어쓰기 부분을
어떻게 처리해야할 지 몰라서 찾아봤더니
sstream이라는 STL이 있었다.
과거 쿠팡 코테도 저런 게 나왔었는데 이제라도 알아서 
다행이다...

그리고 중요한 것은 FOR문 마지막에 SS를 CLEAR해주는 게
중요하다.

또 한가지.
map<string1, string2> m;
는  m[string1] = string2;
로 값 변경 가능... 
*/ 
