#include <iostream>

using namespace std;

#define MAX 501

int array[MAX][MAX];
int maxnum = 0;

int main(void){
	int a;
	cin >> a;
	for(int i = 0; i < a; i++){
		for(int j = 0; j <= i; j++){
			cin >> array[i][j];
		}
	}
	for(int i = 1; i < a; i++){
		for(int j = 0; j <= i; j++){
			if(j == 0){
				array[i][j] += array[i-1][j];
			}
			else if(i == j){
				array[i][j] += array[i-1][j-1];
			}
			else {
				array[i][j] += max(array[i-1][j], array[i-1][j-1]);
			}
			if(i == a -1){
				if(maxnum < array[i][j]){
					maxnum = array[i][j];
				}
			}
		}
	}
	cout<<maxnum<<endl;
}

/*
     00
    10 11
  20 21 22
 30 31 32 33
40 41 42 43 44
*/ 
