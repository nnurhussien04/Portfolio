#include <iostream>;
using namespace std;
template <class DTDM>






DTDM sum (DTDM a,DTDM b){
    return a+b;
};





int main(){
    cout << sum(5,9) << endl;
    cout << sum(true,false)<< endl;
    cout << sum(9.23,9.92) << endl;
}


