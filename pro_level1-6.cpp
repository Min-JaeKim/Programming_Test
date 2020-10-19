#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    int s_arr1[n][n];
    int s_arr2[n][n];
    for(int i = 0; i < n; i++){
        int temp1 = arr1[i];
        int temp2 = arr2[i];
        for(int j = n-1; j >= 0; j--){
            s_arr1[i][j] = temp1 % 2;
            s_arr2[i][j] = temp2 % 2;
            temp1 /= 2;
            temp2 /= 2;
        }
    }
    for(int i = 0; i<n; i++){
        string temp_ans = "";
        for(int j = 0; j<n; j++){
            if(s_arr1[i][j] + s_arr2[i][j] != 0) temp_ans += '#';
            else temp_ans += ' ';
        }
        answer.push_back(temp_ans);
    }
    
    return answer;
}

//다른 사람 풀이를 보니 비트연산자를 써서 완전 간편하게 푼 사람이 있었다. 대단해 보였다.
/* 내가 이 문제에서 놓치고 있었던 것은
굳이 s_arr1과 2를 먼저 string으로 만들어서 효율성을 죽이는 것.
2진수를 간편하게 만들 수 있는 것.
열심히 하자*/ 
 
