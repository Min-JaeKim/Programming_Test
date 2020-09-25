/* 처음 풀었던 풀이 방법, 호기롭게 그리디로 시작했다... 
#include <iostream>
#include <vector>

using namespace std;

#define MAX 101

int array[MAX][MAX];

int getParent(vector<int>& parent, int x){
	if(parent[x] == x) return x;
	return parent[x] = getParent(parent,parent[x]);
}

void unionParent(vector<int>& parent, int a, int b){
	a = getParent(parent,a);
	b = getParent(parent,b);
	a > b ? a = parent[b] : b = parent[a];
}

bool find(vector<int>& parent, int a, int b){
	a = getParent(parent, a);
	b = getParent(parent, b);
	return a==b;
}

int main(){
	int n,m,answer=0,max=0;
	cin >> n >> m;
	vector<int> v[MAX];
	for (int i = 0; i<m; i++){
		int l,r;
		cin>>l>>r;
		v[l].push_back(r);
		v[r].push_back(l);
	}
	vector<int> parent;
	for(int i = 0; i<=n; i++) parent.push_back(i);
	for (auto a : v){
		if(!find(parent, a[0],a[1])) unionParent(parent, a[0],a[1]);
	}
	for (int i = 0; i<n; i++){
		if(getParent(parent,i) == 1) answer++;
	}
	cout<<answer -1 <<endl;
	
}*/


#include <iostream>

#define MAX 101

using namespace std;

int c[MAX];
int n,m,answer=0;
int array[MAX][MAX];

void dfs(int start){
	c[start] = true;
	for(int i = 0; i<=n; i++){
		if(c[i] == true || array[start][i] == 0) continue;
		c[i] = true;
		answer++;
		dfs(i);
	}
}

int main(){
	cin >> n >> m;
	for(int i = 0; i<m; i++){
		int l,r;
		cin >>l>>r;
		array[l][r] = array[r][l] = 1; //연결된 것들은 1로 표시 
	}
	dfs(1);
	cout<<answer<<endl;
}

//드디어 ,, 내 힘으로 dfs를 맞춰보았다. 처음이다 하하하하 이래서 코딩하나보다 
