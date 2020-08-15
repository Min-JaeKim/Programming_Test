#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int weight_now = 0;
    queue<int> times, entered_weights;
    for(int i =1; ; i++){
        if(i - times.front() == bridge_length){
            int finish = times.front() + bridge_length +1;
            times.pop();
            weight_now -= entered_weights.front();
            entered_weights.pop();
            if(truck_weights.size() == 0 && entered_weights.size() == 0) return finish;
        }
        
        while(1){
            if(truck_weights.front() + weight_now > weight 
                || truck_weights.size() == 0) break;
            else {
                entered_weights.push(truck_weights.front());
                times.push(i);
                weight_now += truck_weights.front();
                truck_weights.erase(truck_weights.begin());
                break;
            }
        }
    }
}
