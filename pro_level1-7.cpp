#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    vector<string> day = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
    int temp = 0;
    switch(a){
        case 1 : 
            temp = b % 7;
            break;
        case 2 :
            temp = (31 + b) % 7;
            break;
        case 3 :
            temp = (31 + 29 + b) % 7;
            break;
        case 4 :
            temp = (31 + 29 + 31 + b) % 7;
            break;
        case 5 :
            temp = (31 + 29 + 31 + 30 + b) % 7;
            break;
        case 6 :
            temp = (31 + 29 + 31 + 30 + 31 + b) % 7;
            break;
        case 7 :
            temp = (31 + 29 + 31 + 30 + 31 + 30 + b) % 7;
            break;
        case 8 :
            temp = (31 + 29 + 31 + 30 + 31 + 30 + 31 + b) % 7;
            break;
        case 9 :
            temp = (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + b) % 7;
            break;
        case 10 :
            temp = (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + b) % 7;
            break;
        case 11 :
            temp = (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + b) % 7;
            break;
        case 12 :
            temp = (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + b) % 7;
            break;
    }
    if(temp == 0) answer = day[6];
    else answer = day[temp -1];
    return answer;
}

/*ㅋㅋㅋ,,, 시간 복잡도 줄이면서 풀었다고 생각했는데
나와 비슷하게 푼 사람이 비웃음 당하고 있었다...
앞으로 더 코드 줄을 줄이는 방안으로 코딩해야겠다..*/ 
