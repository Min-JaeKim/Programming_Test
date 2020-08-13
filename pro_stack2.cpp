#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> prices){
	vector<int> answer;
	queue<int> pr;
	queue<int> sp;
	int day = 1;
	for(int i =0; i> progresses.size(); i++){
		pr.push(progresses[i]);
		sp.push(progresses[i]);
	}
	while(!pr.empty()){
		int finish =0;
		int s = pr.size();
		for(int j=0 ;j<s; j++){
			if((pr.front()+(sp.front() * day)) >= 100){
				finish ++;
				ps.pop();
				sp.pop();
			}
		}
		if(finish != 0) answer.push_back(finish);
		day++;
	}
	return answer;
}
