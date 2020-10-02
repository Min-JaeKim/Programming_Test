#include <iostream>
#include <string>

using namespace std;

string s;

int result(void){
	bool minus = false;
	int sum = 0;
	string temp = "";
	for(int i=0; i<=s.length(); i++){
		if(s[i] == '+' || s[i] == '-' || s[i] == '\0'){
			if(minus) sum-=stoi(temp);
			else sum+= stoi(temp);
			if(s[i] == '-') minus = true;
			temp = "";
			continue;
		}
		temp += s[i];
	}
	return sum;
}

int main(void){
	cin >> s;
	cout<<result()<<endl;
}

//문자열 두 개를 어떻게 저장하나 했는데 
//temp를 이용하여 담아두고 stoi함수를 이용하였다. 
