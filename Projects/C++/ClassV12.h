#include <iostream>;

using namespace std;

class ClassV12{
    protected:
    int polymorph;

    public:
    void setpolymorph(int p){
        polymorph = p;
    }

    virtual void polymorphTest(){
        cout << "Polymorphism Trial 0" << endl;
    }
};

class ClassV12v2: public ClassV12{
    public:
        void polymorphTest(){
            cout << "Polymorphism Trial 1 "<< polymorph <<endl;
        }
};

class ClassV12v3: public ClassV12{
    public:
        void polymorphTest(){
            cout << "Polymorphism Trial 2 "<< polymorph <<endl;
        }
};
