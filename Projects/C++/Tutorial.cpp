#include <iostream>;
#include <string>;
#include <cstdlib>;
#include <ctime>;
#include <fstream>;

using namespace std;


//Functions
     
/*void TestFunction(){
    cout << 9 << endl;
}

void TestFunctionV2();

void TestFunctionV3(int x){
    cout << x << endl;
}

void TestFunctionV4(int x){
    cout << x/2 << endl;

}

int TestFunctionV5(int x,int y){
    int answer = x*y;
    return answer;
}

int TestFunctionV6(int x,int y = 5){
    int answer = x/y;
    return answer;
}

int TestFunctionV5(double x,double y){
    int answer = x*y;
    return answer;
}

int TestFunctionV7(int x){
    if (x<=1){
        return 1;
    } else{
        return x + TestFunctionV7(x-1);
    }
}

void TestFunctionV8(int arr[], int size){
    for(int i=0;i<size;i++){
        cout << arr[i] << endl;
    }
}

void TestFunctionV9(int *x){
    cout << *x << endl;
}*/

//OOP
class ClassV1{
    public:
    void Method1(){
        cout << "Hello" << endl;
    }
};

class ClassV2{
    public:
    int x = 5;
    void Method1(){
        cout << "Testing" << endl;
        cout << x << endl;
    }
    private:
    int y = 6;

};

class ClassV3{
    private:
    int x = 80;

    public:
    int getX(){
       return x;
    }
};

class ClassV4{
    public:
    void setX(int parameterx){
        x = parameterx;
    }

     int getX(){
        return x;
    }

    private:
    int x;
};

class ClassV5{
    public:
    ClassV5() {
        cout << "Constructor" << endl;
    }
};

class ClassV6{
    public:
    int y;
    ClassV6(int x){
        y = x;
    }
    int getY(){
        return y;
    }
};

class ClassV8{
    public:
    ClassV8(){

    }
    ~ClassV8(){ 

    }
};

class ClassV9{
    public:
    ClassV9(int x,int y): varint(x),constint(y){
        cout << varint << endl;
        cout << constint << endl;

    }
    private:
        int varint;
        const int constint;

};

class ClassV10{
    public:
     ClassV10(){
        num = 0;
    }
    private: 
     int num;

    friend void privateAccess(ClassV10 &c,int x);
};

void privateAccess(ClassV10 &c, int x){
    c.num = x;
    cout << c.num;
};


