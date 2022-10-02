#include <iostream>;
using namespace std;


template <class T>
class TemplateClassV2{
    public:
        TemplateClassV2(T x){
            cout <<x<<" - not a char"<<endl;
        }
};

template < > 
class TemplateClassV2<char>{
    public:
        TemplateClassV2(char x){
            cout<<x<<" is a char!"<< endl;
        }

};

