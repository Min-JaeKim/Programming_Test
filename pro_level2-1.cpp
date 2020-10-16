#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    while(n >= 1){
        if(n%3 == 0) {
            answer.insert(0,"4");
            n = n/3 -1;
        }
        else {
            answer.insert(0,to_string(n%3));
            n /= 3;
        }
    }
    return answer;
}

/*3진법으로 할 생각을 못했다..*/ 
