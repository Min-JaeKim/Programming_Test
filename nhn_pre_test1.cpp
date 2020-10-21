#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 10

int arr[MAX][MAX];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
bool check[MAX][MAX];
int number;


void dfs(int x, int y, int sizeOfMatrix, int **matrix){
	number++;
	check[x][y] = true; //이 코드 넣는 거 까먹어서 타임아웃 
	for(int i = 0; i<4; i++){
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx < 0 || ny < 0 || nx >= sizeOfMatrix || ny >= sizeOfMatrix) continue;
		if (!check[nx][ny] && matrix[nx][ny]){
			dfs(nx,ny,sizeOfMatrix, matrix);
		}
	}
}

void solution(int sizeOfMatrix, int **matrix) {
  // TODO: 이곳에 코드를 작성하세요.
	vector<int> v;
	for(int i = 0; i<sizeOfMatrix; i++){
		for(int j = 0; j<sizeOfMatrix; j++){
			if(matrix[i][j] && !check[i][j]){
				number = 0; //이부분을 어떻게 해야할 지 몰라서 다른 코딩 참조. 
				dfs(i,j,sizeOfMatrix, matrix);
				v.push_back(number);
			}
		}
	}
	sort(v.begin(), v.end());
	cout<<v.size()<<'\n';
	for(auto a : v) cout<<a<<' ';

}

struct input_data {
  int sizeOfMatrix;
  int **matrix;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.sizeOfMatrix;

  inputData.matrix = new int*[inputData.sizeOfMatrix];
  for (int i = 0; i < inputData.sizeOfMatrix; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    inputData.matrix[i] = new int[inputData.sizeOfMatrix];
    for (int j = 0; j < inputData.sizeOfMatrix; j++) {
      iss >> inputData.matrix[i][j];
    }
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.sizeOfMatrix, inputData.matrix);
  return 0;
}
