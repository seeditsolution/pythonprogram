#include<iostream>
using namespace std;
class test{
    public:
    test()
    {
        cout<<"constructor"<<endl;
    }
    ~test()
    {
        cout<<"destructor"<<endl;
    }

};
int main()
{
    test();
  //  test t;
    //t.~test();
    return 0;
    }
