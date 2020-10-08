#include <string>
#include <vector>

using namespace std;

int answer{50};

void dfs(string begin, string target, vector<string> words, vector<bool>& useCheck, int check=0){
	for(int i = 0; i<words.size(); i++){
		int temp = 0;
		for(int j = 0; j<words[i].size(); j++)
				if(!useCheck[i] && words[i][j] == begin[j]) temp++;
		    if(temp >= words[i].size() - 1){
			    if(target == words[i]&& answer > check+1) {
                    answer = check+1;
                    return;
                }
                useCheck[i] = true;
                dfs(words[i],target,words,useCheck,check+1);
                useCheck[i] = false;
		    }
	}
    }

int solution(string begin, string target, vector<string> words) {
    vector<bool> useCheck(words.size(),false);
    dfs(begin, target, words,useCheck);
	if(answer == 50) return 0;
    return answer;
}





/* 시행착오를 많이 겪은 아래의 코드,, answer의 최솟값을 구해야 했기 때문에 결론적으로는 틀렸었다. 
#include <string> 
#include <vector>
#include <iostream>

using namespace std;

int dfs(string begin, string target, vector<string>& words, int& answer){
	string s = words[0];
	for(int i = 0; i<words.size(); i++){
		//cout<<s<<endl;
		int temp = 0; //전 문자열과 얼마나 같은지 ++ 
		for(int j = 0; j<words[i].size(); j++){
			//cout<<s<<endl;
			if(i == 0){
				if(words[i][j] == begin[j]) {
					//cout<<words[i][j]<<' '<<begin[j];
					temp ++;
					//cout<<temp<<endl;
				}
			}
			else{
				s = words[i-1];
				//cout<<s<<endl;
				if(words[i][j] == s[j]) {
				temp++;
				//cout<<words[i][j]<<' '<<s[j]<<endl;
				}
			}
		}
		if(temp >= words[i].size() - 1){
			cout<<words[i]<<endl;
			answer++;
			//cout<<words[i]<<endl;
			if(target == words[i]) return answer;
		}
	}
	
       /* for(int j = 0; j < words.size(); j++){
            int temp = 0;
            for(int i = 0; i<begin.size(); i++){
                if(begin[i] == words[j][i]){
                    temp++;
                    cout<<words[j]<<endl;
                    cout<<temp<<endl;
                }
            }
            if(temp >= begin.size() -1){
                check++;
                cout<<check<<endl;
                if(target == words[j]) return check;
            }
        }
        return 0;
    }

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    dfs(begin, target, words, answer);
    cout<<answer<<endl;
    return answer;
}

int main(void){
	solution("hit","cog",{"hot", "dot", "dog", "lot", "log", "cog"});
}*/
