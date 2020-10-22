#include <string>
#include <vector>

using namespace std;

vector<int> answer(2); //0과 1을 체크
vector<vector<int>> board;

void box(int x, int y, int size, int first){
    bool keep = true;
    if(size < 2){
        if(board[x][y] == 0) answer[0]++;
        else answer[1]++;
        return;
    }
    for(int i = x; i < x + size; i++){
        for(int j = y; j < y + size; j++){
            if(board[i][j] != first){
                keep = false;
                break;
            }
        }
        if(!keep) break;
    }
    if(keep){
        if(board[x][y] == 0) answer[0]++;
        else answer[1]++;
        return;
    }
    box(x,y,size/2,board[x][y]);
    box(x + (size/2), y, size/2, board[x + (size/2)][y]);
    box(x, y + (size/2), size/2, board[x][y + (size/2)]);
    box(x + (size/2), y + (size/2), size/2, board[x + (size/2)][y + (size/2)]);
    
}

vector<int> solution(vector<vector<int>> arr) {
    int size = arr.size();
    board = arr;
    box(0,0,size,arr[0][0]);
    return answer;
}

/*
내가 도움 받은 것은 대략적인 풀이 방법.
어떻게 풀어야 하는 지 도무지 알 수 없어서 구글링하고, 바로 코드 써내려 갔다.
그리고 arr 또한 전역변수 board를 선언하고 메인함수 담아주는 것 때문에 혼선이 생겼다.
앞으로 문제 푸는 능력을 길러야겠다.
*/ 
