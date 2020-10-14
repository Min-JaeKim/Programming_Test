#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    string temp = ""; //3진법 거꾸로 한 수 문자열로 담기 
    char str =  ""; //stoi를 이용할 문자열(char는 안됨) 
    while(n/3 > 0){
        temp += to_string(n % 3); //3을 나눈 나머지 
        n /= 3;
    }
    temp += to_string(n); //마지막값까지 temp에 저장 
    int cnt = 1; //10진수로 다시 바꿀 곱셈 수
    //거꾸로니까 뒤에 배열부터 3^0 3^1 하여 계산 
    for(int i = temp.length() -1 ; i>=0; i--){
        str = temp[i]; //stoi가 바로 안되기 때문에 별도의 문자열로 저장 
        int check = stoi(str); //check 변수로 stoi한 숫자열 담아줌 
        answer += check * cnt; //10진수로 변환 과정 
        cnt *= 3; //3진수니까 3을 곱하 기 
    }
    
    return answer;
}

/*이게 뭐라고 이렇게 오래 걸려서 풀었나,,
 1. stoi의 사용법을 제대로 몰랐다. (다른 문자열에 문자열 하나 씩  담아둬야됨)
 2. for문에 i--를 하지 않고 i++로 설정해놓았었다. 당연히 될 리 없다. */ 
