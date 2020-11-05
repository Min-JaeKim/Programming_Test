#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    bool flag = false;
    while(!flag){
        vector<vector<bool>> visited(m, vector<bool>(n));
        flag = true;
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                string s1 = board[i-1];
                string s2 = board[i];
                if(!board[i-1][j-1]) continue;
                if(s1[j-1] == s1[j] && s1[j-1] == s2[j-1] && s1[j] == s2[j]){
                    visited[i-1][j-1] = true;
                    visited[i-1][j] = true;
                    visited[i][j-1] = true;
                    visited[i][j] = true;
                    flag = false;
                }
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(visited[i][j]) {
                    answer++;
                    for(int k = i-1; k >= 0; k--){
                        board[k + 1][j] = board[k][j];
                        board[k][j] = 0;
                    }
                }
            }
        }
    }
    return answer;
}
/*
1. 이미 처리한 부분을 어떻게 삭제하지?
ㄴ 삭제해야 할 부분을 1로 바꾸어서 1 위에 있는 배열을 1자리로 내림.
2. 어떻게 2x2를 골라내는지?
ㄴif문
3. ha,,,,원인은 모르겠는데 visited를 bool visitied[m][n]
으로 선언했더니 계속 오류가 났다.
일단 배열 선언은 변수로 선언하지 말아야 하기 때문에
오류가 나는 것은 알겠는데,
그럼 배열로 어떻게 선언해야 돌아가는가를 못알아냈다..
무튼,, 배열 선언이 힘들면
4. 벡터로 선언할 것.... 
*/
