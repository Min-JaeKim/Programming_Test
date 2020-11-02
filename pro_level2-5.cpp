#include <vector>
#include <queue>

using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs(int x, int y, int m, int n, vector<vector<int>> picture, vector<vector<bool>>& visited){
     visited[x][y] = true;
    int color = picture[x][y];
    int area = 0;
    queue<pair<int, int>> q;
    q.push(make_pair(x,y));
    
    while(!q.empty()){
        area++;
        int t_x = q.front().first;
        int t_y = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++){
            int nx = t_x + dx[i];
            int ny = t_y + dy[i];
            if(nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
            if(!visited[nx][ny] && picture[nx][ny] == color){
                q.push(make_pair(nx,ny));
                visited[nx][ny] =true;
            }
        }
    }
    return area;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int temp;
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(!visited[i][j] && picture[i][j]!=0) {
                number_of_area++;
                temp = bfs(i, j, m, n, picture, visited);
                max_size_of_one_area = temp > max_size_of_one_area ? temp : max_size_of_one_area;
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

/*
1. bool값을 vector로 초기화하는 것 
2. 구간마다 갯수 세는 거(temp를 이용해서 max값과 비교하기)
*/ 
