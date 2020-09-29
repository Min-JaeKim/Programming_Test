#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    vector<vector<int>> tmp (triangle.size(),vector<int>(triangle.size()));
    tmp[0] = triangle[0];
    for(int i = 1; i < triangle.size();i++){
        for(int j = 0; j <= i; j++){
            if(j == 0)
                tmp[i][j] = triangle[i][j] + tmp[i-1][j];
            else if (j == i)
                tmp[i][j] = triangle[i][j] + tmp[i-1][j-1];
            else
                tmp[i][j] = triangle[i][j] + max(tmp[i-1][j-1],tmp[i-1][j]);
            if(i == triangle.size() -1)
                answer = max(answer,tmp[i][j]);
        }
    }
    return answer;
}

//우왕 이렇게 푸는 건 정말 획기적이었으나,, 2차원 vector 초기화하는 방법을 잘 몰라서 좀 헤맸다.. 공부할 것,, 
