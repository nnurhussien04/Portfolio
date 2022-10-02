#include <cstdlib>;
#include <iostream>;
#include "Data.h";
#include "ClassV7v2.h";
#include "ClassV11.h";
#include "ClassV12.h";
#include "ClassV13.h";
#include "ClassTemplate.h";
#include "ClassTemplateV2.h"


using namespace std;

template <class T>
T TemplateClass<T>::bigger(){
   return (x>y ? x : y);
}



int main(){
    int y = 5;
    double d = 9.5;
    bool false1 = true;
    ClassV7v2 Class1(y,d,false1);
    Data data_types(Class1,y);
    data_types.PrintData();
    ClassV7v2 Class2(15),Class3(30);
    ClassV7v2 Answer = Class2 +Class3;
    cout << Answer.num2 << endl;
    ClassV11v2 Class4;
    Class4.Father();
    Class4.xtra();
    ClassV12v2 Object5;
    ClassV12v3 Object6;
    ClassV12 *Object7 = &Object5;
    ClassV12 *Object8 = &Object6;
    Object7 ->setpolymorph(15);
    Object8 ->setpolymorph(25);
    Object5.polymorphTest();
    Object6.polymorphTest();
    Object7 -> polymorphTest();
    Object8 -> polymorphTest();
    ClassV12 Object9;
    ClassV12 *Object10 = &Object9;
    Object10 -> polymorphTest();
    ClassV13v2 Object11;
    ClassV13v3 Object12;
    ClassV13 *Object13 = &Object11;
    ClassV13 *Object14 = &Object12;
    Object13 -> AbstractTest();
    Object14 -> AbstractTest();
    TemplateClass <int> Object15(24,16);
    cout << Object15.bigger() << endl;
    TemplateClassV2<int> Object16(15);
    TemplateClassV2<double>Object17(15.92);
    TemplateClassV2<char>Object18('IS');





}