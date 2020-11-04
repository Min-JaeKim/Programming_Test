#include <vector>
#include <iostream>
using namespace std;

bool isPrime(int num){
    for(int i = 2; i < num / 2; i++){
        if(num % i == 0) return false;
    }
    return true;
}

int solution(vector<int> nums) {
    int answer = 0;
    for(int i = 0; i < nums.size(); i++){
        for(int j = i + 1; j < nums.size(); j++){
            for(int m = j + 1; m < nums.size(); m++){
                if(isPrime(nums[i] + nums[j] + nums[m])) answer++;
            }
        }
    }
    return answer;
}



#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool isPrime(int num){
    for(int i = 2; i < num / 2; i++){
        if(num % i == 0) return false;
    }
    return true;
}


/*
int solution(vector<int> nums) {
    int answer = -1;
    int temp = 0;
    vector<int> dec;

    do{
        for(int i = 0; i < 3; i++){
            temp += nums[i];
        }
        if(isPrime(temp)) {
            if(find(dec.begin(), dec.end(), temp) == dec.end())
                dec.push_back(temp);
        }
        temp = 0;
    }while(next_permutation(nums.begin(), nums.end()));
    answer = dec.size();
    return answer;
}
1. 소수를 어떻게 계산해야 할 지 난감했다.
ㄴ 세 개의 수를 더한 값의 절반까지 나누어지는 지에 대한 여부를 확인하기 위해 for문을 돌린다.
ㄴ isPrime으로 구성했는데 문제는 그 다음이다.
2. 조합으로 계산하였더니 곳곳에서 시간초과가 떴다.
ㄴ어떤 사람이 3중 for문 한 걸 보고 유레카를 외쳤다.
3. 한 가지 간과한 것은 중복값 없다는 제한사항이다.
ㄴ조합으로 했을 때는 find, end를 했어야 했지만, 
ㄴ3중 for문으로 하면 안해도 됨. 
*/
