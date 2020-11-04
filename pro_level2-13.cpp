#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    vector<int> monster;
        for(int i = 0; i < nums.size(); i++){
            if(monster.size() >= nums.size() / 2) break;
            if(find(monster.begin(), monster.end(), nums[i]) == monster.end())
                monster.push_back(nums[i]);
        }
    answer = monster.size();
    return answer;
}

/*
나름 풀고 잘 풀었다고 생각했는데 다른 사람풀이 보고
아직 한참 멀었다고 생각을 하였다.

#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> nums)
{
    unordered_map<int, int> hash;
    for(auto num : nums){
        hash[num] += 1;
    }
    return min(hash.size(), nums.size() / 2);
}

굿잡,,
unordered_map은 map보다 더 빠른 탐색을 하고,
시간 복잡도는 O(1)이라고 함.
그냥 map은 시간복잡도 O(log n) 
*/ 
