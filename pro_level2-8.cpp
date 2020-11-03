#include <string>
#include <vector>

using namespace std;

char kakao[8] = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
bool visited[8] = {false,};
vector<char> V;
int answer;

void DFS(int n, vector<string> data, int cnt){
    if(cnt == 8) {
        for(int i = 0; i < n; i++){
            char c1 = data[i][0];
            char c2 = data[i][2];
            char cal = data[i][3];
            int dist = data[i][4] - '0';
            dist++;
            int idx, iidx;
            idx = iidx = -1;
            for(int j = 0; j < 8; j++){
                if(V[j] == c1) idx = j;
                if(V[j] == c2) iidx = j;
                if(idx != -1 && iidx != -1) break;
            }
            if(cal == '=' && abs(idx - iidx) != dist) return;
            if(cal == '>' && abs(idx - iidx) <= dist) return;
            if(cal == '<' && abs(idx - iidx) >= dist) return;
        }
        answer++;
        return;
    }
    for(int i = 0; i < 8; i++){
        if(visited[i]) continue;
        visited[i] = true;
        V.push_back(kakao[i]);
        DFS(n, data, cnt + 1);
        V.pop_back();
        visited[i] = false;
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data) {
    answer = 0;
    DFS(n, data, 0);
    return answer;
}

/*
1. 문자열 처리
1-1. 카카오캐릭터들은 char로 변수 선언
1-2. 데이터 안에 있는 제약 사항을 어떻게 처리하는 지
1-3. 문자열 마지막은 '0' 빼줄 것.
1-4. dist가 0이라고 한 다면 거리는 1로 만들어줘야됨.
1-5. idx로 캐릭터가 있는 위치를 내타내주고. 절대값 계산 

2. 전역변수를 솔루션 함수에서 초기화 하지 않았기 때문에
계속 실패가 떴었다. 
*/
