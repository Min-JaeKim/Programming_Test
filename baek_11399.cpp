#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int main(){
	int answer = 0;
	int n;
	cin >> n;
	vector<int> v(n);
	for(int i = 0; i<n; i++)
		cin >> v[i];
	sort(v.begin(),v.end());
	queue<int> q;
	for(auto a : v)
		q.push(a);
	while(!q.empty()){
		answer+=q.front()*q.size();
		q.pop();
	}
	cout<<answer<<endl;
}
