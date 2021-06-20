//CCC Winning Score 19 J1
//July 18, 2019
//By Robin Nash

#include <iostream>

using namespace std;


int main() {
	int a, b, x;
	a = 0;
	b = 0;
	
	for(int i = 3; i>0; i--){
		scanf("%d", &x);
		a += x*i;
	}
	for(int i = 3; i>0; i--){
		scanf("%d", &x);
		b += x*i;
	}
	
	if (a>b)
		printf("%c", 'A');
	else if (b>a)
		printf("%c", 'B');
	else
		printf("%c",'T');
	
}
//1563476764.0