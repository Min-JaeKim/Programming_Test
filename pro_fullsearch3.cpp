#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    for(int i = 0; i<brown/2; i++){
        for(int j = 0; j <= i; j++){
            if(i * j - brown == yellow && i*2 + j*2 - 4 ==brown ){
                answer.push_back(i);
                answer.push_back(j);
            }
        }
    }
    return answer;
}
