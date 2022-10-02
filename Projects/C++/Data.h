#ifndef DATA.H
#define DATA.H
#include "ClassV7v2.h"
#include <iostream>;

using namespace std;

class Data{
    public:
    Data(ClassV7v2 d, int y):DataTypes(d),num(y){
    }


    void PrintData(){
        DataTypes.PrintDataType();
        cout << " " << num << endl;
    }


    private:
    ClassV7v2 DataTypes;
    int num;
    
    
};

 
#endif