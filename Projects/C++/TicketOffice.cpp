#include <iostream>
using namespace std;

int main() {
    int ages[5];

    for (int i = 0; i < 5; ++i) {
        cin >> ages[i];
    }
    int discount = ages[0];
    for (int j=0;j<5;j++){
        if(ages[j]<discount){
            discount = ages[j];
        }
    }
    cout << discount << " discount" << endl;
    cout << 50*(discount/100) << endl;

    
    return 0;
}



