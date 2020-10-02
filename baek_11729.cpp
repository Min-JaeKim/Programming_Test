#include <iostream>

using namespace std;

void hanoi(int n, int start, int middle, int end){
	if(n ==1 ) {
		cout << start <<' '<<end<<endl;
	}
	else{함 
		hanoi(n-1,start,end,middle);
		cout<<start<<' '<<end<<endl;
		hanoi(n-1,middle,start,end);
	}
}

int main(void){
	int n;
	cin >> n;
	cout << (1<<n) -1 <<endl;
	hanoi(n,1,2,3);
	return 0;
}

//재귀에 약하다 보니 오래걸렸던 문제,,
//줄바꿈은 endl로 사용하면 시간 초과라고 뜨기 때문에 '\n'을 써야 
