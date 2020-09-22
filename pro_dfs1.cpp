#include <string>
#include <vector>

using namespace std;

void dfs(vector<int>& numbers, int target, int& answer, int count = 0, int sum = 0){
    if(count == numbers.size() - 1){
        if(target == numbers[count] + sum) answer++;
        if(target == sum - numbers[count]) answer++;
        return;
    }
    dfs(numbers,target,answer,count + 1, sum + numbers[count]);
    dfs(numbers,target,answer, count + 1, sum - numbers[count]);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(numbers,target,answer);
    return answer;
}
