#include <iostream>
#include <vector>
#include <queue>

#define MAX 1001

using namespace std;

queue<pair<pair<int,int>,int>> q;
int arr[MAX][MAX];
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int M,N;
bool visited[MAX][MAX];
int cnt;

void bfs(){
	while(!q.empty()){
		int x = q.front().first.first;
		int y = q.front().first.second;
		cnt = q.front().second;
		q.pop();
		for(int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(nx <0 || ny < 0 || nx >= N || ny >= M) continue;
				if(arr[nx][ny] == 0 && !visited[nx][ny]){
					//arr[nx][ny] = 1;
					visited[nx][ny] = true;
					q.push(make_pair(make_pair(nx,ny), cnt+1));
				}
		}
	}
}

void check(){
	for(int i = 0; i<N; i++){
		for(int j = 0; j<M; j++){
			if(arr[i][j]==0 && !visited[i][j]){
				cnt = -1; break;
			}
		}
	}
}


int main(void){
	cin >> M >> N;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cin >> arr[i][j]; 
			if(arr[i][j] == 1){
				visited[i][j] = true;
				q.push(make_pair(make_pair(i,j),0));
			}
		}
	}
	bfs();
	check();
	cout<<cnt<<'\n';
}

/*
cin 어떻게 받는지 참고함
입력 받을 때 띄어쓰기가 있으므로
string으로 받지 않고 배열로 받아도 됨.
queue pair 방식으로 저장하는 방법 참고.

++ 진짜 어이없게 계속 틀렸습니다가 나왔다.
그 이유는 check 함수에 if문 중괄호가 없기 때문인데
실행은 잘 되는데 왜 코딩사이트에서는 틀렸다고 나오는지
이해가 되지 않는다. 
*/ 
