//백준 문제풀이를 모르고 런타임 에러가 계속 났다.
//1. cin을 넣을 것
//2. main(void)와 return~; 하지말 것 


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int n, k, answer = 0;
	cin >> n >> k;
	vector<int> v(n);
	for(int i = 0; i < n; i++)
		cin >> v[i];
	sort(v.begin(),v.end(),greater<int>());
	for(int i = 0; i<n; i++){
		while(v[i] <= k){
			answer++;
			k-=v[i];
		}
	}
	cout<<answer<<endl;
}
