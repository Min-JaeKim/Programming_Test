#include <iostream>
using namespace std;


void quicksort(int* data, int start, int end){
	if(start >= end) return;
	
	int key = start;
	int i = start + 1, j = end, temp;
	
	while(i<=j){
		while(i <= end && data[i] <= data[key])
			i++;
		while(j>start && data[j]>=data[key])
			j--;
		if(i>j){
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		} else {
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
		}
	}
	quicksort(data,start,j-1);
	quicksort(data,j+1,end);
}

int main(void){
	int array[] = { 4 , 5, 7, 8, 2, 1, 9, 10, 3, 6};
	
	quicksort(array, 0, 9);
	
	for(int i=0; i<10; i++)
		cout<<array[i]<<" ";
}
