#include <string>
#include <vector>
#include <cmath>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int index = 0;
    int righthand = 12, lefthand = 10;
    for (auto a : numbers) if (a == 0) a = 11;
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 0) numbers[i] = 11;
        if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
            answer += "R";
            righthand = numbers[i];
        }
        else if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
            answer += "L";
            lefthand = numbers[i];
        }
        else {
            if ((abs(numbers[i] - lefthand) / 3 + abs(numbers[i] - lefthand) % 3)
                < (abs(numbers[i] - righthand) / 3 + abs(numbers[i] - righthand) % 3)) {
                answer += "L";
                lefthand = numbers[i];
            }
            else if ((abs(numbers[i] - lefthand) / 3 + abs(numbers[i] - lefthand) % 3)
                > (abs(numbers[i] - righthand) / 3 + abs(numbers[i] - righthand) % 3)) {
                answer += "R";
                righthand = numbers[i];
            }
            else {
                if (hand == "right") {
                    answer += "R";
                    righthand = numbers[i];
                }
                else {
                    answer += "L";
                    lefthand = numbers[i];
                }
            }

        }
    }

    return answer;
}

/* 이게 뭐라고 푸는 데 그렇게 오래 거렬ㅆ을까,
우선 중간에 있는 숫자들 거리를 계산하는 게
(전화번호 숫자 - 왼손(오른손) 현재누르고 있는 숫자) / 3 
+
(전화번호 숫자 - 왼손(오른손) 현재누르고 있는 숫자) % 3
라는 걸 몰랐다,, 계산 공식 빠르게 구하는 것도 천부적인 능력인듯,,
abs는 <cmath>라는 STL이 필요하다.
절댓값을 구하는 함수임.
그럼 끝*/ 
