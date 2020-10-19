#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    sort(d.begin(), d.end());
    for(int i = 0; i<d.size(); i++){
        if(budget < d[i]) break;
        budget -= d[i];
        answer++;
    }
    return answer;
}
//어렵게 생각했는데 그냥 정렬하고 budget예산에 맞게 계산하면 되는 문제였다. 
