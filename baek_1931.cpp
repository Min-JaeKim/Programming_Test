#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//cmp함수에서 에러가 났는데, 그 이유는 모르겠다 ㅜㅜ typedef로 수정해주니 에러가 나지 않았다. 
typedef pair<int,int> P;
vector<P> v;
//위에 두줄은 잘 알아둘 것. 

bool cmp (P a, P b){
	if(a.second == b.second){
        return a.first < b.first;
    }
    else{
        return a.second < b.second;
    }
}

int main(){
	int answer = 1;
	int n;
	cin >> n;
	//vector<pair<int,int>> v(n);
	int l, r;
	for(int i = 0; i < n; i++){
		cin >> l >> r;
		v.push_back(make_pair(l,r));
	}
	sort(v.begin(),v.end(),cmp);
	int temp = v[0].second;
	for(int i = 1; i<n; i++){
		if(temp <= v[i].first){
			answer++;
			temp = v[i].second;
		}
	}
	cout<<answer<<endl;
}

/*
		
		for(auto a : v){
		if(temp <= a.first){
			answer++;
			temp = a.second;
		}
	} // 원래 내가 했던 코드인데 이게 틀린이유가 무엇이냐면
	첫번째 배열조차 같이 계산해버림. 
	정석대로라면 두 번째 열부터 계산해야함
	반례는
	(4 / 1 1 / 1 3 / 4 5 / 6 9)
	답은 4가 나와야 하지만, 이코드는 5가 나오게 됨. 
		
*/
