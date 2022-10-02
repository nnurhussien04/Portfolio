#include <iostream>;

using namespace std;

class ClassV13{
    public:

    virtual void AbstractTest() = 0;
};

class ClassV13v2: public ClassV13{
    public:
        void AbstractTest(){
            cout << "Abstract Trial 1 "<< endl;
        }
};

class ClassV13v3: public ClassV13{
    public:
        void AbstractTest(){
            cout << "Abstract Trial 2 "<< endl;
        }
};
