//CCC Body Mass Index 08 J1
//April 21, 2019
//By Robin Nash

#include <iostream>

using namespace std;

int main () {
   
   float h;
   float w;
   
   cin >> h;
   cin >> w;
   
   float bmi = h/(w*w);
   if (bmi>25){
	   cout << "Overweight";
   }
   else if (bmi<18.5){
	   cout << "Underweight";
   }
   else{
	   cout << "Normal weight";
   }
   
   int x = 0;
   while(x < 1000000000){
	   x++;
   }
   
   return 0;
   
}

//1555811036.0