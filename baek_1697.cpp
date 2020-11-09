#include <iostream>
#include <queue>

using namespace std;

#define MAX 100001

int bfs(int i, int j){
	queue<pair<int, int>> q;
	bool visit[100001] = {false};
	q.push(make_pair(i, 0));
	visit[i] = true;
	while(!q.empty()){
		int num = q.front().first;
		int idx = q.front().second;
		q.pop();
		if(j == num){
			return idx;
		}
		if(num + 1 < MAX && !visit[num+1]){
			q.push(make_pair(num+1, idx+1));
			visit[num+1] = true;
		}
		if(num - 1>= 0 && !visit[num-1]){
			q.push(make_pair(num-1, idx+1));
			visit[num-1] = true;
		}
		if(num*2 < MAX && !visit[num*2]){
			q.push(make_pair(num*2, idx+1));
			visit[num*2] = true;
		}
	}
}

int main(void){
	int i, j;
	cin >> i >> j;
	cout<<bfs(i,j)<<' ';
}

/*
초기화를 하지 않으면 계속  런타임 에러가 뜬다.
주의할 것.

다른 사람들은 이런 풀이를 어떻게 하는지 궁금하다.
나는 아직 한참 멀었다는 것을 느낀 bfs문제였다.

*/ 
