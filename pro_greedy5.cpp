#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int>b){
    return a[2] < b[2];
}

int getParent(vector<int>& parent, int x){
	if(parent[x] == x) return x;
	return parent[x] = getParent(parent,parent[x]);
}

void unionParent(vector<int>& parent, int a, int b){
	a = getParent(parent,a);
	b = getParent(parent, b);
	a > b ? parent[a] = b : parent[b] = a;
}

bool find(vector<int>& parent,int a, int b){
	a = getParent(parent,a);
	b = getParent(parent,b);
	return a==b;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0,max = 0;
    sort(costs.begin(), costs.end(), cmp);
    for(auto a:costs) if(max < a[1]) max = a[1];
    vector<int> parent;
    for(int i = 0; i<=max; i++) parent.push_back(i);
    
    for(auto a:costs){
    	if(!find(parent,a[0],a[1])){
    		answer+=a[2];
    		unionParent(parent,a[0],a[1]);
		}
	}
    
    
    return answer;
}
