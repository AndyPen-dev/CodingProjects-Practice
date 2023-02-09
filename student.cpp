/* 
Andy Pen
C++ OOP 
Program to help calculate the average of test grades as well as corresponding grade letter

*/ 

#include <iostream>
#include <string>
using namespace std;


//define class Student 
class Student {
public:
//public member functions 
    void input(); //sets weight of quizzes and exams to fixed integers
    void output(); //outputs the whole student record: names & grades

private:
//private member functions
    void calc_ave(); //calculate student's weighted avg numeric score
    void calc_letter(); //calculate student's final letter grade

//private member variables name, quiz, midterm,
//final exam, weighted avg grade, letter grade
    string name;
    string letterGrade;
    float quiz, midterm, finalexam, weighted_avg; 
};


int main(){
    //create 3 objects of class Student 
    Student s[3];

    for(int i = 0; i < 1; i++){
        //input their grades for quizzes and exams
        s[i].input();
        //output student records
        s[i].output();        
    }

    return 0; 
}

void Student::input(){
    cout << "Enter student name: ";
    getline(cin, name); //getline incase user enters first and last name

    cout << "Enter quiz grades: ";
    cin >> quiz;

    cout << "Enter midterm exam grade: ";
    cin >> midterm;

    cout << "Enter final exam grade: ";
    cin >> finalexam;

    //calculate weighted average
    calc_ave();
    calc_letter();
}

void Student::output(){
    cout << name << "'s grades are: " << endl;
    cout << "Quiz grade: " << quiz << endl;
    cout << "Midterm exam grade: " << midterm << endl;
    cout << "Final exam grade: " << finalexam << endl;
    cout << "Student's calculated weighted average numeric score: " << weighted_avg << endl;
    cout << "Student's final letter grade is: " << letterGrade << endl;

}

void Student::calc_ave(){
    //calculate student's weighted average numeric score
    //set weight of quizzes and exams to fixed integers
    //I'll set quizzes as 30%, midterm exam as 30%, final exam as 40%
    weighted_avg = (quiz * .3) + (midterm * .3) + (finalexam * .4);
}

void Student::calc_letter(){
    //calculate the students final letter grade
    if(weighted_avg < 60){
        letterGrade = "F";
    }
    if(weighted_avg >= 60 && weighted_avg <= 66.9){
        letterGrade = "D";
    }
    if(weighted_avg >= 67 && weighted_avg <= 69.9){
        letterGrade = "D+"; 
    }
    if(weighted_avg >= 70 && weighted_avg <= 72.9){
        letterGrade = "C-";
    }
    if(weighted_avg >= 73 && weighted_avg <= 76.9){
        letterGrade = "C"; 
    }
    if(weighted_avg >= 77 && weighted_avg <= 79.9){
        letterGrade = "C+"; 
    }
    if(weighted_avg >= 80 && weighted_avg <= 82.9){
        letterGrade = "B-";
    }
    if(weighted_avg >= 83 && weighted_avg <= 86.9){
        letterGrade = "B";
    }
    if(weighted_avg >= 87 && weighted_avg <= 89.9){
        letterGrade = "B+";
    }
    if(weighted_avg >= 90 && weighted_avg <= 92.9){
        letterGrade = "A-";
    }
    if(weighted_avg >= 93 && weighted_avg <= 96.9){
        letterGrade = "A";
    }
    if(weighted_avg >= 97 && weighted_avg <= 100){
        letterGrade = "A+";
    }

}
