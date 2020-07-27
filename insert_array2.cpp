#include <iostream>
using namespace std;

int main(void){
	int array[] = { 4 , 5, 7, 8, 2, 1, 9, 10, 3, 6};
	int temp;
	for (int i = 0; i<10; i++){
		for(int j=i; j>0; j--){
			if(array[j]<array[j-1]){
				temp = array[j-1];
				array[j-1] = array[j];
				array[j]=temp;
				
			}
		}
	}
	
	for(int i=0; i<10; i++)
		cout<<array[i]<<" ";
}
