#include <iostream>
#include <vector>
#include <string.h>

#define MAX 51

using namespace std;

int arr[MAX][MAX];
int w, h;
bool visited[MAX][MAX];
int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

void dfs(int x, int y){
	for(int i = 0; i < 8; i++){
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
		if(!visited[nx][ny] && arr[nx][ny]) {
			visited[nx][ny] = true;
			dfs(nx, ny);
		}
	}
}

int main(void){
	while(1){
		cin >> w >> h;
		if(w == 0 && h==0) break;
		memset(arr, 0, sizeof(arr));
		memset(visited, 0, sizeof(visited));
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				int l;
				cin >> l;
				arr[i][j] = l;
			}
		}
		int cnt = 0;
		for(int i = 0; i<h; i++){
			for(int j = 0; j < w; j++){
				if(!visited[i][j] && arr[i][j]){
					cnt++;
					dfs(i,j);
				}
			}
		}
		cout<<cnt<<'\n';
	} 
}

/*
dfs 실버2 문젠데 한 번에 맞춘 건 처음이다 꺅
앞으로 열심히 해야지~~
그리고 주의할 사항은 가로와 세로 뒤바뀌는 것 조심하기.
*/ 
