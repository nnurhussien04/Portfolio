#ifndef CLASSV7_H
#define CLASSV7_H
#include "ClassV7v2.h"


class ClassV7
{

    public:
     int num2=0;
     ClassV7();
     void PrintFunction();
     void ConstFunction() const;
     ClassV7(int x,int y);
     

    private:
     int varint;
     const int constint;



};



#endif //ClassV7