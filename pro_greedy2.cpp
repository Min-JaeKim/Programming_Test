#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    for(int i =0, index = -1; i<number.length()-k; i++){
        int max = 0;
        for(int j = index + 1; j <= k+i; j++ ){
            if(max < number[j]){
                index = j;
                max = number[j];
            }
        }
        answer += max;
    }
    return answer;
}

//이문제는 아직도 이해 못하겠다,, 그냥 외워야지.. 
