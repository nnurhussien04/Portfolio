#include "ClassV7.h"
#include <iostream>;

using namespace std;

const int ConstDefaultValue = 5;

ClassV7::ClassV7():constint(ConstDefaultValue){
    cout << "Successful" << endl;;
}

void ClassV7::PrintFunction(){
    cout << "Unbelievable" << endl;
}

void ClassV7::ConstFunction() const{
    cout << "Constant1" << endl;
}

ClassV7::ClassV7(int x,int y):varint(x),constint(y){
    cout << varint << endl;
    cout << constint << endl;
}



int main(){
    ClassV7 OOP;
    OOP.PrintFunction();
    ClassV7 *ptr = &OOP;
    ptr->PrintFunction();
    const ClassV7 ConstantOOP;
    ConstantOOP.ConstFunction();
    ClassV7 VarOOP(5,8);


}