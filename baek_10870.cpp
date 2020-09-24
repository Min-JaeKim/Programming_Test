#include <iostream>

using namespace std;

int fibonacci(int n){
	if(n == 0) return 0;
	if(n <=2) return 1;
	return fibonacci(n-1) + fibonacci(n-2);
} 

int main(){
	int answer = 0;
	int n;
	cin >> n;
	answer = fibonacci(n);
	cout<<answer<<endl;
}

//자꾸 조건을 제대로 안 읽어서 틀린다.. 

