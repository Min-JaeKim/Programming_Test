#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare (pair<string, pair <int,int> > a,
			  pair<string, pair <int, int> > b) {
			  	if(a.second.first==b.second.first)
			  		return a.second.second > b.second.second;
			  	else
			  		return a.second.first < b.second.first;
			  }
			  
int main(void) {
	vector <pair <string, pair<int, int> > > v;
	v.push_back(pair <string, pair<int, int> > ("±ט",make_pair(99,19961029)));
	v.push_back(pair <string, pair<int, int> > ("ÀÌ",make_pair(77,19921029)));
	v.push_back(pair <string, pair<int, int> > ("park",make_pair(84,19951029)));
	v.push_back(pair <string, pair<int, int> > ("na",make_pair(99,19911029)));
	v.push_back(pair <string, pair<int, int> > ("choi",make_pair(84,19931029)));
	
	sort(v.begin(),v.end(),compare);
	for(int i = 0; i<v.size(); i++)
	cout<<v[i].first<< ' ';
	return 0;
}
