#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

#define MAX 50

using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int visited[MAX][MAX] = {0};
int l,m,n;
int arr[MAX][MAX] = {0}; 

void dfs(int y, int x){
	for(int i = 0; i<4; i++){
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx < 0 || ny < 0 || nx >= l || ny >= m) continue;
		if(arr[ny][nx] && !visited[ny][nx]) {
			visited[ny][nx]++;
			dfs(ny,nx);
	}
}
}

int main(void){
	int N,a,b;
	cin >> N;
	for(int i = 0; i<N; i++){
		cin >> l >> m >> n;
		
		int ans = 0;
		memset(arr, 0, sizeof(arr));
        memset(visited, 0, sizeof(visited));
		for(int j = 0; j < n; j++){
			cin >> a >> b;
			arr[b][a] = 1;
		}
		for(int k = 0; k < m; k++)
			for(int h = 0; h < l; h++)
				if(arr[k][h] && !visited[k][h]){
					visited[k][h]++;
					ans++;
					dfs(k,h);
				}
			cout<<ans<<'\n';
			}
	}
	
/*
왜 인지 모르겠는데 memset을 하지 않으니  백준에서 계속 틀렸다고 했다.
memset을 안해도 통과하긴 하는데 이유를 모르겠다.
그리고 x와 y의 좌표를 다르게 해서 계산해야 한다. 왜지?
난 이게 너무 헷갈린다
*/
 
