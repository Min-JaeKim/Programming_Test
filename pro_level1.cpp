#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    set<int> s;
    vector<int> answer;
    for(int i = 0; i < numbers.size(); i++){
        for(int j = 0; j < numbers.size(); j++){
            if( i == j ) continue;
            else s.insert(numbers[i] + numbers[j]);
        }
    }
    for(auto a:s) answer.push_back(a);
    return answer;
}

//python으로 코딩테스트 언어를 바꿔야 하나 고민을 굉장히 많이했다..
//이번 하반기에도 취직 못하면 python으로 바꿔야겠다. 
