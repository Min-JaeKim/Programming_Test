using namespace std;

long long gcd(int a, int b){
    long c;
    while(b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

long long solution(int w,int h) {
    long long W = w;
    long long H = h;
    long long temp =  (W + H) - gcd(W,H);
    return W * H - temp;
}

/*
gcd로 풀 수 있는 방식을 떠올리지 못했다.
이런 발상을 대체 어떻게 하는 걸까?
그리고 형식이 long long이라서 그걸 해결하는데에도 시간이 많이 걸렸다. 이상
*/ 
