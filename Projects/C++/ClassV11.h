#include <iostream>;
#include <string>;

using namespace std;


class ClassV11{
    public:
        ClassV11(){
            cout << "Constructor Base " << endl;
        };
        ~ClassV11(){
            cout << "Destructor Base" << endl;
        }
    
    void Father(){
        cout << "Father Class" << endl;
    };

    protected:
    int x;
};

class ClassV11v2: public ClassV11{
    public:
        ClassV11v2(){
            cout << "Constructor Derived" << endl;
        };
        ~ClassV11v2(){
            cout << "Destructor Derived" << endl;
        }
        
    void xtra(){
        x = 50;
        cout << x << endl;
    }
    

};


