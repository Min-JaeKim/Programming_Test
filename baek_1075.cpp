#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N;
    int F;
    cin >> N >> F;
    N = N/100 * 100;
    
    while(1){
    if(N%F == 0) break;
    N += 1;
	}
	string n = to_string(N);
	cout<<n[n.length()-2]<<n[n.length()-1];
    return 0;

}

//문자열로 생각해서 뒤에 두자리수를 0으로 바꾸려고 했는데 
//애초에 나누기를 이용하고 100을 곱하면 뒷 자리수가 00으로 바뀐다. 
