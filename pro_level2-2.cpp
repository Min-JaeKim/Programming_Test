#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    map<char,int> m;
    for(int i = 0; i<skill.length(); i++)
        m[skill[i]] = i+1;
    for(auto a : skill_trees){
        bool check = true;
        int count = 1;
        for(int i = 0; i<a.length(); i++){
            if(m[a[i]] > count){
                check = false;
                break;
            } else if(m[a[i]] == count) count++;
            else continue;
        }
        if(check) answer++;
    }
    return answer;
}
/*왜이렇게 되는지 모르겠다.
일단 내가 처음에 어떻게 풀었는지 설명해보자면,
skill_trees에서 skill 중간의 문자열들을 먼저 마주치더라도 넘어가게 했기 때문에
통과가 되지 않았다. 즉, 문제 해석을 잘못했단 뜻.
따라서 해쉬를 이용하는 풀이를 보았다.
웬만한 건 다 이해를 했지만
m[skill[i]] = i가 아니라 i+1로 해야하고,
count = 0이 아니라 1로 선언해야 한다.
이유가 무엇인지 모르겠다. ㅠㅠ
*/ 