int main(){


    //C++ intro
    /*cout << "Hello world"; //prints Hello World
    cout << "This " << "is " << "awesome!" << endl;
    cout << "Nebil \n"; 
    cout << "Nurhussien \n";
    int No = 10;
    cout << No;
    int No2 = 50;
    int sum = No+No2;
    cout << sum << endl;*/
    
    //Variables
    /*int num, num2;
    cout << "Input a number \n ";
    cin >> num;
    cout << num;
    cout << "Input another number ";
    cin >> num2;
    int total = num + num2;
    cout << "Total is " << total << endl;
    int total2 =+ (num/num2);
    cout << total2;*/

    /* If else statements*/
    /*string Name;
    cin >> Name;
    if (Name == "Nebil"){
        cout << "Hello Nebil";
    }
    else{
        cout << "Hello";
    }*/
    /*int Num4;
    cout << "Enter a Number \n";
    cin >> Num4;
    if (Num4>=5){
        cout << "Successful ";
        if(Num4>=10){
            cout << "Excellent Score";
        }
    }
    else{
        cout << "Fail ";
        cout << "Try Again";
    }*/

    //While Loop

    /*int x=0;
    while (x<5){
        cout << x << endl;
        x++;
    }
    int pin;
    cout << "Enter the Pin: ";
    cin >> pin;
    while (pin!=1234){
            cout << "Enter the Pin: ";
            cin >> pin;
    }

    int sum;
    int total=0;
    cout << "Enter the No";
    cin >> sum;
    int y = 0;
    int no = sum;
    while( y != no){
        total+=sum;
        y++;
        cout << total << endl;
    }*/

    /*For Loop*/

    /*for(int i=0;i<10;i++){
        cout << i << endl;
    }
    for(int j=0;j<30;j+=3){
        cout << j << endl;
    }*/

    /*Do While Loop*/
    /*int x = 0;
    do{
        cout << x << endl;
        x++;
    }
    while(x<10);
    x=0;
    int total=0;
    do{ 
        x++;
        total=x;
        total+=total;
        cout << total << endl;
    }
    while(x<10);*/

    /*Switch Statement*/

    /*int x;
    cout << "Enter a Number ";
    cin >> x;
    switch(x){
        case 1:
            cout << 1;
            break;
        case 2:
            cout << 2;
            break;
        case 3:
            cout << 3;
            break;
        default:
            cout << "Unknown";
            break;
    }*/

    /*Logical Operators*/

    /*int age = 20;
    if(age > 16 && age < 60){
        cout << "Accepted" << endl;
    }
    else if(age > 10 || age < 20){
        cout << "Okay" << endl;
    }
    else if(age != 20){
        cout << "Intresting";
    }
    else{
        cout << "Never Mind";
    }*/

    /*Data Types*/

    /*string a = "Nebil";
    char n = 'n';
    bool check = true;
    float decimal = 0.21;
    double decimal2 = 9.41;*/
    
    

    /*Arrays*/
    /*int array[5] = {12,4,7,3,9};
    cout << array[0] << endl;
    cout << array[3] << endl;
    for (int i =0;i<=4;i++){
        array[i]=i*5;
        cout << array[i] << endl;
    }
    int sum=0;
    for (int j=0;j<5;j++){
        sum+= array[j];
    }
    cout <<  "Answer is: "<< sum << endl;

    int array_2d[3][3] = {{2,4,5}, {3,5,6}};
    cout << array_2d[1][2] << endl;*/
    

   //Pointers
   /*int pointer = 19;
   cout << &pointer << endl;
   int *pointerPtr;
   pointerPtr = &pointer;
   cout << pointerPtr << endl;
   int x = 9; int y=0;
   int * px = &x;
   int * py = &y;
   *px += *py;
   cout << px << " " << py << endl;*/

   //Dynamic Memory
   /*int *x = new int;
   *x = 9;
   cout << x << endl;
   delete x;*/

   //sizeof 

    /*int x;
    cout << sizeof(x) << endl;*/

    //Functions
    /*TestFunction();
    TestFunctionV2();
    TestFunctionV3(4);
    TestFunctionV4(8);
    TestFunctionV4(5);
    TestFunctionV4(12);
    cout << TestFunctionV5(20,10);
    cout << rand();
    srand(time(0));
    for (int i=0;i<5;i++){
        cout << 5 + (rand() % 10) << endl;
    }
    cout << TestFunctionV6(6,2) << endl;
    cout << TestFunctionV5(0.5,2.5) << endl;
    cout << TestFunctionV7(4) << endl;
    int array[] = {2,3,5};
    TestFunctionV8(array,3);
    int x = 9;
    TestFunctionV9(&x);*/

    //OOP
    /*ClassV1 OOPTest;
    OOPTest.Method1();

    ClassV2 OOPTest2;
    OOPTest2.Method1();

    ClassV3 OOPTest3;
    cout << OOPTest3.getX();

    ClassV4 OOPTest4;
    OOPTest4.setX(14);
    cout << OOPTest4.getX() << " Successful" << endl;

    ClassV5 OOPTest5;

    ClassV6 OOPTest6(5);
    cout << OOPTest6.getY() << endl;

    ClassV8 OOPTest7;*/

    //Constants 
    //const int x = 10;
    //cout << x << endl;

    //const ClassV3 OOPTest;
    //ClassV9 OOPTest2(9,5);


    //Friends
    //ClassV10 CV10;
    //privateAccess(CV10,5);

    //Exceptions
   /* int Trial1 = 35;
    int Trial2 = 40;
    if (Trial2 > Trial1){
        //throw "Unsuccessful";
    }
    try{
        Trial1 = 59;
        Trial2 = 96;
        if (Trial2 > Trial1){
            throw 90;
        }
    }
    catch(int x){
        cout << "Wrong Number"<<x;
    }

    try{    
        int no1;
        cin >> no1;
        int no2;
        cin >> no2;

        if (no2 == 0){
            throw 0;
        }

        cout << "Result" << no1/no2;
    }

    catch(int x){
        cout << "Division by zero";
    }*/

    //Files
    /*ofstream File;
    //File.open("FileTest.txt");
    File.open("FileTest.txt",ios::out | ios::app);
    if (File.is_open()){
    File << "Test129 \n";
    }
    else{
        cout << "error" << endl;
    }*/

    ifstream File("FileTest.txt");
    string line;
    while (getline(File,line)){
        cout << line << '\n';
    }
    File.close();



















    
    return 0;



}






void TestFunctionV2(){
    cout << "Successful" << endl;

}




