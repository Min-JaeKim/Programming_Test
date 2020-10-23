#include <iostream>
#include <vector>

#define MAX 1001

using namespace std;

vector<int> arr[MAX];
int M,N;
bool visited[MAX];

void dfs(int a){
	visited[a] = true;
	for(int i = 0; i < arr[a].size(); i++){
		int next = arr[a][i];
		if(!visited[next]){
			dfs(next);
		}
	}
}

int main(void){
	cin >> N >> M;
	for(int i = 0; i < M; i++){
		int l,r;
		cin>>l>>r;
		arr[l].push_back(r);
		arr[r].push_back(l);
	}
	int cnt = 0;
	for(int i = 1; i <= N; i++){
		if(!visited[i]){
			dfs(i);
			cnt++;
		}
	}
	cout << cnt << '\n';
}
/*
이렇게 쉬운 문제도 못맟히다니,,,
main에 두 번째 for문은 1부터 시작해줘야 한다.
습관처럼 0부터 시작하면 안된다. 왜냐면 arr시작은 1이기 때문이다.
연결이 되어 있으면 서로의 벡터에 push_back해줘야 한다.
끝
*/ 
