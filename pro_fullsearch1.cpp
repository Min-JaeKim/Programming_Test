#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> a {1,2,3,4,5};
    vector<int> b {2,1,2,3,2,4,2,5};
    vector<int> c {3,3,1,1,2,2,4,4,5,5};
    vector<int> temp(3);
    
    for(int i = 0; i<answers.size(); i++){
            if(answers[i%answers.size()] == a[i%a.size()]) temp[0]++;
            if(answers[i%answers.size()] == b[i%b.size()]) temp[1]++;
            if(answers[i%answers.size()] == c[i%c.size()]) temp[2]++;
    }
    
    int max = *max_element(temp.begin(), temp.end());
    for(int i = 0; i < temp.size(); i++){
        if(max == temp[i]) answer.push_back(i+1);
    }
    
    return answer;
}
