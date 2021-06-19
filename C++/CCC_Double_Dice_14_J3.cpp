//CCC Double Dice 14 J3
//April 20, 2019
//By Robin Nash

#include <iostream>

using namespace std;

int main () {
   //
   int antonia = 100;
   int david = 100;
   int rolls, a, d;
   cin >> rolls;
   for (int i=0; i<rolls; i++){
	   cin>> a >> d;
	   
	   if (a>d){
		   david = david - a;
	   }
	   else if (d>a){
		   antonia = antonia - d;
	   }
	   
   }
   cout << antonia << endl;
   cout << david;
   
   int x = 0;
   while(x < 1000000000){
	   x++;
   }
   
   return 0;
   
}

//1555804768.0