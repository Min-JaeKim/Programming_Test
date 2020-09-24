#include <iostream>

using namespace std;

int factorial(int n){
	if(n < 1) return 1;
	return factorial(n-1) * n;
} 

int main(){
	int answer = 0;
	int n;
	cin >> n;
	answer = factorial(n);
	cout<<answer<<endl;
}

//factorial 0이 0인줄 알고 틀린 이유도 모르고 있었는데 0의 답은 1이라고 한다.. 
