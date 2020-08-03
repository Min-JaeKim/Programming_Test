#include <iostream>
#include <algorithm>

using namespace std;

class Student {
	public :
		string name;
		int score;
	Student (string name, int score){
		this->name = name;
		this->score = score;
	}
	bool operator < (Student &student){
		return this->score < student.score;
	}
};

int main(void){
	Student students[] = {
		Student("³ª",90),
		Student("±è",99),
		Student("ÀÌ",85),
		Student("¹Ú",44),
		Student("ÃÖ",68)
	};
	sort(students, students + 5);
	for (int i = 0; i<5; i++)
	cout<<students[i].name<<' ';
	return 0; 
}
