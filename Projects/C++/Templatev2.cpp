#include "ClassTemplate.h";
#include <iostream>;
using namespace std;
template <class S,class N>

S smaller (S x,N y){
    return (x<y ? x:y);
}

int main(){
    int x = 5;
    double y = 9.412;
    cout << smaller(x,y);
    

}