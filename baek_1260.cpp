#include <iostream>
#include <queue>

using namespace std;

#define MAX 1001

int n,m,start;
int A[MAX][MAX]; // 정점과 정점에 간선이 있는지 확인하는 2차 배열 
int visit[MAX]; //방문한 것을 확인하는 배열 

void dfs(int x){ //깊이 우선 탐색 
	cout<<x<<' '; //변수 출력 
	visit[x] = true; //방문 확인차 true로 
	for(int i = 1; i<=n; i++){ //두 번째 정점부터 연결되어 있는 지 확인 
		if(visit[i] == 1 || A[x][i] == 0) continue; // 이미 방문했거나, 연결이 안되어 있으면 지나감 
		dfs(i); //재귀함수로 dfs표현 
	}
}

void bfs(int v){ //너비 우선 탐색 
	queue<int> q; //너비 우선탐색은 queue를 이용 
	q.push(v); //매개변수를 q에 넣고 
	visit[v] = false; //방문한 것을 false로 표현 
	while(!q.empty()){ //q에 남아있으면 
		int x = q.front(); //q 맨 앞 값을 x에 
		q.pop(); 
		cout<<x<<' '; //q 맨 앞 값 출력 
		for(int i = 1; i<=n; i++){ // 두번째 값부터 for문 
			if(visit[i] == 0 || A[x][i] == 0) continue; // 방문했거나, 연결 안되어 있으면 지나감 
				q.push(i); //방문도 안되어 있고 연결 되어 있으면 q에 삽입 
				visit[i] = false; //방문 처리 
		}
	}
}

int main(){
	cin >> n >> m >> start;
	for(int i = 0 ;i < m; i++){
		int l, r;
		cin >> l>>r; 
        A[l][r] = A[r][l] = 1; // [1][2]의 인접행렬의 값은 [2][1]과 같기 때문

	}
	dfs(start);
	cout<<endl;
	bfs(start);
}



/*
1. if(visit[i] == 1 || A[x][i] == 0) continue;
여기를 visit[매개변수] 로 해서 틀렸다.
2. bfs while문을 if문으로 했더니 1만 출렦됐다.
 */
