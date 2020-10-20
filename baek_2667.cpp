#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 25

using namespace std;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};
int N;
bool check[MAX][MAX]; //방문 표시 	
int arr[MAX][MAX];
int home_count;

void dfs(int x, int y){
	home_count++;
	check[x][y] = true;
	for(int i = 0; i<4; i++){
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
		if(arr[nx][ny] == 1 && check[nx][ny] == false)
			dfs(nx, ny);
	}
}


int main(void){
	cin >> N;
	vector<int> v;
	for(int i = 0; i<N; i++){
		string temp;
		cin >> temp;
		for(int j = 0; j < N; j++)	arr[i][j] = temp[j] - '0';
	}
	for(int i = 0; i < N; i++){
		for(int j = 0; j<N; j++){
			if(arr[i][j] == 1 && check[i][j] == false){
				home_count = 0;
				dfs(i, j);
				v.push_back(home_count);
			}
		}
	}
	sort(v.begin(), v.end());
	cout<<v.size()<<'\n';
	for(auto a : v) cout<< a << '\n';
}
/*
도움 받은 목록들 
문자열 어떻게 저장하는지 잘 모름
집 개수 세는 거

계속 안되던 원인은 
내가 전역변수로 bool check를 이미 선언해놨는데 main함수에
또 선언하면서 false로 초기값을 설정하게 되어 실행되지 않았다.
원인은 정확히 파악하진 못했는데 전역변수를 쓸 때 조심해야할 
문제인 것 같다.

그래도 남의 코드를 거의 베끼지 않고 쓰려고 노력했다 하하
dfs 문제를 더 많이 풀어보아야 할 것 같다. 

ps. 몇날 며칠 고민하다가 풀기를 포기한 문제인데(dx, dy를 이해하지 못해서)
에네첸 연습문제인 걸 알고 풀게 되었다  ㅋㅋ ㅠㅠㅠㅠ 에네첸 가고 싶다. 
*/ 

