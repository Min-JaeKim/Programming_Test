#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack<int> s; //인형을 담아둘 스택;
    for(int j = 0; j < moves.size(); j++){
        for(int i = 0; i<board.size(); i++){
            if(board[i][moves[j] -1] != 0){
                if(!s.empty() && s.top() == board[i][moves[j] -1]) {
                    board[i][moves[j] -1] = 0;
                    answer+=2;
                    s.pop();
                    break;
                    }
                    else {
                    s.push(board[i][moves[j] -1]);
                    board[i][moves[j] -1] = 0;
                        break;
                }
                }
            }
        }
    return answer;
}

/*내가 그동안 break를 잘못 알고 있었다는 걸 오늘 깨달았다.
이중 포문 안에 break를 걸면 두 개의 포문이 끝나는 게 아니라
break를 걸었던 그 포문이 끝난다.. 이걸 왜 이제 알았을까 멍청이다.. 
하여간에 소스코드를 너무 조잡하게 짰었다.
코드를 줄이는 방법을 깨우칠것..*/ 
