#include <iostream>
#include<vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> board)
{
    int answer = board[0][0];
    for(int i = 1; i < board.size(); i++){
        for(int j = 1; j < board[i].size(); j++){
            if(board[i][j] == 1){
                board[i][j] = min(board[i-1][j], board[i][j-1]);
                board[i][j] = min(board[i-1][j-1], board[i][j]) + 1;
                answer = max(answer, board[i][j]);
            }
        }
    }
    return answer*answer;
}

/*
정사각형 구하는 게 도저히 감이 안와서 다른 사람 풀이를
보았다. 분명 다 이해를 했는데 
answer = 0으로 하니까 계속 실패가 떴다.
반례는 그냥 1만 있는 board였다.
정사각형 크기가 1로 나와야 정상인데,
1이 하나만 있기 때문에 for문에도 들어가지 않는다. 
따라서 answer값을 0으로만 주면 0을 리턴할 수 밖에 없다.
board[0][0]으로 줬어야 됨.

*/ 
