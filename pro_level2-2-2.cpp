#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    for(int i = 0; i < skill_trees.size(); i++){
        string tree = skill_trees[i];
        string tmp = skill;
        for(int j = 0; j < tree.length(); j++){
            for(int k = 0; k < tmp.length(); k++){
                if(tmp[k] == tree[j]){ 
                    if(k != 0) goto outside; 
                    else{ 
                        tmp.erase(0,1);
                        k = -1;
                        tree.erase(j,1);
                    }
                }
            }
        }
        answer++;
        outside: continue;
    }
    return answer;
}



/*

두 번째 풀이

*/ 
