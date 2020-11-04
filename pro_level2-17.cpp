#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<string> overlap = {words[0],};
    for(int i = 1; i < words.size(); i++){
        if(overlap[i-1][overlap[i-1].length() - 1] != words[i][0] || 
          find(overlap.begin(), overlap.end(), words[i]) != overlap.end()){
            return { i % n + 1,i / n + 1 };
        }
        else{
            overlap.push_back(words[i]);
        }
    }
    return {0,0};
}

/*
너무 어렵게 구현한 것 같다.
다른 사람들은 map을 썼다.
본받을 것.
그리고 나는 return 값을
if((i+1) % n == 0){
                return{n, (i+1)/n};
            }
            return{((i+1)%n), (i+1)/n  + 1};
이렇게 구현했는데,
ㄷㅏ른 사람이 복잡하지 않게 return하는 것을 보고
따라했다. 후후. 

map으로 푸는 방법

#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    map<string, int>h;
    h[words[0]] = 1;
    for(int i = 1; i < words.size(); i++){
        int len = words[i-1].length();
        if(h[words[i]] || words[i-1][len - 1] != words[i][0])
            return {i % n + 1, i / n + 1};
        h[words[i]] = 1;
    }
    return {0,0};
}

진짜 엄청 쉽다.
점점 남의 코드 읽는 속도가 빨라지고 있다.  
*/ 
