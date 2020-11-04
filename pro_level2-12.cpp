#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0, human = 0, avgtime = 0, mintime = 1, maxtime = 0;
    maxtime = *max_element(times.begin(), times.end()) * (long long) n;
    while(mintime <= maxtime){
        avgtime = (maxtime + mintime) / 2;
        for(auto t : times) human += avgtime/t;
        if(n <= human){
            answer = avgtime;
            maxtime = avgtime - 1;
        } else mintime = avgtime + 1;
        human = 0;
    }
    return answer;
}

/*
1. 이분탐색을 처음 해보았다.
2. 9번째 줄에 n을 longlong으로 하는 이유는
times의 수들과 n이 모두 int 형이기때문에 둘이 곱했을 때,
자릿수가 엄청 커져도 int 형이기 때문. 
따라서 n을 long long으로 바꾼 다음에 계산해야 한다.
3. 한 가지 빼먹은 건 마지막에 human을 초기화 해야 한다.
*/ 
