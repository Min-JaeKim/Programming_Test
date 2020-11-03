#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(string expression) {
    long long answer = 0;
    string num;
    vector<long long> v_num;
    vector<char> v_cal;
    vector<char> ex_cal;
    for(int i = 0;  i < expression.length(); i++){
        if(expression[i] == '+' || expression[i] == '*' || expression[i] == '-'){
            v_num.push_back(stoi(num));
            num = "";
            if(find(ex_cal.begin(), ex_cal.end(),expression[i]) == ex_cal.end())
                ex_cal.push_back(expression[i]);
            v_cal.push_back(expression[i]);
        }
        else 
            num += expression[i];
    }
    v_num.push_back(stoi(num));
    sort(ex_cal.begin(), ex_cal.end());
    do{
        vector<long long> tmp_num = v_num;
        vector<char> tmp_cal = v_cal;
        for(int i = 0; i < ex_cal.size(); i++){
            for(int j = 0; j < tmp_cal.size(); j++){
                if(ex_cal[i] == tmp_cal[j]){
                    if(tmp_cal[j] == '+')
                        tmp_num[j] = tmp_num[j] + tmp_num[j+1];
                    else if(tmp_cal[j] == '-')
                        tmp_num[j] = tmp_num[j] - tmp_num[j+1];
                    else if(tmp_cal[j] == '*')
                        tmp_num[j] = tmp_num[j] * tmp_num[j+1];
	                tmp_num.erase(tmp_num.begin() + j + 1);
	                tmp_cal.erase(tmp_cal.begin() + j);
	                j--;
            	}
            }
        }
        answer = answer > abs(tmp_num[0]) ? answer : abs(tmp_num[0]);
    }while(next_permutation(ex_cal.begin(), ex_cal.end()));
    
    return answer;
}


/*
1. set으로 계속 처리하는 것은 무리이므로, 벡터에서 find와 end를 쓸 것
2. set일 때는 변수명.find가 가능하지만 벡터일 때는 안되는 듯.
2-2. 따라서 벡터로 할 때는 find(v.begin, v.end, 찾는 값) == v.end() 이런식으로
3. 벡터에서 값을 지울 때는 clear가 아니라 erase
3-3. erase할 때 괄호에 값을 넣는 게 아니라 인덱스를 넣을 것.
--> dump 됨
ㄴ 원인은 마지막 수를 v_num에 넣지 않았기 때문. 하지만 그래도 값이 틀리다. 원인은?ㄴ
ㄴ 원인은 do~while절 안에 tmp_num과 tmp_cal이라는 임시벡터로 받지 않았기 때문인데
	왜 그렇게 되는지는 이해가 가지 않는다... 
*/     
