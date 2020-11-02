#include <iostream>
#include <vector>
#include <queue>

#define MAX 101

using namespace std;

int arr[MAX][MAX];
int w, h;
bool visited[MAX][MAX];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = { 0, 1, 0,-1};
queue<pair<int,int>> q;
int dist[MAX][MAX];

int main(void){
		cin >> h >> w;
		for(int i = 0; i < h; i++){
			string s;
			cin >> s;
			for(int j = 0; j < w; j++){
				arr[i][j] = s[j] - '0';
			}
		}
		q.push(make_pair(0,0));
		dist[0][0] = 1;
		visited[0][0] = true;
		while(!q.empty()){
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			for(int i = 0; i<4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if( nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
				if(arr[nx][ny] && !visited[nx][ny]){
					q.push(make_pair(nx,ny));
					dist[nx][ny] = dist[x][y] + 1;
					visited[nx][ny] = true;
				}
			}
		}
		cout<<dist[h-1][w-1]<<'\n';
}

/* 
dfs로는 도저히 풀리지 않아서 고수들의 소스코드를 보았다.
 bfs가 너비 우선 탐색이니 bfs로 풀어야됨.
 
 + 메모리 초과됨. 
 visited를 while문 밖에 0,0으로 한 번.
 while문 안에 방문하지 않았다고 할 때 한 번. 코드를 적어줘야 됨. 
*/ 
