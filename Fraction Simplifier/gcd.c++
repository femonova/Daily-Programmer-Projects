#include <iostream>
#include <string>
using namespace std;

int gcd(int a, int b){

  if(b == 0)
    return a;
  else
    return gcd(b, a%b);
}

void simplify(int a, int b){
  int value = gcd(a, b);

  cout << a/value << " / " << b/value << endl;

}
int main(void){

  string list[] = {"1 2", "1536 78360", "51478 5536", "46410 119340", "7673 4729", "4096 1024"};

  for(int i = 0; i < 6; i++)
  {
    int pos = list[i].find(" ");

    int a = stoi(list[i].substr(0,pos));
    int b = stoi(list[i].substr(pos+1));
    simplify(a,b);
  }

}
