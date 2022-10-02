#ifndef CLASSV7V2
#define CLASSV7V2

#include <iostream>;
using namespace std;


class ClassV7v2
{
    public:
        int num2;

        ClassV7v2(){};

        ClassV7v2(int n,double d,bool b) : num(n),decimal(d),boolean(b){
            cout << this-> decimal<< " Test Value" << endl;
        };

        ClassV7v2(int a):num2(a) {};

        void PrintDataType(){
            cout << num << " The number variable" << endl;
            cout << decimal << " The double variable" << endl;
            cout << boolean << " The boolean variable" << endl;

        };

        
    ClassV7v2 operator+(ClassV7v2 &c){
        ClassV7v2 Answer;
        Answer.num2 = this->num2 + c.num2;
        return Answer;
    };

    private:
        int num;
        double decimal;
        bool boolean;
    




};



#endif