#include <string>
#include <vector>
#include <iostream>
#define min_int 6565
#define max_int 9797

using namespace std;

int check[2][max_int+1];

bool checkalpha(char s){
    bool result = false;
    if((65 <= s && s <= 90) || (97 <= s && s <= 122)) result = true;
    return result;
}

char totoupper(char s){
    if(97 <= s) s-=32;
    return s;
}

int solution(string str1, string str2) {
    int answer = 0;
    double temp_result = 0, s_union = 0, s_set = 0;
    vector<string> v;
    v.push_back(str1);
    v.push_back(str2);
    for(int i =0; i < 2; i++){
        string word = v[i];
        for(int j = 1; j < (int)v[i].length(); j++){
            char s1 = word[j-1];
            char s2 = word[j];
            if(checkalpha(s1) && checkalpha(s2)){
                s1 = totoupper(s1);
                s2 = totoupper(s2);
                int num = s1 *100 + s2;
                check[i][num]++;
            }
        }
    }
    for(int i = min_int; i <= max_int; i++){
        s_union += max(check[0][i], check[1][i]);
        s_set += min(check[0][i], check[1][i]);
    }
    cout<<s_union<<' '<<s_set<<' ';
    if(s_union != 0){
        temp_result = s_set / s_union;
        answer = (int)(temp_result * 65536);
    } else answer = 65536;
    return answer;
}

/*
문자열 처리를 엉망진창으로 했나보다.
일단 내가 했던 것, 
1. 두 개의 문자가 알파벳인지 확인하고,
2.   t_str1[i-1]에 tolower한 상태로 push_back하는 것.
3. 하지만 벡터형을  vector<vector<string>> t_str1;
 이상하게 선언했던 건지, 계속 push_back에서 오류남.
4. 어떻게 처리를 계속 하다가 결국 막혔다.
두 글자 씩 담은 벡터를 정렬한 것이 앞 뒤가 똑같으면
중복값 1증가 유일값 1감소, 평소에는 계속 유일 값 1증가하였다.
5. 하지만 발생한 문제가 뭐였냐면
중복값이 3개 이상일 경우에도 유일값이 1씩 증가하였기에
풀리지 않았다.
6. 해결하기 위해서 결국 해답을 보았다. 해답은 
7. 해당 문자열의 갯수를 세는 것이다.

8.하,,, 코드는 맞았는데 계속 틀렸다고 나와서
밥도 못먹고 세 시간째 붙잡고 있었는데
9. 원인은 check 배열을 전역변수로 선언해주지 않았기
때문이다. 전역변수는 초기화를 하지 않아도 항상
0으로 초기화 되어 있다. 
만약 내가 지역변수를 사용하려면 초기화를 꼭,,
해줘야 한다. 
이런 허무한 걸로 시간 잡아 먹지 않게 기초를
탄탄히 해야겠다 ㅠㅠㅠㅠ 
