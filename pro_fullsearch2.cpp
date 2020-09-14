소수 문제로 알게 된 것

1. 매개 변수를 다 넣지 않을 경우에 값을 주지 않을 매개 변수는 초기화를 미리 시켜준다.

2. set : 수를 중복이 되지 않게 차례로 저장시키는 라이브러리

3. 벡터를 push_back할 땐 push_bakc({~~,~~}) 소괄호 중괄호 이용



#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

void push(vector<pair<char, bool>> piece, set<int>& p, string a = "", int cnt = 0){
    for(int j = 0; j<piece.size(); j++){
        if(!piece[j].second){
            piece[j].second = true;
            a+= piece[j].first;
            p.insert(stoi(a));
            cnt++;
        } else continue;
        if(cnt != piece.size()) push(piece,p,a,cnt);
        piece[j].second = false;
        a=a.substr(0, a.length()-1);
        cnt--;
    }
}

bool Decheck(int a){
    for(int i = 2; i<=sqrt(a); i++)
        if(a%i == 0) return false;
    return true;
}

int solution(string numbers) {
    int answer = 0;
    vector<pair<char, bool>> piece;
    set<int> p;
    for(int i =0; i<numbers.length(); i++)
        piece.push_back({numbers[i],false});
    push(piece,p);
    for(auto c : p){
        if(c == 0 || c == 1) continue;
        if(Decheck(c)) answer++;
    }
    return answer;
}



